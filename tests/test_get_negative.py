import allure
import pytest
from framework.check import check_get_id
from framework.jsonplaceholder_client import Client
from framework.data.constants.smoke_consts import USER_IDS


@allure.suite('GET /posts/N')
@pytest.mark.xfail(reason="non-existent id")
@allure.title('Negative. Get id_post=101')
def test_get_specific_resource_negative():
    response = Client().get_post_by_id(USER_IDS[0])
    check_get_id(response)
