from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class DetailsPageView(TemplateView):
    template_name = 'details.html'























# Create your views here.

# def homePageView(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     return HttpResponse('Pages Application Home')

# def homePageView(request):
#     response = "<h1>Pages Application Home</h1>\n<p>New Paragraph</p>"
#     return HttpResponse(response)

# def homePageView(request):
#     return render(request, "home.html")


# def details(*args, **kwargs):
#     return HttpResponse('Details Application Home')

# def details(request):
#     return HttpResponse('Details Application Home')

# def details(request):
#     return render(request, 'details.html')