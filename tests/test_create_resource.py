import allure
import pytest
from framework.check import check_create_resource
from framework.jsonplaceholder_client import Client
from framework.data.constants.smoke_consts import COMPANY_IDS, TITLE, BODY_RESOURCE


@allure.suite('POST /posts')
@pytest.mark.parametrize('company_id', COMPANY_IDS)
@allure.title('Positive. Send POST and create a resource')
def test_create_resource(company_id):
    data = {
        "title": TITLE,
        "body": BODY_RESOURCE,
        "userId": company_id }
    response = Client().create_resource_good(data)
    check_create_resource(response)
