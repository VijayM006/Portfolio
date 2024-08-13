
from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import socket

# Check if the SMTP server can be resolved to an IP address
try:
    print(f"SMTP Server IP: {socket.gethostbyname('smtp.gmail.com')}")
except socket.gaierror as e:
    print(f"Failed to resolve SMTP server: {e}")

vj = Flask(__name__, static_url_path='/static')
vj.secret_key = "maris2002"

# Flask-Mail configuration
vj.config['MAIL_SERVER'] = "smtp.gmail.com"
vj.config['MAIL_PORT'] = 587
vj.config['MAIL_USERNAME'] = "vijaymurugankkl@gmail.com"  # Hardcode for testing
vj.config['MAIL_PASSWORD'] = "qmsilztqjmwbpvpu"  # Hardcode for testing
vj.config['MAIL_USE_TLS'] = True
vj.config['MAIL_USE_SSL'] = False

mail = Mail(vj)

@vj.route("/")
def home():
    return render_template("index.html")

@vj.route('/send', methods=['POST'])
def send():
    # Fetch form data
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Ensure all fields are filled out
    if not all([name, email, subject, message]):
        return "Please fill out all fields", 400

    # Prepare the email
    msg = Message(subject=subject, sender=vj.config['MAIL_USERNAME'], recipients=['vijaymurugankkl@gmail.com'])
    msg.body = f"The sender name: {name}\nThe sender mail: {email}\nMessage: {message}"

    try:
        mail.send(msg)
        print("Mail sent successfully")
    except Exception as e:
        print(f"Failed to send mail: {e}")

    return redirect(url_for('home'))

if __name__ == "__main__":
    vj.run(debug=True, port=5987)