import os

# Correct way to load environment variables (using proper names)
API_ID = os.getenv("API_ID", "20081897")  # Fallback to your value if env var not set
API_HASH = os.getenv("API_HASH", "8051dfd6c39c07e3eb56d58ef7f9f15f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8437726474:AAE6-hpZIu_D3KuuwcTW0q4cmLKEbnwj-Bg")
AUTH_USERS = os.getenv("AUTH_USERS", "7292006343")  # Single user by default

# Convert auth_users to list of integers safely
try:
    auth_users = [int(user_id.strip()) for user_id in AUTH_USERS.split(",") if user_id.strip()]
except (AttributeError, ValueError):
    auth_users = []

# Initialize the bot
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Verification print (remove in production)
print("Configuration loaded successfully!")
print(f"API_ID: {API_ID}")
print(f"AUTH_USERS: {auth_users}")
