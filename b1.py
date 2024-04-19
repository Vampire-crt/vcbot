import json
import requests
import os
import sys
from pyrogram import Client, filters

BOT_TOKEN = '6992476835:AAFSpMcyobLhE3dPBlJpN5d3Lt-Yt2XZDtc'
API_ID = '11740987'
API_HASH = 'e94b99e12ae7861e45042813021237ce'

# Create a Pyrogram Client
app = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def send_started_req(client, username_info):
    ut = f"https://t.me/{username_info}"
    url = "https://d45d-2a02-c7c-52c5-a600-30ea-6799-df0f-5716.ngrok-free.app/telegram/voicechat"
    json_data = {"text": ut, "status": "Active"}
    api_key = 'YOUR_API_KEY'
    headers = {"X-VC-API-KEY": api_key, "Accept": "application/json"}
    response = requests.post(url, json=json_data, headers=headers)
    if response.status_code == 200:
        print("POST request for vc start successful!")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")

async def send_end_req(client, username_info):
    ut = f"https://t.me/{username_info}"
    url = "https://d45d-2a02-c7c-52c5-a600-30ea-6799-df0f-5716.ngrok-free.app/telegram/voicechat"
    json_data = {"text": ut, "status": "Inactive"}
    api_key = 'YOUR_API_KEY'
    headers = {"X-VC-API-KEY": api_key, "Accept": "application/json"}
    response = requests.post(url, json=json_data, headers=headers)
    if response.status_code == 200:
        print("POST request for vc end successful!")
        print(response.json())
    else:
        print(f"Error: {response.status_code} - {response.text}")


# Function to handle video chat start event
@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message):
    username_info = message.chat.username
    print(f"Video Chat Started {message.chat.id}, {username_info}")
    await send_started_req(client, username_info)

# Function to handle video chat end event
@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message):
    username_info = message.chat.username
    print(f"Video Chat closed {message.chat.id}, {username_info}")
    await send_end_req(client, username_info)

# Function to handle start command
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Great news! I am now active, and working in the background")


print('Start the bot')
app.run()
