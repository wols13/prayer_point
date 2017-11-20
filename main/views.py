from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book, PrayerPoint, Category, Bible

# Create your views here.


def index(request):
    headers_template = loader.get_template('main/headers.html')
    index_template = loader.get_template('main/index.html')
    return HttpResponse(headers_template.render({}, request) + index_template.render({}, request))


def sorted_by_scripture(request):
    headers_template = loader.get_template('main/headers.html')
    chapters_div = loader.get_template('main/chapters_div.html')

    books = Book.objects.order_by('id')
    categories = Category.objects.order_by('name')
    context = {
        'books': books,
        'categories': categories,
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
                prayer_points = PrayerPoint.objects.filter(book=book, chapter=chapter, verse=verse)
            else:
                prayer_points = PrayerPoint.objects.filter(book=book, chapter=chapter)
        else:
            prayer_points = PrayerPoint.objects.filter(book=book)
    except PrayerPoint.DoesNotExist:
        prayer_points = None

    context = {'prayer_points': prayer_points,}
    return HttpResponse(prayer_points_list.render(context, request))


def add_prayer_point(request):
    headers_template = loader.get_template('main/headers.html')
    add_pp_template = loader.get_template('main/add_prayer_point.html')

    books = Book.objects.order_by('id')
    context = {
        'books': books,
    }
    return HttpResponse(headers_template.render({}, request) + add_pp_template.render(context, request))


def number_of_chapters(request):
    book = int(request.GET['book'])

    chapter_drop_down = loader.get_template('main/chapter_drop_down.html')
    try:
        result = Book.objects.filter(id=book)
        result = result[0].no_of_chapters
    except Book.DoesNotExist:
        result = 0

    context = {'chapter_range': range(1, result + 1)}
    return HttpResponse(chapter_drop_down.render(context, request))


def get_scripture(request):
    book = int(request.GET['book'])
    chapter = int(request.GET['chapter'])
    verse = int(request.GET['verse'])

    try:
        result = Bible.objects.filter(b=book, c=chapter, v=verse)
        result = result[0].t
    except Bible.DoesNotExist:
        result = ""

    return HttpResponse(result)











