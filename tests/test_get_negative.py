import allure
import pytest
from framework.check import check_get_id
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts/N')
@pytest.mark.xfail(reason="non-existent id")
@allure.title('Negative. Get id_post=101')
def test_get_specific_resource_negative(input_value):
    response = Client().get_post_by_id(input_value)
    check_get_id(response)
