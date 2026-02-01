from flask import Blueprint, render_template
from flask_babel import Babel, gettext as _

essays_print = Blueprint(__name__, "essays_print", static_folder="static", template_folder="templates")



@essays_print.route("/علم-المعاني-والبرجماتية-واهمية-التمييز-بينهما-لطلاب-قسم-الترجمة")
def semantics_pragmatics():
    return render_template("semaNpragEssay.html")
    
@essays_print.route("/الوحدة-الصرفية-(morpheme)-و-الوحدة المعجمية-(lexeme)-لطلاب-قسم-الترجمة")
def morpheme_lexeme():
    return render_template("morphNlexeEssay.html")