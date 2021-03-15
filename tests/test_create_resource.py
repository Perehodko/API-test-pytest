import allure
import pytest
from framework.check import check_create_resource
from framework.jsonplaceholder_client import Client
from framework.data.constants.smoke_consts import USER_IDS, TITLE, BODY_RESOURCE


@allure.suite('POST /posts')
@pytest.mark.parametrize('user_id', USER_IDS)
@allure.title('Positive. Send POST and create a resource')
def test_create_resource(prepared_resource_id, user_id):
    data = {
        "title": TITLE,
        "body": BODY_RESOURCE,
        "userId": user_id
    }
    response = Client().create_post(data)
    check_create_resource(response)
