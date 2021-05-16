from httpx import post
import random
import string

url_base = 'http://localhost:5000/'
endpoint = 'equipment/'
url = url_base + endpoint

vessel = 'MV108' 

name = "compressor"
code = "5310B9D7"
location = "Brasil"  


class TestTask():
    def test_equipament_must_return_400_when_receive_a_post_without_code_param(self):
        request = post(url + vessel, data={})
        assert request.status_code == 400

    def test_equipament_must_return_400_when_receive_a_post_and_code_value_is_null(self):
        request = post(url + vessel, data={'code': ''})
        assert request.status_code == 400

    def test_equipament_must_return_400_when_receive_a_post_without_name_param(self):
        request = post(url + vessel, data={'code': code })
        assert request.status_code == 400

    def test_equipament_must_return_400_when_receive_a_post_and_name_value_is_null(self):
        request = post(url + vessel, data={'code': code, 'name': '' })
        assert request.status_code == 400
    
    def test_equipament_must_return_400_when_receive_a_post_without_location_param(self):
        request = post(url + vessel, data={'code': code, 'name': name })
        assert request.status_code == 400

    def test_equipament_must_return_400_when_receive_a_post_and_name_value_is_null(self):
        request = post(url + vessel, data={'code': code, 'name': name, 'location': '' })
        assert request.status_code == 400

    def test_equipament_must_return_404_if_vessel_not_found(self):
        vessel = 'MV011' 
        request = post(url + vessel, data={'code': code, 'name': name, 'location': location })
        assert request.status_code == 404
    
    def test_equipament_must_return_400_if_equipament_code_is_not_unique(self):
        request = post(url + vessel, data={'code': code, 'name': name, 'location': location})
        assert request.status_code == 400
    
    def test_equipament_must_Return_201_if_equipament_dont_exists_yet(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
        request = post(url + vessel, data={'code': code, 'name': name, 'location': location})
        assert request.status_code == 201


