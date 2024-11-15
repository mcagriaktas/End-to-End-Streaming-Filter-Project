import org.apache.spark.sql.{SparkSession, DataFrame}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.{StructType, StructField, StringType, DoubleType}
import play.api.libs.json._

object StreamingApp {
  def main(args: Array[String]): Unit = {
    val spark: SparkSession = initiliazSpark()
    import spark.implicits._

    val kafkaDF: DataFrame = read_raw_topic(spark)
    spark.sparkContext.setLogLevel("WARN")

    val schemaRegistryUrl = "http://kafka-schema-registry:18081"
    val structSchema = fetchSchemaFromRegistry(spark, schemaRegistryUrl, "raw-value")

    val data = kafkaDF
      .selectExpr("CAST(value AS STRING) as json")
      .select(from_json(col("json"), structSchema).as("data"))
      .select("data.*")

    val (lowTopic, midTopic, highTopic) = filterData(data)

    writeToKafka(lowTopic, "low")
    writeToKafka(midTopic, "mid")
    writeToKafka(highTopic, "high")

    spark.streams.awaitAnyTermination()
  }

  def filterData(data: DataFrame): (DataFrame, DataFrame, DataFrame) = {
    val lowTopic = data.filter(col("balance") <= 500)
    val midTopic = data.filter(col("balance") > 500 && col("balance") <= 2000)
    val highTopic = data.filter(col("balance") > 2000)
    (lowTopic, midTopic, highTopic)
  }

  def writeToKafka(data: DataFrame, topic: String): Unit = {
    data.selectExpr("CAST(id AS STRING) as key", "to_json(struct(*)) AS value")
      .writeStream
      .format("kafka")
      .option("kafka.bootstrap.servers", "kafka1:9192,kafka2:9192,kafka3:9192")
      .option("topic", topic)
      .option("checkpointLocation", s"/tmp/checkpoints/$topic")
      .outputMode("append")
      .start()
  }

  def read_raw_topic(spark: SparkSession): DataFrame = {
    val kafkaBrokers: String = "kafka1:9192,kafka2:9192,kafka3:9192"
    val topicName: String = "raw"

    val kafkaDf: DataFrame = spark.readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", kafkaBrokers)
      .option("subscribe", topicName)
      .option("startingOffsets", "latest")
      .load()

    kafkaDf
  }

  def initiliazSpark(): SparkSession = {
    SparkSession.builder()
      .appName("KafkaConsumerApp")
      .master("local[*]")
      .config("spark.jars.packages",
        "org.apache.spark:spark-core_2.12:3.5.3," +
        "org.apache.spark:spark-sql_2.12:3.5.3," +
        "org.apache.spark:spark-streaming_2.12:3.5.3," +
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3," +
        "org.apache.kafka:kafka-clients:3.5.1," +
        "com.typesafe.play:play-json_2.12:2.9.4"
      )
      .getOrCreate()
  }

  def fetchSchemaFromRegistry(spark: SparkSession, schemaRegistryUrl: String, subject: String): StructType = {
    val url = s"$schemaRegistryUrl/subjects/$subject/versions/latest"
    val response = scala.io.Source.fromURL(url).mkString
    val json = Json.parse(response)
    val schemaString = (json \ "schema").as[String]

    val schemaJson = Json.parse(schemaString)
    
    val fields = (schemaJson \ "fields").as[Seq[JsObject]].map { field =>
      val fieldName = (field \ "name").as[String]
      val fieldType = (field \ "type").as[String] match {
        case "string" => StringType
        case "double" => DoubleType
        case _ => StringType
      }
      StructField(fieldName, fieldType, nullable = true)
    }
    StructType(fields)
  }
}
