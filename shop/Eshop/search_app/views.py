from django.shortcuts import render
from shopapp.models import Product
from django.db.models import Q
# Create your views here.

def searchResult(request):
    products=None
    queri=None
    if 'q' in request.GET:
        queri=request.GET.get('q')
        products=Product.objects.all().filter(Q(name__contains=queri)|Q(description__contains=queri))
        return render(request,'search.html',{'queri':queri,'products':products})
