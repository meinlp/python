from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import os

SECRET_KEY = os.urandom(32)
print(f'SECRET_KEY = {SECRET_KEY}')
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = SECRET_KEY


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
    # return '<h1>Bad Request</h1>', 400


if __name__ == '__main__':
    app.run(debug=True)
