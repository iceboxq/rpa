import pywinmacro as pw
import time


url = 'https://dict.naver.com/search.nhn?query=%ED%85%8C%EC%8A%AC%EB%9D%BC'


def n_search():
    pw.click((673, 62))
    pw.type_in(url)
    pw.key_press_once("enter")

n_search()