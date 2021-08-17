from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import os
from  dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def send_msg():
    if request.method == "POST":
        email = request.form['email']
        subject = request.form['subject']
        msg = request.form['message']

        message = Message(subject,sender=os.getenv('MAIL_USERNAME'),recipients=[os.getenv('MAIL_USERNAME')])
        message.body = f""" From: {email} <Subject:{subject}> \n{msg} """ 
        mail.send(message)

        # success = "Your message has been sent"
        return redirect('/')





if __name__ == '__main__':
    app.run(debug=False)