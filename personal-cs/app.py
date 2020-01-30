from databases import *
from flask import *
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index-login.html', methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template("index-login.html")
    user = get_user(request.form['username'])
    if user != None and user.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        print("Logged in")
        return redirect(url_for("page"))
    else:
        return redirect(url_for("home"))


@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template("index-signup.html")
    user = get_user(request.form['username'])
    if user == None:
        print("new user added.")
        add_user(request.form['username'],request.form['password'])
    return home()


@app.route('/logged-in')
def logged_in():
    return render_template('logged.html')


@app.route('/logout')
def logout():
    login_session['logged_in'] = False
    return home()

@app.route('/page')
def page():
    return render_template('page.html')

@app.route('/malak')
def malak():
    return render_template('malak.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/lifestyle')
def lifestyle():
    return render_template('lifestyle.html')


if __name__ == '__main__':
    app.run(debug=True)
