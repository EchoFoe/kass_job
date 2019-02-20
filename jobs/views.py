from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from jobs.models import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages

def job(request, job_id):
    jobs = Job.objects.get(id=job_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)

    return render(request, 'landing/jobs.html', locals())



