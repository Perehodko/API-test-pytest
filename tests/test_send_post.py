import allure
import pytest
from framework.check import check_create_resourse
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestSendPost:
    @pytest.mark.parametrize('data',
                             [{"title": 'title_1', "body": 'text text text',"userId": 101}, {"title"}])
    @allure.title('Positive. Send post and create a resource')
    def test_create_resourse(self, data):
        response = Client().create_resourse(data)
        check_create_resourse(response)