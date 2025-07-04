# webhook-repo

This is a Flask-based backend application that receives GitHub webhook events (like push and pull requests) and stores them in MongoDB. It also includes a frontend UI to display these events in real time.

---

## Features

- Receives GitHub webhooks on `/webhook`
- Parses push and pull request events
- Stores event details in **MongoDB Atlas**
- Provides a clean UI (`/`) that shows recent activity
- Automatically refreshes the event list every **15 seconds**

---

## Tech Stack

- Backend: Python, Flask
- Database: MongoDB Atlas (cloud)
- Frontend: HTML, JavaScript
- Other Tools: GitHub Webhooks, ngrok

---

##  Project Structure
webhook-repo/
     -app.py # Flask server with webhook & UI routes
     -templates/
               index.html # UI that shows latest GitHub events
     -venv/ # Virtual environment (not pushed)
     -requirements.txt # Project dependencies
     

##  How to Run the App Locally

### Step 1: Clone the Repository
```bash
git clone https://github.com/Himanshu-Rathod/webhook-repo.git
cd webhook-repo

### Step 2: Setup Environment
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate for Linux/Mac
pip install -r requirements.txt

### Step 3: Run the Server
python app.py

### Step 4: Expose to Internet using ngrok
ngrok http 5000

##  Webhook Event Flow

Push code to action-repo
GitHub sends a webhook to webhook-repo server
Flask parses the event and stores it in MongoDB
UI fetches and displays the data

