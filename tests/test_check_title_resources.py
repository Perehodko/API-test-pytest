import allure
import pytest
from framework.check import check_get_title
from framework.jsonplaceholder_client import Client


@pytest.mark.parametrize('data, correct_title', [
    (1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'),
    (2, 'qui est esse'),
    (3, 'ea molestias quasi exercitationem repellat qui ipsa sit aut'),
    (4, 'eum et est occaecati'),
    (5, 'nesciunt quas odio'),
    (6, 'dolorem eum magni eos aperiam quia'),
    pytest.param(7, 'another title1', marks=pytest.mark.xfail(reason='incorrect title')),
    pytest.param(8, 'another title3', marks=pytest.mark.xfail(reason='incorrect title'))])
@allure.title('Positives and Negatives (7, 8). Get posts and check titles')
def test_get_specific_resources(data, correct_title):
    response = Client().get_post_by_id(data)
    check_get_title(response, correct_title)
