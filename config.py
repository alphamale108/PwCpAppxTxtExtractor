import os

# Fetch environment variables
api_id = os.getenv("20081897")
api_hash = os.getenv("8051dfd6c39c07e3eb56d58ef7f9f15f")
bot_token = os.getenv("8437726474:AAE6-hpZIu_D3KuuwcTW0q4cmLKEbnwj-Bg")
auth_users = os.getenv("7292006343").split(",")  # Split comma-separated IDs into a list

# Validate environment variables
if not all([api_id, api_hash, bot_token]):
    raise ValueError("Missing required environment variables: API_ID, API_HASH, or BOT_TOKEN")

# Convert auth_users to a list of integers
auth_users = [int(user_id) for user_id in auth_users if user_id]
