
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_BASE_URL = "https://1001albumsgenerator.com/api/v1/projects/"
API_TOKEN = "2hahnhmaanawnf5ahualksqkwFacbCCBekdazcKnAoVaJaasuae8AkdlAa30dpeb"

@app.route("/lametric", methods=["GET"])
def lametric():
    slug = request.headers.get("slug")
    if not slug:
        return jsonify({"frames": [{"icon": "i2309", "text": "No slug provided"}]}), 400

    api_url = f"{API_BASE_URL}{slug}"
    headers = {"x-api-access": API_TOKEN}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        album_data = data.get("currentAlbum")
        history_data = data.get("history", [])
        current_album_name = album_data.get("name", "Unknown Album")
        artist_name = album_data.get("artist", "Unknown Artist")
        total_revealed = sum(1 for entry in history_data if entry.get("revealedAlbum"))
        progress_text = f"Album {total_revealed + 1} af 1001" if total_revealed < 1001 else "FINISHED"

        return jsonify({
            "frames": [
                {"icon": "i1186", "text": f"{current_album_name} – {artist_name}"},
                {"icon": "i2376", "text": progress_text}
            ]
        })
    except Exception as e:
        return jsonify({
            "frames": [
                {"icon": "i2309", "text": "Fejl"},
                {"icon": "i2309", "text": str(e)}
            ]
        })

if __name__ == "__main__":
    app.run(debug=True)
