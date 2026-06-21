import requests
from io import BytesIO
from typing import Optional, Tuple, Dict, Any
from flask import Flask, send_file, jsonify, request

app = Flask(__name__)

def safe_get_url(url: str) -> requests.Response: response = requests.get(url); response.raise_for_status(); return response

def fetch_player_data_by_uid_or_name(search_parameter: str) -> Optional[Tuple]:
    url = f"https://info.killersharmabot.online/player-info?uid={search_parameter}" if search_parameter.isdigit() else f"https://info.killersharmabot.online/player-info?name={search_parameter}"
    response = requests.get(url)
    if response.status_code != 200: return None
    data = response.json()
    basic_info = data.get("basicInfo")
    if not basic_info: return None
    return (basic_info.get("accountId"), basic_info.get("nickname"), basic_info.get("region", "Not Choosen"), data)

def fetch_banner_image(player_data: Dict[str, Any]) -> bytes:
    basic_information = player_data.get("basicInfo", {})
    clan_information = player_data.get("clanBasicInfo", {})
    prime_level = basic_information.get("primeLevel", {}).get("level", 0)
    frame = "true" if prime_level == 8 else "false"
    nickname = basic_information.get("nickname", "").replace('#', '%23').replace('&', '%26')
    clan_name = clan_information.get("clanName", "").replace('#', '%23').replace('&', '%26')
    url = f"https://image.killersharmabot.online/banner-image?headPic={basic_information.get('headPic','')}&bannerId={basic_information.get('bannerId','')}&name={nickname}&level={basic_information.get('level',2)}&guild={clan_name}&pinId={basic_information.get('pinId','900000012')}&celebrity={basic_information.get('celebrityStatus',0)}&primeLevel={prime_level}&frame={frame}"
    response = safe_get_url(url)
    return response.content

def fetch_outfit_image(player_data: Dict[str, Any]) -> bytes:
    basic_information = player_data.get("basicInfo", {})
    profile_information = player_data.get("profileInfo", {})
    equipped_weapons = basic_information.get("weaponSkinShows", [])
    equipped_outfits = profile_information.get("clothes", [])
    character_id = profile_information.get("avatarId", "102000007")
    outfit_ids = ",".join(str(item) for item in (equipped_outfits + equipped_weapons)) if (equipped_outfits or equipped_weapons) else ""
    url = f"https://image.killersharmabot.online/outfit-image?avatar_id={character_id}&clothes={outfit_ids}"
    response = safe_get_url(url)
    return response.content

@app.route('/player-info', methods=['GET'])
def get_player_info():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    result = fetch_player_data_by_uid_or_name(search_param)
    if not result: return jsonify({"error": "Player not found"}), 404
    account_id, nickname, region, data = result
    return jsonify({"uid": account_id, "name": nickname, "region": region, "data": data})

@app.route('/banner-image', methods=['GET'])
def get_banner_image():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    result = fetch_player_data_by_uid_or_name(search_param)
    if not result: return jsonify({"error": "Player not found"}), 404
    _, _, _, player_data = result
    banner_bytes = fetch_banner_image(player_data)
    return send_file(BytesIO(banner_bytes), mimetype='image/png')

@app.route('/outfit-image', methods=['GET'])
def get_outfit_image():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    result = fetch_player_data_by_uid_or_name(search_param)
    if not result: return jsonify({"error": "Player not found"}), 404
    _, _, _, player_data = result
    outfit_bytes = fetch_outfit_image(player_data)
    return send_file(BytesIO(outfit_bytes), mimetype='image/png')

@app.route('/bancheck', methods=['GET'])
def get_bancheck():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    url = f"https://info.killersharmabot.online/bancheck?uid={search_param}" if search_param.isdigit() else f"https://info.killersharmabot.online/bancheck?name={search_param}"
    response = requests.get(url)
    if response.status_code != 200: return jsonify({"error": "Player not found"}), 404
    data = response.json()
    return jsonify(data)

@app.route('/wishlist', methods=['GET'])
def get_wishlist():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    url = f"https://info.killersharmabot.online/wishlist?uid={search_param}" if search_param.isdigit() else f"https://info.killersharmabot.online/wishlist?name={search_param}"
    response = requests.get(url)
    if response.status_code != 200: return jsonify({"error": "Player not found"}), 404
    data = response.json()
    return jsonify(data)

@app.route('/leader-info', methods=['GET'])
def get_leader_info():
    uid = request.args.get('uid')
    name = request.args.get('name')
    search_param = uid if uid else name
    if not search_param: return jsonify({"error": "Missing uid or name parameter"}), 400
    result = fetch_player_data_by_uid_or_name(search_param)
    if result is None: return jsonify({"error": "Player not found"}), 404
    account_id, player_name, region, data = result
    captain_information = data.get("captainBasicInfo", {})
    if not captain_information.get("accountId"): return jsonify({"error": "Leader not found"}), 404
    leader_uid = captain_information.get("accountId")
    url = f"https://info.killersharmabot.online/player-info?uid={leader_uid}"
    response = requests.get(url)
    if response.status_code != 200: return jsonify({"error": "Leader data not found"}), 404
    leader_data = response.json()
    return jsonify(leader_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)