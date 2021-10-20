from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "index.html", {'authorized': True, 'questions': range(25)})


def ask(request: HttpRequest):
    return render(request, "ask.html", {'authorized': True})


def tag(request: HttpRequest):
    return render(request, "tag.html", {'authorized': True, 'tag': 'bender', 'questions': range(5)})


def settings(request: HttpRequest):
    return render(request, "settings.html", {'authorized': True})


def login(request: HttpRequest):
    return render(request, "login.html", {'authorized': False})


def register(request: HttpRequest):
    return render(request, "registration.html", {'authorized': False})


# Просто, чтобы показать все кнопочки верстки. Я знаю, что у Django есть модельки
class Answer:
    checked_correct: bool

    def __init__(self, correct: bool):
        self.checked_correct = correct


def question(request: HttpRequest):
    return render(request, "question.html", {
        'authorized': True,
        'answers': [Answer(i % 2 == 0) for i in range(3)],
        'is_author': False,
    })