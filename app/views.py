from django.http import HttpRequest
from django.shortcuts import render
from django.core.paginator import Paginator, Page
from random import randrange

questions = [{
    'title': f'Sample title for question #{i}',
    'id': i,
    'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur dolore hic necessitatibus quasi 
    quidem quod ratione tenetur totam voluptas? Alias minus modi nesciunt possimus temporibus? Dignissimos eos fugiat 
    libero ullam!''',
    'answers': [{
        'checked_correct': j % 2 == 0,
        'id': j,
        'title': f'Sample title for answer #{j}',
        'text': '''Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aspernatur dolore hic necessitatibus quasi 
        quidem quod ratione tenetur totam voluptas? Alias minus modi nesciunt possimus temporibus? Dignissimos eos fugiat 
        libero ullam!''',
        'stars': j
    } for j in range(i)],
    'tags': [['black jack', 'bender', 'aboba'][randrange(0, 3)]],
    'stars': i + 10
} for i in range(1000)]


def paginate(objects: list, request: HttpRequest, page_size: int = 20) -> Page:
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects, page_size)
    return paginator.page(page_num)


def index(request: HttpRequest):
    return render(request, "index.html", {'authorized': True, 'questions': paginate(questions, request)})


def hot(request: HttpRequest):
    sorted = list(questions)
    sorted.sort(key=lambda x: x['stars'], reverse=True)
    return render(request, "hot.html", {'authorized': True, 'questions': paginate(sorted, request)})


def ask(request: HttpRequest):
    return render(request, "ask.html", {'authorized': True})


def tag(request: HttpRequest, tag_name: str):
    return render(request, "tag.html", {
        'authorized': True,
        'tag': tag_name,
        'questions': paginate(list(filter(lambda x: tag_name in x['tags'], questions)), request)
    })


def settings(request: HttpRequest):
    return render(request, "settings.html", {'authorized': True})


def login(request: HttpRequest):
    return render(request, "login.html", {'authorized': False})


def register(request: HttpRequest):
    return render(request, "registration.html", {'authorized': False})


def question(request: HttpRequest, question_id: int):
    q = questions[question_id]
    return render(request, "question.html", {
        'authorized': True,
        'question': q,
        'answers': paginate(q['answers'], request),
        'is_author': False,
    })
