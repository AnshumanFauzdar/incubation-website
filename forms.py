from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('name',
                        validators=[InputRequired(), Length(min=2, max=20)], 
                        render_kw={"placeholder": "Your name *"})
    email = StringField('Email',
                        validators=[InputRequired(), Email()], render_kw={"placeholder": "Your Email *"})
    phone = StringField('Phone_no',
                        validators=[InputRequired(), Length(min=10, max=10, message="Please enter a valid 10 digit phone number")], 
                        render_kw={"placeholder": "Your Phone Number *", "type": "number"})
    message = TextAreaField('Message',
                        validators=[InputRequired()], 
                        render_kw={"placeholder": "Your Message *", "style":"width: 100%; height: 150px;"})
    submit = SubmitField('submit')