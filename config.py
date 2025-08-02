import os
from pyrogram import Client 
# <-- Add this import at the top

# Environment variables with fallback values
API_ID = os.getenv("API_ID", "20081897")
API_HASH = os.getenv("API_HASH", "8051dfd6c39c07e3eb56d58ef7f9f15f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8437726474:AAE6-hpZIu_D3KuuwcTW0q4cmLKEbnwj-Bg")
AUTH_USERS = os.getenv("AUTH_USERS", "7292006343")

# Convert auth_users to list of integers
try:
    auth_users = [int(user_id.strip()) for user_id in AUTH_USERS.split(",") if user_id.strip()]
except (AttributeError, ValueError):
    auth_users = []

# Initialize bot (optional - better to do this in app.py)
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
