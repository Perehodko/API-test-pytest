import allure
from framework.jsonplaceholder_client import Client
from framework.check import response_general_check
from framework.data.constants.smoke_consts import USER_IDS


@allure.suite('PATCH /posts/{post_id}')
@allure.title('Positive. Patch a resource')
def test_delete_resource():
    data = {
        'title': 'New title for post'
    }
    response = Client().patch_post(USER_IDS[0], data)
    response_general_check(response)
