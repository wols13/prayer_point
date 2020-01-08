from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, InvalidPage, EmptyPage
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
        paginator = Paginator(prayer_points, 20, orphans=4)
        try:
            page = paginator.page(request.GET['page_no'])
            context = {'prayer_points': page,}
        except (InvalidPage, EmptyPage) as e:
            context = {'prayer_points': None,}
    except PrayerPoint.DoesNotExist:
        context = {'prayer_points': None,}

    return HttpResponse(prayer_points_list.render(context, request))


def add_prayer_point(request):
    headers_template = loader.get_template('main/headers.html')
    add_pp_template = loader.get_template('main/add_prayer_point.html')

    return HttpResponse(headers_template.render({}, request) + add_pp_template.render({}, request))










