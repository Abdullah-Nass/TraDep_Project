from flask import Flask, render_template, send_from_directory, url_for, redirect, request, session
import os
from books import Books
from essays import essays_print
from content import content
from groups import Groups_Mand
from studyPlan import Studyplan
from flask_babel import Babel, gettext as _
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("secret_key") 

app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'
app.config["LANGUAGES"] = {
    'ar': 'العربية',
    'en': 'English'
}
app.config['BABEL_DEFAULT_LOCALE'] = 'ar'

def get_locale():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(app.config["LANGUAGES"].keys()) or 'ar'


babel = Babel(app, locale_selector=get_locale)


@app.route('/set_language/<language>')
def set_language(language):
    if language in app.config["LANGUAGES"]:
        session["lang"]=language
    return redirect(request.referrer or url_for('home'))



app.jinja_env.globals.update(get_locale=get_locale)
app.register_blueprint(Books)
app.register_blueprint(content)
app.register_blueprint(essays_print)
app.register_blueprint(Groups_Mand)
app.register_blueprint(Studyplan)

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route("/")
def home():
    return render_template("home.html", is_home_active = "active")

@app.route("/دليل-اعضاء-الهيئة-التدريسية-لقسم-الترجمة-جامعة-اليرموك")
def emails():
    return render_template("emails.html", is_dr_active ="active")


@app.route("/الخطة-الدراسية-لقسم-الترجمة-جامعة-اليرموك")
def studyplan():
    return render_template("studyplan.html", is_plan_active = "active", credits=_('احمد حجازي'))

@app.route("/عن-قسم-الترجمة-التحريرية-والشفوية")
def about():
    return render_template("about.html",is_about='active')
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'sitemap.xml')
@app.route('/robots.txt')
def robots():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'robots.txt')





if __name__ == "__main__":
    app.run(host= "0.0.0.0" , debug=False)