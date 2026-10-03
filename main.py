import requests

def test_get_post():
    response = requests.get('https//dummyjson.com/products/1')
    assert response.status_code == 200