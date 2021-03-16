from framework.jsonplaceholder_client import Client
from framework.check import _response_general_check


def get_all_post():
    response = Client().get_all_posts()
    _response_general_check(response)
    return response


def delete_post(post_id):
    response = Client().delete(post_id)
    _response_general_check(response)