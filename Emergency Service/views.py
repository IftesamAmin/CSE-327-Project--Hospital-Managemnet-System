from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import detail
from django.views.generic.list import ListView
# Create your views here.




@login_required

def detail(request):
    """
      This method is used to show the the types of service and their registration


      :param request: it's a HttpResponse from user.


      :type request: HttpResponse.


      :return: this method returns a html page viewing all details about the service


      :rtype: HttpResponse.
      """
    detail= detail.objects.all()
    context = {
        'detail' : detail
    }
    return render(request, 'EmergencyService/detail.html', context)
