# Use OpenJDK base image
FROM openjdk:17-slim-bullseye

# Install necessary packages
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Create directory for Schema Registry installation
RUN mkdir /opt/schema-registry && \
    curl -SL "https://packages.confluent.io/archive/7.3/confluent-community-7.3.0.tar.gz" \
    -o /opt/schema-registry/confluent.tar.gz && \
    mkdir /schema-registry && cd /schema-registry && \
    tar -xvzf /opt/schema-registry/confluent.tar.gz --strip 1 && \
    rm /opt/schema-registry/confluent.tar.gz

# Create data directory for Schema Registry (if needed)
RUN mkdir -p /data/schema-registry

# Copy custom start script (if you have one)
COPY start-schema-registry.sh /usr/bin/start-schema-registry.sh
RUN chmod +x /usr/bin/start-schema-registry.sh

# Expose the default Schema Registry port
EXPOSE 18081

# Set the working directory
WORKDIR /schema-registry

# Command to start Schema Registry
CMD ["/usr/bin/start-schema-registry.sh"]