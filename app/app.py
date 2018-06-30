from flask import Flask, render_template, flash, request
from lib.graffiti import generate_graffiti_address
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '3287642837'


class ReusableForm(Form):
    string = TextField(
        'Graffiti (20 characters max):', validators=[validators.required()])


@app.route('/', methods=['GET', 'POST'])
@app.route('/<tag>', methods=['GET', 'POST'])
def index(tag=None):
    if tag != None:
        return generate_graffiti_address(tag)
    form = ReusableForm(request.form)
    if request.method == 'POST':
        tag = request.form['string']
        if form.validate():
            # Save the comment here.
            flash('Write graffiti "' + tag +
                  '" to blockchain by sending (at least) 5460 haks to:')
            flash('')
            flash(generate_graffiti_address(tag))
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()
