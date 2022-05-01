from flask import Blueprint, render_template, request  # Сперва импорттируем класс блюпринта
import logging

import functions
from config import POST_PATH
from exceptions import WrongImgType

loader_blueprint = Blueprint('loader_blueprint', __name__)  # Затем создаем новый блюпринт
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route('/post', methods=["GET"])  # Создаем вьюшку, используя в декораторе блюпринт
def create_new_post_page():     # Создание нового поста
    return render_template("post_form.html")


@loader_blueprint.route('/post', methods=["POST"])
def create_new_post_user():       # Загрузка и добавление новых данных в список постов
    picture = request.files.get("picture")
    content = request.form.get("content")
    if not picture or not content:
        logging.info("Данные не загружены, отсутсвует часть данных")
        return "Отсутствует часть данных"

    posts = functions.load_json_data(POST_PATH)

    try:
        new_post = {"pic": functions.save_picture(picture), "content": content}
    except WrongImgType:
        return "Неверный тип изображения"
    functions.add_post(posts, new_post)
    return render_template("post_uploaded.html", new_post=new_post)
