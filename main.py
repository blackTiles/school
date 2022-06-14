
import os
from flask import Flask, render_template, jsonify, request
from auth import auth

app = Flask(__name__)

staticFolder = os.path.join('static')
app.config['UPLOAD_FOLDER'] = staticFolder
static = app.config['UPLOAD_FOLDER']

@app.route('/', methods=['GET','POST'])
def Homepage():
    return render_template('index.html', static = static)

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/news_and_events')
def news_and_events():
    return render_template('news.html', static=static)

@app.route('/school_fees')
def school_fees():
    return render_template('fees.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', static=static)

@app.route('/history')
def history():
    return render_template('history.html',static = static)

@app.route('/academics')
def academics():
    return render_template('academics.html',static = static)

@app.route('/about_us')
def about_us():
    return render_template('about-us.html',static = static)

@app.route('/facilities')
def facilities():
    return render_template('facilities.html',static = static)

@app.route('/contact')
def contact():
    return render_template('contact.html',static = static)

@app.route('/admission')
def admission():
    return render_template('admission.html')

@app.route('/login')
def login_page():
    return render_template('index-login.html')

@app.route('/register')
def sign_up_page():
    return render_template('index-signup.html')

@app.route('/register_parent', methods=['POST','GET'])
def register():
    # if request.method == 'POST':
        # userEmail = request.form['form_email']
        # userPassword = request.form['form_password']
    userEmail="satyamraj466@gmail.com"
    userPassword="satyamraj"
    user = auth.create_user_with_email_and_password(userEmail, userPassword)
    print(user)

if __name__ == '__main__':
    app.run(debug=True)
