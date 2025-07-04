from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MongoDB Connection
# Replace the string below with your own MongoDB connection string
client = MongoClient("mongodb+srv://myuser:MyBDpass@cluster0.ro9pjcp.mongodb.net/github_events?retryWrites=true&w=majority&tls=true&tlsAllowInvalidCertificates=true")
db = client.github_events
collection = db.events

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    if event_type == "push":
        info = {
            "author": data['pusher']['name'],
            "to_branch": data['ref'].split('/')[-1],
            "event_type": "push",
            "timestamp": datetime.utcnow()
        }
    elif event_type == "pull_request":
        info = {
            "author": data['pull_request']['user']['login'],
            "from_branch": data['pull_request']['head']['ref'],
            "to_branch": data['pull_request']['base']['ref'],
            "event_type": "pull_request",
            "timestamp": datetime.utcnow()
        }
    else:
        return jsonify({"status": "ignored event"}), 200

    collection.insert_one(info)
    return jsonify({"status": "success"}), 200

@app.route('/events', methods=['GET'])
def get_events():
    events = collection.find().sort("timestamp", -1).limit(10)
    result = []

    for e in events:
        if e["event_type"] == "push":
            message = f'{e["author"]} pushed to {e["to_branch"]} on {e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")}'
        elif e["event_type"] == "pull_request":
            message = f'{e["author"]} submitted a pull request from {e["from_branch"]} to {e["to_branch"]} on {e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")}'
        else:
            continue
        result.append(message)

    return jsonify(result)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
