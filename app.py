from flask import Flask, request, jsonify
from utils.emoji_map import emoji_map

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        emojis = request.json.get('emojis', [])
        story = ' '.join(emoji_map.get(e, "unknown emoji") for e in emojis)
        return jsonify({"story": story})
    return "Welcome to Emoji-to-Story Generator!"

if __name__ == '__main__':
    app.run(debug=True)
