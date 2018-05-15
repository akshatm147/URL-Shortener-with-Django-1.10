from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .models import MyUrl
from .forms import SubmitUrlForm

# Create your views here.

def home_view_fbv(request, *args, **kwargs):
    if request.method== 'POST':
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" : "Akshat's URL Shortener",
            "form" : the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        context = {
            "title" : "Akshat's URL Shortener",
            "form" : form
        }

        template = "shortener/home.html"

        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = MyUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(MyUrl, shortcode=shortcode)
        # save item
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


'''
def kirr_redirect_view(request, shortcode=None, *args, **kwargs): #function based view FBV
    #print(request.user)
    #print(request.user.is_authenticated())\
    print('method is \n')
    print(request.method)
    #obj = KirrURL.objects.get(shortcode=shortcode)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    #obj_url = obj.url
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()
    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponse("hello {sc}".format(sc=obj.url))
'''
