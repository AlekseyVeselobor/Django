from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
def home(request):
    text = """<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>Великорус А.О.</i>
"""
    return HttpResponseBadRequest(text)

def about(request):
    text = """ <p>Имя: <strong>Иван</strong>
<p>Отчество: <strong>Петрович</strong>
<p>Фамилия: <strong>Иванов</strong>
<p>телефон: <strong>8-923-600-01-02</strong>
<p>email: <strong>vasya@mail.ru</strong>
"""
    return HttpResponse(text):git add . 