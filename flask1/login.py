from __init__ import *
from database import *

app = Flask(__name__) 
app.secret_key='b_5#y2L"F4Q8z\n\xec]/'
@app.route('/')
def Home():
    'This method will display Home page with login form'
    return render_template('login.html')

@app.route('/index')
def index():
    'while logging in it creates the session'

    if 'email' in session:
        return render_template('logsuc.html') + session['email']

@app.route('/login')
def log():

    'while clicking the login link this method will redirect to the home page'

    return redirect(url_for('Home'))


@app.route('/success',methods = ['POST'])
def login():


    app.logger.debug('A value for debugging')
    'It will check for the existing user if none redirect to the login page or it will redirect to the login'

    if request.method == 'POST':
        session['email'] = request.form['email']
        session['pass'] = request.form['pass']
        login_user = users.find_one({'email' : request.form['email'],
                                      'password': request.form['pass']  })

        if login_user is None:
            return render_template('register.html')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():

    'This method  will logout and redirect to the login page'

    return redirect(url_for('Home'))

@app.route('/signup')
def signup():

    'This method will render the html  registration page when the signup option is clicked'

    return render_template('register.html')


@app.route('/successful',methods = ['POST'])
def regsuc():

    "it will compare the existing user details in the database and if match it will say existing user or it will add the details to d    atbase and redirect to the homwe page to login"


    if request.method == 'POST':

        existing_user = users.find_one( { 'email' : request.form['email'],
                                          'password': request.form['pass'],
                                          'contact': request.form['contact'] } )



        if existing_user is None:

            users.insert_one( { 'email' : request.form['email'],
                                'password': request.form['pass'] ,
                                'contact': request.form['contact'] })
                
            return redirect(url_for('Home')) 
        return 'already registered'
             
                  





