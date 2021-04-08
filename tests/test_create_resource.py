import allure
import pytest
from framework.check import check_create_resource
from framework.jsonplaceholder_client import Client
from framework.data.constants.smoke_consts import USER_IDS, TITLES, BODY_RESOURCE


@allure.suite('POST /posts')
@pytest.mark.parametrize('prepared_resource_id', USER_IDS, indirect=True)
@allure.title('Positive. Send POST and create a resource')
def test_create_resource(prepared_resource_id):
    data = {
        "title": TITLES[0],
        "body": BODY_RESOURCE,
        "userId": prepared_resource_id
    }
    response = Client().create_post(data)
    check_create_resource(response)
