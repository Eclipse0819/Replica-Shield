from django.shortcuts import render
from responses.models import Response
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):

    return render(request, 'profile.html')


@login_required
def database_view(request):

    responses = Response.objects.all()

    return render(request, 'dataview.html', {'responses': responses})


