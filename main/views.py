from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import PrayerPoint, Category


def index(request):
    headers_template = loader.get_template('main/headers.html')
    index_template = loader.get_template('main/index.html')
    return HttpResponse(headers_template.render({}, request) + index_template.render({}, request))


def sorted_by_category(request):
    headers_template = loader.get_template('main/headers.html')
    chapters_div = loader.get_template('main/chapters_div.html')

    categories = Category.objects.order_by('name')
    context = {
        'categories': categories,
    }

    return HttpResponse(headers_template.render({}, request) + chapters_div.render(context, request))


def prayer_point_by_category(request):
    category = request.GET['category']

    prayer_points_list = loader.get_template('main/prayer_points_list.html')
    try:
        prayer_points = PrayerPoint.objects.filter(category__icontains=category)
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










