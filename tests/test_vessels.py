from httpx import post
import random
import string

endpoint = 'vessels'
url_base = 'http://localhost:5000/'
url = url_base + endpoint

class TestTask():
    def test_vessel_must_return_400_when_receive_a_post_without_code_param(self):
        request = post(url, data={})
        assert request.status_code == 400
    
    def test_vessel_must_return_400_when_receive_a_post_and_code_value_is_null(self):
        request = post(url, data={'code': '' })
        assert request.status_code == 400
    
    def test_vessel_must_return_400_when_receive_a_post_with_params_and_vessel_already_exists(self):
        code = 'MV108' 
        request = post(url, data={'code': code})
        assert request.status_code == 400
    
    def test_vessel_must_return_201_when_receive_a_post_with_params_and_vessel_dont_exists_yet(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        request = post(url, data={'code': code})
        assert request.status_code == 201