import json
from config import POST_PATH, UPLOAD_FOLDER
from exceptions import WrongImgType, DataJsonError


def load_json_data(path):
    """
    Функция загрузки  json файла
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_posts_by_substring(posts, substring):
    """ Функция поиска в постах """
    posts_founded = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded


def save_picture(picture):
    """ Функция загрузки картинки"""
    allowed_type = ["jpg", "png", "gif", "jpeg"]
    picture_type = picture.filename.split(".")[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Неверный формат файла! Допустимы только {', '.join(allowed_type)}")
    picture_path = f"{UPLOAD_FOLDER}/{picture.filename}"
    picture.save(picture_path)

    return picture_path


def add_post(posts, new_post):
    """ Функция добавления поста в список и сохранения json файла"""
    posts.append(new_post)
    with open(POST_PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file)
