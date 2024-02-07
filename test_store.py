from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
from requests.exceptions import HTTPError
import json
import jsonschema
import random

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''

# @pytest.fixture
def sample_data():
    return {
        "pet_id": 0
    }

def post_order(test_endpoint):
    try:
        response = api_helpers.post_api_data(test_endpoint,sample_data())
        json_data = json.loads(response.content)
        assert response.status_code == 201
        order_id = json_data["id"]
        validate(instance=response.json(), schema=schemas.Order)
        return order_id
        
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")
    

@pytest.mark.parametrize("status", ['available', 'pending'])
def test_patch_order_by_id(status):
    try:
        test_endpoint = "/store/order"
        order_id = post_order(test_endpoint)
        new_endpoint = test_endpoint + "/" + str(order_id)
        params = { 
            "status": status
        }
        response = api_helpers.patch_api_data(new_endpoint, params)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
        json_data = json.loads(response.content)
        assert json_data["message"] == "Order and pet status updated successfully"
    except HTTPError as e:
        pytest.fail(f"HTTPError occurred: {e}")
