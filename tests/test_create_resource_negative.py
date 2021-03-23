import allure
import pytest
from framework.check import check_create_resource
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
@pytest.mark.xfail(reason="Send POST on unresolved resource")
@pytest.mark.parametrize('data', [
    {
        "title": 'title_one',
        "body": 'text body',
        "userId": 102
    }]
                         )
@allure.title('Negative. Send POST on unresolved resource')
def test_create_resource_b(data):
    response = Client().create_resource_bad(data)
    check_create_resource(response)
