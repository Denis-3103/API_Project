import requests

"""Список HTTP методов"""

class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_method.headers, cookies=Http_method.cookie)
        return result