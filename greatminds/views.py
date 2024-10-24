from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'greatminds/index.html')

def about(request):
    return render(request, 'greatminds/about.html')

def blog(request):
    return render(request, 'greatminds/blog.html')

def contact(request):
    return render(request, 'greatminds/contact.html')

def detail(request):
    return render(request, 'greatminds/detail.html')

def feature(request):
    return render(request, 'greatminds/feature.html')

def price(request):
    return render(request, 'greatminds/price.html')

def quote(request):
    return render(request, 'greatminds/quote.html')

def service(request):
    return render(request, 'greatminds/service.html')

def team(request):
    return render(request, 'greatminds/team.html')

def testimonial(request):
    return render(request, 'greatminds/testimonial.html')