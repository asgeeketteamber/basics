from flask import Flask
from flask import request
from markupsafe import escape
from flask import url_for

app = Flask(__name__)
@app.route('/helloworld')
def hello_world():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"
@app.route('/')
def index():
    return 'Index '

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def show_user_profile(username):
    return f'{username}\'s profile'
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login' , next='/'))
    print(url_for('show_user_profile', username='john doe'))

# @app.route('/login', methods=['GET,POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
#     @app.route('/logout')
#     def logout():
#         return 'logout'
@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f=request.files['the_file']
        f.save(f.helloworld1.jpg)
        return 'file uploaded successfully'
        return upload_form()
     