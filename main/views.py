from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, Prayer_point

# Create your views here.


def index(request):
    headers_template = loader.get_template('main/headers.html')
    index_template = loader.get_template('main/index.html')
    return HttpResponse(headers_template.render({}, request) + index_template.render({}, request))


def sorted_by_scripture(request):
    headers_template = loader.get_template('main/headers.html')
    chapters_div = loader.get_template('main/chapters_div.html')

    books = Book.objects.order_by('id')
    context = {
        'books': books,
    }

    return HttpResponse(headers_template.render({}, request) + chapters_div.render(context, request))


def prayer_point_by_scripture(request):
    book = int(request.GET['book'])
    chapter = int(request.GET['chapter'])
    verse = int(request.GET['verse'])

    prayer_points_list = loader.get_template('main/prayer_points_list.html')
    try:
        if chapter != 0:
            if verse != 0:
                prayer_points = Prayer_point.objects.filter(book=book, chapter=chapter, verse=verse)
            else:
                prayer_points = Prayer_point.objects.filter(book=book, chapter=chapter)
        else:
            prayer_points = Prayer_point.objects.filter(book=book)
    except Prayer_point.DoesNotExist:
        prayer_point = None

    context = {'prayer_points': prayer_points}
    return HttpResponse(prayer_points_list.render(context, request))


def sorted_by_category(request):
    headers_template = loader.get_template('main/headers.html')
    return HttpResponse(headers_template.render({}, request))
