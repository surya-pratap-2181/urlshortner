from django.contrib import messages
from django.shortcuts import redirect, render
from .models import ShortURL
from django.db.models import Sum
import random
import string

# Create your views here.


def home(request, query=None):
    if not query or query is None:
        return render(request, 'core/home.html')
    else:
        try:
            check = ShortURL.objects.get(short_query=query)
            check.visits += 1
            check.save()
            return redirect(check.original_url)
        except ShortURL.DoesNotExist:
            messages.error(request, "URL does not exist")
            return render(request, 'core/home.html')

    # return render(request, 'core/home.html')


def delete_url(request, id):
    url = ShortURL.objects.get(id=id)
    url.delete()
    return redirect('/dashboard/')


def dashboard(request):
    if request.user.is_anonymous:
        messages.info(request, 'Login required!!')
        return redirect('/accounts/')
    else:
        person = ShortURL.objects.filter(user=request.user)
        total = person.aggregate(Sum('visits'))
        visits = total.get('visits__sum')
        return render(request, 'core/dashboard.html', {'usr': person, 'visits': visits})


def random_query():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(6))


def short_url(request):
    if request.user.is_anonymous:
        messages.info(request, 'Login required!!')
        return redirect('/accounts/')
    if request.method == "POST":
        if request.POST['url'] and request.POST['short']:
            usr = request.user
            original_url = request.POST['url']
            short_query = request.POST['short']
            check = ShortURL.objects.filter(short_query=short_query)
            if not check:
                newurl = ShortURL(
                    user=usr,
                    original_url=original_url,
                    short_query=short_query,
                )
                newurl.save()
                messages.success(request, "Your URL is generated")
                # return redirect("/")
                newquery = ShortURL.objects.last().short_query
                myurl = "http://127.0.0.1:8000/" + newquery
                return render(request, 'core/shorturl.html', {'myurl': myurl})
            else:
                messages.error(request, "Already Exists")
                return redirect('/shorturl/')
        elif request.POST['url']:
            # generate random url as short url is not set
            usr = request.user
            original_url = request.POST['url']
            generated = False
            while not generated:
                short_query = random_query()
                check = ShortURL.objects.filter(short_query=short_query)
                if not check:
                    newurl = ShortURL(
                        user=usr,
                        original_url=original_url,
                        short_query=short_query,
                    )
                    newurl.save()
                    messages.success(request, "Your URL is generated")
                    newquery = ShortURL.objects.last().short_query
                    myurl = "http://127.0.0.1:8000/" + newquery
                    return render(request, 'core/shorturl.html', {'myurl': myurl})
                else:
                    continue
        else:
            # If Didn't Provide a url
            messages.error(request, "Please Provide a Link")
            return redirect('/shorturl/')
    return render(request, 'core/shorturl.html', {'myurl': "Short URL appear here"})
