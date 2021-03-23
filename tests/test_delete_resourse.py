import allure
import pytest
from framework.jsonplaceholder_client import Client
from framework.check import response_general_check
from framework.data.constants.smoke_consts import USER_IDS


@allure.suite('DELETE /posts/{post_id}')
@allure.title('Positive. Delete a resource')
@pytest.mark.parametrize('create_post', USER_IDS, indirect=True)
def test_delete_resource(create_post):
    response = Client().delete_post(create_post)
    response_general_check(response)
