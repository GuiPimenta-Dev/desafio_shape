from httpx import get

endpoint = 'vessel'
url_base = 'http://localhost:5000/'
url = url_base + endpoint

code = '/MV100' 


class TestTask():
    def test_vessel_must_return_400_when_receive_a_get_without_params(self):
        request = get(url)
        assert request.status_code == 404
    
    def test_vessel_must_return_404_when_receive_a_get_with_params_and_vessel_not_found(self):
        request = get(url+code)
        assert request.status_code == 404
    
    def test_vessel_must_return_200_when_receive_a_get_with_params_and_vessel_contains_active_equipments(self):
        request = get(url+code)
        assert request.status_code == 200
    
    def test_vessel_must_return_204_when_receive_a_get_with_params_and_vessel_dont_contains_active_equipments(self):
        request = get(url+code)
        assert request.status_code == 204