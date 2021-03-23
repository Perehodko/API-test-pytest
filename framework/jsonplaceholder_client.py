import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, data):
        return r.post(url=JSONPLACEHOLDER_HOST + path, data=data)

    def _delete(self, path: str):
        return r.post(url=JSONPLACEHOLDER_HOST + path)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def create_post(self, data):
        return self._post(path=f'/posts', data=data)

    @allure.step
    def create_resource_good(self, data):
        return self.create_post(path=f'/posts', data=data)

    @allure.step
    def create_resource_bad(self, data):
        return self.create_post(path=f'/post/1/comments', data=data)

    @allure.step
    def delete_post(self, post_id: int):
        return r.delete(url=JSONPLACEHOLDER_HOST + f'/posts/{post_id}')