from flask import render_template, request, sessions, g, abort, redirect, url_for, flash
from app import app, babel
from .send_mail import question_mail
from config import SUPPORTED_LANGUAGES, BABEL_DEFAULT_LOCALE
from flask_babel import gettext


@app.before_request
def before():
    if request.view_args and 'lang_code' in request.view_args:
        if request.view_args['lang_code'] not in SUPPORTED_LANGUAGES.keys():
            return abort(404)
        g.current_lang = request.view_args['lang_code']
        request.view_args.pop('lang_code')


@babel.localeselector
def get_locale():
    return g.get('current_lang', BABEL_DEFAULT_LOCALE)


@app.route('/')
def root():
    return redirect(url_for('index', lang_code=BABEL_DEFAULT_LOCALE))


@app.route('/<lang_code>')
@app.route('/<lang_code>/index')
def index():
    return render_template('index.html', lang_code=g.current_lang, title=gettext('Home'))


@app.route('/<lang_code>/price')
def price():

    return render_template('price.html', lang_code=g.current_lang, title=gettext('Price'))


@app.route('/<lang_code>/about')
def about():

    return render_template('about.html', lang_code=g.current_lang, title=gettext('About'))


@app.route('/<lang_code>/faq')
def faq():

    return render_template('faq.html', lang_code=g.current_lang, title=gettext('FAQ'))


@app.route('/<lang_code>/contacts', methods=['GET', 'POST'])
def contacts():
    name = phone = email = message = ''
    bot = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', 'None')
        message = request.form.get('message', '')
        bot = request.form.get('bot', 'None')
        if bot == 'None':
            question_mail(name, phone, email, message)
            flash(gettext('Your message has been send. Thank you!'))
            return redirect(url_for('contacts', lang_code=g.current_lang))
    return render_template('contacts.html', lang_code=g.current_lang, title=gettext('Contacts'))


def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500



