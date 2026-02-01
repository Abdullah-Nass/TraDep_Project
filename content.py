from flask import Blueprint, send_from_directory

content = Blueprint("content",__name__, static_folder="static", template_folder="templates")

@content.route('/contents/images/<filename>')
def send_image(filename):
    return send_from_directory('static/images', filename)
@content.route('/contents/images/prof/<filename>')
def send_prof_pic(filename):
    return send_from_directory('static/images/profs', filename)


@content.route('/contents/<dir_name>/<file_cover>')
def send_cover(file_cover, dir_name):
    return send_from_directory(f'static/{dir_name}', file_cover)
