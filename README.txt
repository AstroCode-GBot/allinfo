
===========================================
FreeFire Player Info API - Flask Application
===========================================

# OWNER
# -----
# Owner: @agajayofficial ( Ajay )
# Telegram Bot: https://t.me/agajayofficial
# Telegram Group: https://t.me/AjayFFLikeGroup
# APIs Provided by: Killer Sharma (Aditya)

# THANKS TO
# ---------
# Special thanks to @KillerSharmaBot for providing these FreeFire APIs
# - Player Information API
# - Banner Image API
# - Outfit Image API
# - Ban Check API
# - Wishlist API
# - Token API
# - Access Token API

# REQUIREMENTS
# ------------
Python 3.7+
Flask
Pillow
Requests

# INSTALLATION
# ------------
pip install Flask Pillow Requests

# OR
pip install -r requirements.txt

# RUN APPLICATION
# ---------------
python app.py

# Server will start on: http://localhost:5000
# Debug mode: Enabled
# Port: 5000

# FREE FIRE UID INFORMATION
# -------------------------
# FreeFire UID can be 8 to 11 digits long
# Examples:
#   8-digit UID: 12345678
#   9-digit UID: 123456789
#   10-digit UID: 1234567890
#   11-digit UID: 12345678901
# 
# How UID detection works:
#   - If search_parameter.isdigit() returns True -> Treat as UID
#   - If contains non-digit characters -> Treat as Name
#   - UIDs must contain only numbers
#   - Names can contain letters, numbers, and special characters

# API ENDPOINTS
# -------------

# 1. GET PLAYER INFORMATION
#    /player-info?uid={uid}
#    /player-info?name={name}
#    /player-info?uid={uid}&name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    
#    Response Format:
#    {
#      "uid": "1234567890",
#      "name": "PlayerName",
#      "region": "IND",
#      "data": {
#        "basicInfo": {...},
#        "clanBasicInfo": {...},
#        "profileInfo": {...}
#      }
#    }

# 2. GET BANNER IMAGE
#    /banner-image?uid={uid}
#    /banner-image?name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    Returns: PNG Image
#    Parameters: headPic, bannerId, name, level, guild, pinId, celebrity, primeLevel, frame

# 3. GET OUTFIT IMAGE
#    /outfit-image?uid={uid}
#    /outfit-image?name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    Returns: PNG Image
#    Parameters: avatar_id, clothes (outfit + weapon skins)

# 4. GET BAN CHECK
#    /bancheck?uid={uid}
#    /bancheck?name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    
#    Response Format:
#    {
#      "accountId": "1234567890",
#      "name": "PlayerName",
#      "region": "IND",
#      "banStatus": {...}
#    }

# 5. GET WISHLIST
#    /wishlist?uid={uid}
#    /wishlist?name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    
#    Response Format:
#    {
#      "player": {
#        "uid": "1234567890",
#        "name": "PlayerName",
#        "region": "IND"
#      },
#      "wishlist": [...]
#    }

# 6. GET GUILD LEADER INFO
#    /leader-info?uid={uid}
#    /leader-info?name={name}
#    
#    Supports UID: 8-11 digits
#    Supports Name: Any text with special characters
#    
#    Response Format:
#    {
#      "basicInfo": {
#        "accountId": "9876543210",
#        "nickname": "LeaderName",
#        "region": "IND"
#      },
#      "clanBasicInfo": {...}
#    }

# UID VALIDATION RULES
# --------------------
# 1. Must be numeric only (0-9)
# 2. Length: 8 to 11 characters
# 3. No spaces or special characters
# 4. Example valid UIDs:
#    - 8-digit: 12345678
#    - 9-digit: 123456789
#    - 10-digit: 1234567890
#    - 11-digit: 12345678901
# 
# 5. Example invalid UIDs:
#    - 1234567 (7 digits - too short)
#    - 123456789012 (12 digits - too long)
#    - 12345abc (contains letters)
#    - 1234 5678 (contains space)

# NAME VALIDATION RULES
# ---------------------
# 1. Can contain letters (A-Z, a-z)
# 2. Can contain numbers (0-9)
# 3. Can contain special characters (-, _, ., space)
# 4. Case-sensitive in some cases
# 5. Example valid names:
#    - Killer-Test
#    - Player_123
#    - John Doe
#    - Pro.Player
#    - 123Player

# ERROR CODES
# -----------
# 200 - Success
# 400 - Missing uid or name parameter
# 404 - Player not found
# 500 - Internal server error

# TEST EXAMPLES
# -------------
# UID Examples (8-11 digits):
#   8-digit UID: 12345678
#   9-digit UID: 123456789
#   10-digit UID: 7669969208
#   11-digit UID: 12345678901
# 
# Name Examples:
#   Killer-Test
#   Player123
#   Pro_Gamer

# SAMPLE API REQUESTS
# -------------------

# Get player info by 8-digit UID
curl "http://localhost:5000/player-info?uid=12345678"

# Get player info by 9-digit UID
curl "http://localhost:5000/player-info?uid=123456789"

# Get player info by 10-digit UID
curl "http://localhost:5000/player-info?uid=7669969208"

# Get player info by 11-digit UID
curl "http://localhost:5000/player-info?uid=12345678901"

# Get player info by Name
curl "http://localhost:5000/player-info?name=Killer-Test"

# Download banner image by 10-digit UID
curl "http://localhost:5000/banner-image?uid=7669969208" --output banner.png

# Download banner image by Name
curl "http://localhost:5000/banner-image?name=Killer-Test" --output banner.png

# Download outfit image by UID
curl "http://localhost:5000/outfit-image?uid=7669969208" --output outfit.png

# Download outfit image by Name
curl "http://localhost:5000/outfit-image?name=Killer-Test" --output outfit.png

# Get ban check by UID
curl "http://localhost:5000/bancheck?uid=7669969208"

# Get ban check by Name
curl "http://localhost:5000/bancheck?name=Killer-Test"

# Get wishlist by UID
curl "http://localhost:5000/wishlist?uid=7669969208"

# Get wishlist by Name
curl "http://localhost:5000/wishlist?name=Killer-Test"

# Get guild leader info by UID
curl "http://localhost:5000/leader-info?uid=7669969208"

# Get guild leader info by Name
curl "http://localhost:5000/leader-info?name=Killer-Test"

# BROWSER URLs
# ------------

# http://localhost:5000/player-info?uid=7669969208
# http://localhost:5000/player-info?uid=12345678
# http://localhost:5000/player-info?uid=123456789
# http://localhost:5000/player-info?uid=12345678901
# http://localhost:5000/player-info?name=Killer-Test
# http://localhost:5000/banner-image?uid=7669969208
# http://localhost:5000/banner-image?name=Killer-Test
# http://localhost:5000/outfit-image?uid=7669969208
# http://localhost:5000/outfit-image?name=Killer-Test
# http://localhost:5000/bancheck?uid=7669969208
# http://localhost:5000/bancheck?name=Killer-Test
# http://localhost:5000/wishlist?uid=7669969208
# http://localhost:5000/wishlist?name=Killer-Test
# http://localhost:5000/leader-info?uid=7669969208
# http://localhost:5000/leader-info?name=Killer-Test

# PYTHON CODE EXAMPLE
# -------------------

import requests

# Test with different UID lengths
uids = ["12345678", "123456789", "7669969208", "12345678901"]
name = "Killer-Test"

for uid in uids:
    # Get player info
    response = requests.get(f"http://localhost:5000/player-info?uid={uid}")
    if response.status_code == 200:
        player_data = response.json()
        print(f"UID: {player_data['uid']}")
        print(f"Name: {player_data['name']}")
        print(f"Region: {player_data['region']}")
    else:
        print(f"Player not found for UID: {uid}")

# Get player info by Name
response = requests.get(f"http://localhost:5000/player-info?name={name}")
if response.status_code == 200:
    player_data = response.json()
    print(f"Found player: {player_data['name']} with UID: {player_data['uid']}")

# Download banner image by UID
uid = "7669969208"
response = requests.get(f"http://localhost:5000/banner-image?uid={uid}")
if response.status_code == 200:
    with open(f"banner_{uid}.png", "wb") as f:
        f.write(response.content)
    print(f"Banner image saved for UID: {uid}")

# Download outfit image by Name
response = requests.get(f"http://localhost:5000/outfit-image?name={name}")
if response.status_code == 200:
    with open(f"outfit_{name}.png", "wb") as f:
        f.write(response.content)
    print(f"Outfit image saved for Name: {name}")

# Get ban check
response = requests.get(f"http://localhost:5000/bancheck?uid={uid}")
if response.status_code == 200:
    ban_data = response.json()
    print(f"Ban Status: {ban_data}")

# Get wishlist
response = requests.get(f"http://localhost:5000/wishlist?uid={uid}")
if response.status_code == 200:
    wishlist_data = response.json()
    print(f"Wishlist Data: {wishlist_data}")

# Get leader info
response = requests.get(f"http://localhost:5000/leader-info?uid={uid}")
if response.status_code == 200:
    leader_data = response.json()
    print(f"Leader Data: {leader_data}")

# HOW UID vs NAME DETECTION WORKS
# -------------------------------
# 
# def fetch_player_data_by_uid_or_name(search_parameter):
#     if search_parameter.isdigit():
#         # Treat as UID (8-11 digits)
#         url = f"https://info.killersharmabot.online/player-info?uid={search_parameter}"
#     else:
#         # Treat as Name (contains non-digit characters)
#         url = f"https://info.killersharmabot.online/player-info?name={search_parameter}"
# 
# When both uid and name parameters are provided:
#     if uid and name:
#         search_param = uid if uid.isdigit() else name
# 
# This ensures:
# - If uid parameter contains only digits -> Use as UID
# - If uid parameter contains letters -> Fallback to name parameter
# - If only name parameter provided -> Use as Name

# EXPECTED OUTPUT
# ---------------
# Player should exist in FreeFire database
# UID: Must be 8-11 digits
# Example UID 7669969208 is 10 digits (valid)
# Name: Killer-Test contains hyphen (valid)
# Region will be auto-detected (IND, BGD, etc.)
# Banner and outfit images will be generated based on player's equipped items

# NOTES FOR DIFFERENT UID LENGTHS
# -------------------------------
# 8-digit UID: Older FreeFire accounts
# 9-digit UID: Common for mid-age accounts
# 10-digit UID: Most common for current accounts
# 11-digit UID: Newer accounts or specific regions
# 
# All UID lengths work exactly the same way with the API
# The API automatically handles different UID lengths

# API PROVIDER NOTES
# ------------------
# All APIs are provided by @KillerSharmaBot (Aditya)
# For support or issues: https://t.me/KillerSharmaBot
# Join Telegram group: https://t.me/adityalikegroup
# APIs used:
#   - https://info.killersharmabot.online (Player Info, Bancheck, Wishlist)
#   - https://image.killersharmabot.online (Banner, Outfit Images)
#   - https://token.killersharmabot.online (Token Generation)
#   - https://access.killersharmabot.online (Access Token)

# TROUBLESHOOTING
# ---------------
# 1. Port already in use: Change port in app.run(port=5001)
# 2. Module not found: Run pip install Flask Pillow Requests
# 3. Connection error: Check internet connection
# 4. Player not found (404): Verify UID is 8-11 digits and correct
# 5. API not responding: Contact @KillerSharmaBot for support
# 6. Image not generated: Check if player has equipped items

# If player not found (404):
#   - Verify UID length is between 8-11 digits
#   - Verify UID contains only numbers
#   - Verify Name spelling (case sensitive)
#   - Check if player exists in FreeFire
#   - Try using only UID or only Name

# If image not generated:
#   - Check if player has equipped outfits
#   - Check if player has weapon skins
#   - Default avatar (102000007) will be used if no character equipped

# CREDITS
# -------
# Developed using Aditya FF Apis
# API Owner: @KillerSharmaBot
# Special thanks for providing FreeFire API services