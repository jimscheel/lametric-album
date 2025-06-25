
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/lametric")
def lametric():
    slug = request.args.get("slug") or request.headers.get("slug")
    if not slug:
        return jsonify({
            "frames": [{
                "icon": "i5555",
                "text": "Missing slug"
            }]
        })

    api_url = f"https://1001albumsgenerator.com/api/v1/projects/{slug}"
    headers = {"x-api-access": "2hahnhmaanawnf5ahualksqkwFacbCCBekdazcKnAoVaJaasuae8AkdlAa30dpeb"}

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        album = data["currentAlbum"]["album"]
        album_name = album["name"]
        artist = album["artist"]
        total_albums = data["totalAlbums"]
        current_index = data["revealedAlbumsCount"]
        progress_text = "FINISHED" if current_index >= total_albums else f"Album {current_index+1} af {total_albums}"

        return jsonify({
            "frames": [
                {
                    "icon": "i1186",
                    "text": f"{album_name} – {artist}"
                },
                {
                    "icon": "i2376",
                    "text": progress_text
                }
            ]
        })
    except Exception as e:
        return jsonify({
            "frames": [{
                "icon": "i5555",
                "text": "Error fetching album"
            }]
        })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
