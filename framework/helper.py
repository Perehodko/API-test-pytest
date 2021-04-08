from framework.jsonplaceholder_client import Client
from framework.check import _response_general_check
from framework.data.constants.smoke_consts import TITLES, BODY_RESOURCE
from framework.check import check_create_resource


def get_all_post():
    response = Client().get_all_posts()
    _response_general_check(response)
    return response


def delete_post(post_id):
    response = Client().delete_post(post_id)
    _response_general_check(response)


def gen_create_post(post_id):
    data = {
        'title': TITLES,
        'body': BODY_RESOURCE,
        'userId': post_id
    }
    response = Client().create_post(data)
    check_create_resource(response)
