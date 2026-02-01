from flask import Blueprint, render_template
from flask_babel import Babel, gettext as _
import json
import os

Books = Blueprint(__name__, "Books", static_folder="static", template_folder="templates")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR,"templates", "books.json")
with open(path, "r", encoding="UTF-8") as file:
    content = json.load(file)
    
def names_codes ():
    return {
    'TRA101': _('قواعد اللغة الانجليزية (1)'),
    'TRA102': _('قواعد اللغة الانجليزية (2)'),
    'TRA104': _('كتابة الفقرة في اللغة الإنجليزية'),
    'TRA105': _('صوتيات اللغة الإنجليزية'),
    'TRA202': _('النحو التطبيقي المقارن (1)'),
    'TRA208': _('قراءة متقدمة باللغة الإنجليزية'),
    "TRA210": _("مدخل الى الأدب الإنجليزي والعربي"),
    'TRA230': _('ترجمة عامة(E-ع)'),
    'TRA232': _('ترجمة عامة (ع-E)'),
    'TRA241': _('مقدمة في نظريات الترجمة'),
    'TRA320': _('قواعد متقدمة باللغة الانجليزية'),
    'TRA206': _('كتابة المقال في اللغة الانجليزية'),
    'TRA311': _('الترجمة الأدبية'),
    'TRA312': _('الترجمة السمعبصرية'),
    'TRA321': _('علم المعاني والبراجماتية'),      
    'TRA330': _('الترجمة التتابعة والفورية (E-ع)'),
    "TRA331": _("الترجمة التتابعة والفورية (ع-E)"),
    'TRA332': _('الترجمة بإستخدام الحاسوب'),
    'TRA333': _('الترجمة القانونية'),
    'TRA334': _('الترجمة الاعلامية'),
    'TRA335': _('الترجمة التقنية'),
    'TRA430': _('تحليل الخطاب'),
    'TRA431': _('النحو العربي لأغراض الترجمة'),
    'TRA433': _('الترجمة والسياحة'),
    'TRA412': _('ترجمة القصة القصيرة'),
    'TRA340': _('المعاجم والمصطلحات'),
    'TRA433A': _('الترجمة والسياحة'),
    'TRA439': _('مشروع التخرج'),
    "TRA438": _("ترجمة نصوص دينية"),
    "TRA435": _("موضوع خاص في الترجمة"),
}
@Books.route("/كتب-مساقات-قسم-الترجمة-جامعة-اليرموك-الاجبارية")
def mandatory():
        return render_template("view.html" ,
        title= _("كتب مساقات قسم الترجمة جامعة اليرموك الاجبارية"),
        name_of_catg = _("قسم اجباري"),
        pre_table = _('كتب مساقات قسم الترجمة جامعة اليرموك الاجبارية'),
        description = _("موقع تعليمي لطلاب قسم الترجمة في جامعة اليرموك: اكتشف مجموعة واسعة من كتب الترجمة والمراجع العلمية لطلاب قسم الترجمة لمواد القسم الاجبارية في جامعة اليرموك. وفر وقتك مع موارد تعليمية شاملة جاهزة للتحميل مجانا لدعم دراستك"),
        dic = content['mandatory'],
        choices = names_codes(),
        credits =_("لين صمادي"),
        dirname = "MandatoryBookCover",
        mandatory_active ="active")

@Books.route("/كتب-مساقات-قسم-الترجمة-جامعة-اليرموك-الاختيارية")
def optional():
    return render_template("view.html" ,
    title=_("كتب مساقات قسم الترجمة جامعة اليرموك الاختيارية"),
    pre_table = _('كتب مساقات قسم الترجمة جامعة اليرموك الاختيارية'),
    description =_( "موقع تعليمي لطلاب قسم الترجمة في جامعة اليرموك: اكتشف مجموعة واسعة من كتب الترجمة والمراجع العلمية لطلاب قسم الترجمة لمواد القسم الاختيارية في جامعة اليرموك. وفر وقتك مع موارد تعليمية شاملة جاهزة للتحميل مجانا لدعم دراستك"),
    dic = content["elective"],
    choices = names_codes(),
    dirname = "OptionalBookCover",
    credits =_("لين صمادي"),
    optional_active ="active")

@Books.route("/ملخصات-مساقات-قسم-الترجمة-tenses-rule")
def tenses_rule():
    return render_template("view.html",
        title=_("Tenses Rule ملخصات قسم الترجمة "),
        description = _("ملخصات لمواد قسم الترجمة جامعة اليرموك.Tenses Rule . كتب قسم الترجمة جامعة اليرموك. تحميل كتب."),
        pre_table = _('Tenses Rule جميع ملخصات'),
        dic = content["tenses_rule"],
        choices = names_codes(),
        credits ="Tenses Rule Group",
        dirname= "TensesRuleBookCover",
        TR_active="active",
     )