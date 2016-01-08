import os
import stripe

from flask import Flask, flash, request, render_template, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, validators

# CONFIG
DEBUG = True
# Don't forget to set key!!!
SECRET_KEY = os.environ['FLASK_SECRET_KEY']
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY']
}

# CREATE APP
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
stripe.api_key = stripe_keys['secret_key']


# FORMS
class EmailForm(Form):
    name = StringField('Name')
    email = StringField('Email Address')
    message = TextAreaField('Message')


@app.route('/', methods=['GET', 'POST'])
def get_index():
    form = EmailForm()
    if request.method == 'POST' and form.validate():
        flash('Thanks, email sent')
        print('name: ', form.name.data)
        print('email: ', form.email.data)
        print('message: ', form.message.data)

        return render_template('index.html',
                               form=form,
                               title='RoxyChow')
    return render_template('index.html',
                           form=form,
                           title='RoxyChow',
                           key=stripe_keys['publishable_key'])
