from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_TOKEN = "2hahnhmaanawnf5ahualksqkwFacbCCBekdazcKnAoVaJaasuae8AkdlAa30dpeb"
API_BASE_URL = "https://1001albumsgenerator.com/api/v1/projects/"

@app.route("/lametric", methods=["GET"])
def lametric_data():
    slug = request.args.get("slug")
    if not slug:
        return jsonify({"frames": [{"text": "Missing slug", "icon": "i2309"}]})

    try:
        response = requests.get(
            f"{API_BASE_URL}{slug}",
            headers={"x-api-access": API_TOKEN}
        )
        if response.status_code != 200:
            return jsonify({"frames": [{"text": "API error", "icon": "i2309"}]})

        data = response.json()

        if "currentAlbum" not in data or data["currentAlbum"] is None:
            return jsonify({"frames": [{"text": "Ingen album tildelt endnu", "icon": "i2309"}]})

        album = data["currentAlbum"].get("name", "Ukendt album")
        artist = data["currentAlbum"].get("artist", "Ukendt kunstner")
        history_length = len(data.get("history", []))
        current_album_number = history_length + 1
        total_albums = 1001

        if current_album_number > total_albums:
            progress_text = "FINISHED"
        else:
            progress_text = f"Album {current_album_number} af {total_albums}"

        return jsonify({
            "frames": [
                {
                    "text": f"{album} – {artist}",
                    "icon": "i1186"
                },
                {
                    "text": progress_text,
                    "icon": "i2376"
                }
            ]
        })

    except Exception as e:
        import traceback
        return jsonify({
            "frames": [
                {
                    "text": f"Fejl: {str(e)}",
                    "icon": "i2309"
                },
                {
                    "text": traceback.format_exc().splitlines()[-1],
                    "icon": "i2309"
                }
            ]
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
