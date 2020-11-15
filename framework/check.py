import allure
from hamcrest import assert_that, equal_to
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    try:
        assert_that(response.status_code, equal_to(expected_code),
                    f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')
    except Exception as e:
        print("Исключение:", e)

@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))

@allure.step
def check_get_title(response):
    _response_general_check(response)
    assert_that(response.json()["title"], equal_to("sunt aut facere repellat provident occaecati excepturi optio reprehenderit"))

@allure.step
def check_get_id(response):
    _response_general_check(response)
    assert_that((response.status_code), equal_to(404))

def _response_create_resourse(response, expected_code=201):
    try:
        assert_that(response.status_code, equal_to(expected_code),
                    f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')
    except Exception as e:
        print("Исключение:", e)

@allure.step
def check_create_resourse(response):
    _response_create_resourse(response)
