from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
import os

# PASSWORD = os.environ['pass']
# MY_EMAIL = os.environ['mejl']

PASSWORD = os.getenv('LOZINKA')
MY_EMAIL = os.getenv('MEJL')


app = Flask(__name__)
connection = smtplib.SMTP('smtp.gmail.com',port=587)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form-entry',methods=['GET','POST'])
def recieve_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["message"])
    if request.method == 'POST':
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f'Subject:Nova poruka sa sajta!\n\nOd: {data["email"]}\nIme:{data["name"]}\nPoruka:{data["message"]}')
        connection.close()
        # return "<h1>Successfully sent your message</h1>"
        # flash('Your message was successfully sent!')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()