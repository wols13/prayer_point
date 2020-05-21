from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .models import PrayerPoint, Category
from .forms import AddPPForm


def index(request):
    headers_template = loader.get_template('main/headers.html')
    index_template = loader.get_template('main/index.html')
    return HttpResponse(headers_template.render({}, request) + index_template.render({}, request))


def sorted_by_category(request):
    headers_template = loader.get_template('main/headers.html')
    chapters_div = loader.get_template('main/chapters_div.html')

    categories = Category.objects.order_by('cat_id')
    context = {'categories': categories}

    return HttpResponse(headers_template.render({}, request) + chapters_div.render(context, request))


def prayer_point_by_category(request):
    category = request.GET['category']

    prayer_points_list = loader.get_template('main/prayer_points_list.html')
    try:
        prayer_points = PrayerPoint.objects.filter(category__icontains=category)
        paginator = Paginator(prayer_points, 20, orphans=4)
        try:
            page = paginator.page(request.GET['page_no'])
            context = {'prayer_points': page}
        except (InvalidPage, EmptyPage) as e:
            context = {'prayer_points': None}
    except PrayerPoint.DoesNotExist:
        context = {'prayer_points': None}

    return HttpResponse(prayer_points_list.render(context, request))


def add_prayer_point(request):
    headers_template = loader.get_template('main/headers.html')
    add_pp_template = loader.get_template('main/add_prayer_point.html')
    suggestion_received = 0
    job_response = ""
    job_response_code = 0

    if request.method == 'POST':
        form = AddPPForm(request.POST)
        if form.is_valid():
            subject = 'Omoilorin: New prayer point suggestion'
            recipients = ['ayodeji.oyewole@gmail.com']
            sender = 'ayodeji.oyewole@gmail.com'
            message = generate_email_content(form.cleaned_data)
            try:
                suggestion_received = send_mail(subject, message, sender, recipients)
            except:
                pass

            job_response = "Suggestion could not be submitted. Please email your suggestion to us at ayodeji.oyewole@gmail.com"
            job_response_code = 2
            if suggestion_received:
                job_response = "Thank you for your suggestion! We will review it as soon as possible."
                job_response_code = 1
                try:
                    subject = 'Omoilorin: Prayer point suggestion received'
                    recipients = [form.cleaned_data['add_pp_email']]
                    sender = 'ayodeji.oyewole@gmail.com'
                    message = generate_suggestion_confirmation(form.cleaned_data)
                    send_mail(subject, message, sender, recipients)
                except:
                    pass
                form = AddPPForm()
        else:
            job_response = "Please fix the error(s) in the form below and re-submit."
            job_response_code = 2
    else:
        form = AddPPForm()
    context = {'form': form, 'job_response': job_response, 'job_response_code': job_response_code}
    return HttpResponse(headers_template.render({}, request) + add_pp_template.render(context, request))


def generate_email_content(cleaned_data):
    message = f"===========\nSender Details\n===========\nName: {cleaned_data['add_pp_full_name']}\n" + \
              f"Email: {cleaned_data['add_pp_email']}\n\n\n"
    return message + generate_prayer_point_details(cleaned_data)


def generate_suggestion_confirmation(cleaned_data):
    message = f"Hi {cleaned_data['add_pp_full_name']},\n\nThank you so much for your prayer point suggestion.\n\n" + \
              "This is a confirmation that we have received your suggestion and it will be added to the prayer " + \
              "point database upon review. We appreciate your contribution and encourage you to keep being involved" + \
              " in our prayer community.\n\n\n" + generate_prayer_point_details(cleaned_data) + "\n\n\nThank you, " + \
              "stay blessed.\nOmoilorin team."
    return message


def generate_prayer_point_details(cleaned_data):
    details = f"==============\nPrayer point details\n==============\nBible ref: {cleaned_data['add_pp_bible_ref']}" + \
              f"\nContent: {cleaned_data['add_pp_content']}\nSuggested categories: "

    categories = {'add_pp_cat_cons': 'Consecration', 'add_pp_cat_fami': 'Family', 'add_pp_cat_nati': 'Nation/Land',
                  'add_pp_cat_warf': 'Warfare', 'add_pp_cat_dire': 'Direction', 'add_pp_cat_favo': 'Favour',
                  'add_pp_cat_prot': 'Protection', 'add_pp_cat_weal': 'Wealth', 'add_pp_cat_enco': 'Encouragement',
                  'add_pp_cat_heal': 'Health', 'add_pp_cat_prov': 'Provision', 'add_pp_cat_wors': 'Worship'}
    suggested_categories = ""
    for category in categories:
        if cleaned_data[category]:
            if len(suggested_categories) > 0:
                suggested_categories += ', '
            suggested_categories += categories[category]
    return details + suggested_categories







