from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

app = Flask(__name__)

# 🔐 Replace with your Gmail
YOUR_EMAIL = "neophukubye2001@gmail.com"
APP_PASSWORD = "kabelophukubye"

def send_email(answer):
    msg = MIMEText(
        f"Valentine Response 💕\n\n"
        f"He answered: {answer}\n"
        f"Time: {datetime.now()}"
    )

    msg["Subject"] = "He answered your Valentine Question 💖"
    msg["From"] = YOUR_EMAIL
    msg["To"] = YOUR_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(YOUR_EMAIL, APP_PASSWORD)
        server.send_message(msg)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def answer():
    data = request.json
    user_answer = data["answer"]

    # Save locally
    with open("responses.txt", "a") as f:
        f.write(f"{user_answer} - {datetime.now()}\n")

    # Send email
    send_email(user_answer)

    return jsonify({"status": "success"})

if __name__ == "__main__":
    app.run(debug=True)
