import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)

Session = requests.Session()

def test_post_create(user_login):
    res = Session.post(url=data['url3_post'], headers={'X-Auth-Token': user_login},
    data={'title': data['title'], 'description': data['description'], 'content': data['content']})
    assert str(res) == '<Response [200]>', 'post_create FAIL'


def test_check_post_create(user_login, get_description):

    result = Session.get(url=data['url2'], headers={'X-Auth-Token': user_login}).json()['data']
    list_description = [i['description'] for i in result]
    assert get_description in list_description, 'check_post_create FAIL'


if __name__ == "__main__":
    pytest.main(["-vv"])
    