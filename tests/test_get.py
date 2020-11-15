import allure
import pytest
from framework.check import check_get_all_posts_response, check_get_title, check_get_id
from framework.jsonplaceholder_client import Client


@allure.suite('GET')
class TestGetPosts:

    @allure.title('Positive. Get id_post=1')
    def test_get_all_posts(self):
        response = Client().get_post_by_id(1)
        check_get_title(response)

    @pytest.mark.xfail
    @allure.title('Negative. Get id_post=999')
    def test_get_all_posts(self):
        response = Client().get_post_by_id(999)
        check_get_id(response)
