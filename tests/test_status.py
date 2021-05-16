from httpx import get

endpoint = 'status'
url_base = 'http://localhost:5000/'
url = url_base + endpoint

class TestTask():
    def test_status_must_return_400_when_receive_a_get_without_code_param(self):
        request = get(url, params={})
        assert request.status_code == 400
    
    def test_status_must_return_400_when_receive_a_get_with_empty_code(self):
        request = get(url, params={'code': '' })
        assert request.status_code == 400
    
    def test_status_must_return_200_when_receive_any_code_different_than_null(self):
        code = '5310785,5310786' 
        request = get(url, params={'code': code })
        assert request.status_code == 200