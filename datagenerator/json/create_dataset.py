from faker import Faker
import random
import json

fake = Faker()

# Number of users and total rows
num_users = 10000
num_rows = 1000000
rows_per_user = num_rows // num_users

# Step 1: Generate unique users with an initial balance
users = []
user_balances = {}  # Dictionary to store current balance for each user

for _ in range(num_users):
    user_id = fake.uuid4()
    initial_balance = round(random.uniform(1000, 5000), 2)  # Initial balance between 1000 and 5000
    user = {
        "id": user_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "balance": initial_balance
    }
    users.append(user)
    user_balances[user_id] = initial_balance  # Initialize balance in dictionary

# Step 2: Generate transactions for each user, updating balance with each transaction
transactions = []
for user in users:
    user_id = user["id"]
    for _ in range(rows_per_user):
        # Simulate a random transaction (deposit or withdrawal)
        transaction_amount = round(random.uniform(-500, 500), 2)  # Transaction amount between -500 and 500
        new_balance = round(user_balances[user_id] + transaction_amount, 2)
        
        # Ensure balance doesn’t go below zero
        if new_balance < 0:
            new_balance = user_balances[user_id]  # Skip transaction if it results in negative balance
        
        # Record the transaction
        transaction = {
            "id": user_id,
            "first_name": user["first_name"],
            "last_name": user["last_name"],
            "balance": new_balance
        }
        transactions.append(transaction)
        
        # Update user balance in the dictionary
        user_balances[user_id] = new_balance

# Step 3: Shuffle transactions to mix user records for realistic streaming simulation
random.shuffle(transactions)

# Step 4: Write shuffled data to file
with open("shuffled_bank_dataset.json", "w") as f:
    f.write("[\n")  # Start of JSON array
    for i, transaction in enumerate(transactions):
        json.dump(transaction, f)
        if i != len(transactions) - 1:
            f.write(",\n")  # Comma between rows
    f.write("\n]")  # End of JSON array
