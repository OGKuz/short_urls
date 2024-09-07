from app.models import Link, db
from . import app
from flask import render_template, redirect

from app.forms import NewShortUrl

from random import choice
from string import ascii_letters

LETTERS = ascii_letters + '0123456789'

@app.route('/', methods = ["GET", "POST"])
def index():
    form = NewShortUrl()
    if form.validate_on_submit():
        new_link = Link()
        new_link.long_url = form.long_url.data
        short_url = ''.join( [choice(LETTERS) for i in range(6)] )
        print (short_url)
        new_link.short_url = short_url
        db.session.add(new_link)
        db.session.commit()
        return render_template('index.html', form = form, short_url = short_url)
    return render_template('index.html', form = form)

@app.route('/urls')
def urls_view():
    context = Link.query.all()
    return render_template ('urls.html', context=context)

@app.route('/<link>')
def redirect_to_link(link):
    link = Link.query.filter(Link.short_url == link).first()
    if link:
        link.count_view += 1
        db.session.add(link)
        db.session.commit()
        return redirect(link.long_url)