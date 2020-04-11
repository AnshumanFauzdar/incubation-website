from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from add_to_csv import add_to_csv

# Ini app
app = Flask(__name__)
app.config['SECRET_KEY'] = '2ece243aa5bfad295dca55d8b38cdbcd'
app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# create db model
db = SQLAlchemy(app)

# create db class
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.Text())
    message = db.Column(db.Text())

    def __init__(self, name, email, phone, message):
        self.name = name
        self.email = email
        self.phone = phone
        self.message = message


# route to index.html at / with loader animation home.html template
@app.route('/')
def index():
    return render_template('home_loader.html')

# route to home.html
@app.route('/home')
def home():
    return render_template('home.html')

# route to about.html at /about
@app.route('/about')
def about():
    return render_template('about.html')

# route
@app.route('/board')
def board():
    return render_template('board.html')

# route
@app.route('/mentors')
def mentors():
    return render_template('mentors.html')

# route
@app.route('/advisors')
def advisors():
    return render_template('advisors.html')

# route
@app.route('/events')
def events():
    return render_template('events.html')

# route
@app.route('/incubates')
def incubates():
    return render_template('incubates.html')

# route
@app.route('/career')
def career():
    return render_template('career.html')

# route
@app.route('/apply')
def apply():
    return render_template('apply.html')

# route to contact-us.html
@app.route('/contact-us', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    # make sure POST request
    if request.method == 'POST':
        if form.validate_on_submit():
            # get data from form
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            message = request.form['message']

            data = Feedback(name, email, phone, message)
            db.session.add(data)
            db.session.commit()

            add_to_csv(name, email, phone, message)
            
            send_mail(name, email, phone, message)

            return render_template('notify.html', message='Thank you for your feedback.\
                                        We will get in touch with you soon!\
                                        <br><br><a href="/home" style="color:#000066">\
                                        <i class="fa fa-home fa-fw" aria-hidden="true"></i>\
                                        <u>Back to home page</u></a>')

    # GET method render contact-us.html
    return render_template('contact-us.html', form=form)



# HTTP ERROR HANDLERS -

# 404 Page not found error
@app.errorhandler(404)
def page_not_found(error):
    return render_template('notify.html', message='<h1>Oops! Page Not Found (404)</h1>\
    <br><a href="/home" style="color:#000066">\
    <i class="fa fa-home fa-fw" aria-hidden="true"></i>\
    <u>Go to home page</u></a>,\
    or reach us at <a href="mailto:diif.dite@gmail.com?subject=DITE_IIF_Inquiry" style="color:#000066">\
    <i class="fa fa-envelope"></i> diif.dite@gmail.com</a>'), 404

# 403 Forbidden error
@app.errorhandler(403)
def error_403(error):
    return render_template('notify.html', message='<h1>You do not have permission to access that (403)</h1>\
    <br> reach us at <a href="mailto:diif.dite@gmail.com?subject=DITE_IIF_Inquiry" style="color:#000066">\
    <i class="fa fa-envelope"></i> diif.dite@gmail.com</a>'), 403

# 500 Internal Server error
@app.errorhandler(500)
def error_500(error):
    app.logger.error(f"Server error: {error}, route: {request.url}")
    return render_template('notify.html', message='<h1>Something went wrong (500)</h1>\
    <br><p>We are experiencing some trouble on our end. Please try again in the near future,\
    or reach us at \
    <a href="mailto:diif.dite@gmail.com?subject=DITE_IIF_Inquiry_Server_Error" style="color:#000066">\
    <i class="fa fa-envelope"></i> \
    diif.dite@gmail.com</a>'), 500

if __name__ == '__main__':
    app.run()
