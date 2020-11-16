import allure
import pytest
from framework.check import check_create_resourse
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestSendPost:
    @pytest.mark.parametrize('data', [
        {"title": 'title_1', "body": 'text text text', "userId": 101},
        {"title": 'title_1', "body": 'text text text'},
        {"title": 'title_1'},
    ])
    @allure.title('Positive. Send POST and create a resource')
    def test_create_resourse(self, data):
        response = Client().create_resourse_good(data)
        check_create_resourse(response)

    @pytest.mark.xfail(reason="Send POST on unresolve resourse")
    @pytest.mark.parametrize('data', [
        {"title": 'title_one', "body": 'text body', "userId": 102}])
    @allure.title('Negative. Send POST on unresolve resourse')
    def test_create_resourse_b(self, data):
        response = Client().create_resourse_bad(data)
        check_create_resourse(response)
