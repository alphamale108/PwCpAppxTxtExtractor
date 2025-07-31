import os

# Fetch environment variables
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
auth_users = os.getenv("AUTH_USERS", "").split(",")  # Split comma-separated IDs into a list

# Validate environment variables
if not all([api_id, api_hash, bot_token]):
    raise ValueError("Missing required environment variables: API_ID, API_HASH, or BOT_TOKEN")

# Convert auth_users to a list of integers
auth_users = [int(user_id) for user_id in auth_users if user_id]
