import os
import requests
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

DISCORD_API_ENDPOINT = "https://discord.com/api/v10"
GUILD_ID = "1183784452674039919"
BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

@app.route('/api/verify', methods=['POST'])
def verify_discord_role():
    app.logger.info("Received request: %s", request.json)
    discord_id = request.json.get('discord', '').strip()
    role_id = request.json.get('role_id', '').strip()
    
    if not discord_id or not role_id:
        app.logger.error("Discord ID or Role ID not provided")
        return jsonify({
            "error": {
                "code": 0,
                "message": "Discord ID and Role ID are required"
            },
            "data": {
                "result": False
            }
        }), 200
    
    try:
        app.logger.info("Fetching member data for Discord ID: %s", discord_id)
        member_data = get_discord_member(discord_id)
    except requests.RequestException as e:
        app.logger.error("Failed to fetch member data: %s", str(e))
        return jsonify({
            "error": {
                "code": 0,
                "message": f"Failed to fetch member data: {str(e)}"
            },
            "data": {
                "result": False
            }
        }), 200
    
    user_roles = member_data.get('roles', [])
    has_role = role_id in user_roles
    
    app.logger.info("Verification complete. Has role: %s", has_role)
    return jsonify({
        "error": {
            "code": 0,
            "message": ""
        },
        "data": {
            "result": has_role
        }
    }), 200

def get_discord_member(user_id: str):
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
    }
    url = f"{DISCORD_API_ENDPOINT}/guilds/{GUILD_ID}/members/{user_id}"
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

@app.route('/')
def home():
    return "Discord Role Verification API is running!"

app = app
