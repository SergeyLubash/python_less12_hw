from flask import request, render_template, Blueprint
import logging
from config import POST_PATH
from exceptions import DataJsonError
from functions import search_posts_by_substring, load_json_data

main_blueprint = Blueprint('main_blueprint', __name__)


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get('s', "")
    logging.info("Выполняется поиск")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Проблема с открытием файла постов"
    filtered_posts = search_posts_by_substring(posts, s)
    return render_template("post_list.html", posts=filtered_posts, s=s)
