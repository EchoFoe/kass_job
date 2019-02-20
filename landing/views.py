from django.shortcuts import render
from .forms import *
from job_seeker.forms import *
from employer.forms import *
from jobs.models import *
from django.db.models import Count

def home(request):
    # products_images = ProductImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
    # products_images_mot_masla = products_images.filter(Product__category_id=1)
    # products_images_indust_masla = products_images.filter(Product__category_id=3)
    # products_images_indust_transmis_masla = products_images.filter(Product__category_id=4)
    # products_images_gydra_masla = products_images.filter(Product__category_id=5)
    # products_images_prom_masla = products_images.filter(Product__category_id=6)
    # products_images_smazki = products_images.filter(Product__category_id=7)
    # products_images_tormoz_masla = products_images.filter(Product__category_id=8)
    # products_images_mot_mobil_masla = products_images.filter(Product__category_id=9)
    # products_images_prochee = products_images.filter(Product__category_id=10)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    return render(request, 'landing/home.html', locals())

def job_seeker(request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    form = Job_seekerForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'job_seeker/job_seeker.html', locals())

def employer(request):
    job_seekers = Job_seeker.objects.filter(is_active=True)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    form = EmployerForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["first_name"])
        new_form = form.save()
    return render(request, 'employer/employer.html', locals())

def information(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()


    return render(request, 'information/information.html', locals())

def jobs(request):

    jobs_images = JobImage.objects.filter(is_active=True, is_main=True, Job__is_active=True)
    jobs_images_1 = jobs_images.filter(Job__category_id=1)
    jobs_images_2 = jobs_images.filter(Job__category_id=2)
    jobs_images_3 = jobs_images.filter(Job__category_id=3)
    jobs_images_4 = jobs_images.filter(Job__category_id=4)
    jobs_images_5 = jobs_images.filter(Job__category_id=5)
    jobs_images_6 = jobs_images.filter(Job__category_id=6)
    jobs_images_7 = jobs_images.filter(Job__category_id=7)
    jobs_images_8 = jobs_images.filter(Job__category_id=8)
    jobs_images_9 = jobs_images.filter(Job__category_id=9)
    jobs_images_10 = jobs_images.filter(Job__category_id=10)
    jobs_images_11 = jobs_images.filter(Job__category_id=11)
    jobs_images_12 = jobs_images.filter(Job__category_id=12)
    jobs_images_13 = jobs_images.filter(Job__category_id=13)
    jobs_images_14 = jobs_images.filter(Job__category_id=14)
    jobs_images_15 = jobs_images.filter(Job__category_id=15)
    jobs_images_16 = jobs_images.filter(Job__category_id=16)

    categories = JobCategory.objects.filter(is_active=True)
    category_1 = JobCategory.objects.get(id=1)
    category_2 = JobCategory.objects.get(id=2)
    category_3 = JobCategory.objects.get(id=3)
    category_4 = JobCategory.objects.get(id=4)
    category_5 = JobCategory.objects.get(id=5)
    category_6 = JobCategory.objects.get(id=6)
    category_7 = JobCategory.objects.get(id=7)
    category_8 = JobCategory.objects.get(id=8)
    category_9 = JobCategory.objects.get(id=9)
    category_10 = JobCategory.objects.get(id=10)
    category_11 = JobCategory.objects.get(id=11)
    category_12 = JobCategory.objects.get(id=12)
    category_13 = JobCategory.objects.get(id=13)
    category_14 = JobCategory.objects.get(id=14)
    category_15 = JobCategory.objects.get(id=15)
    category_16 = JobCategory.objects.get(id=16)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()


    return render(request, 'jobs/jobs.html', locals())

def contact(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()


    return render(request, 'contact/contact.html', locals())