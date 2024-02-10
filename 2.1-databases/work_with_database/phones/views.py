from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()

    sort_param = request.GET.get('sort')
    if sort_param == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort_param == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort_param == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()

    context = {
        'phones': phone_objects,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
