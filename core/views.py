from django.shortcuts import render
import requests

# Create your views here.


def home(request):
    return render(request, 'core/short.html', {'shorted_url': 'Your Response Will appear Here...'})


def shortner(request):
    if request.method == "POST":
        url = request.POST['url']
        access_token = "a9567bd55bf10f122a13dcf5e53f47c11b723fee"
        guid = "Bl8qcKchi0h"
        headers = {"Authorization": f"Bearer {access_token}"}
        # url = ""
        shorten_res = requests.post("https://api-ssl.bitly.com/v4/shorten",
                                    json={"group_guid": guid, "long_url": url}, headers=headers)
        if shorten_res.status_code == 200:
            # if response is OK, get the shortened URL
            link = shorten_res.json().get("link")
            print("Shortened URL:", link)
            shorted_url = link
            return render(request, 'core/short.html', {'shorted_url': shorted_url})
        else:
            print("Not Getting the shortened url")
            shorted_url = "Not Getting the shortened url"
            return render(request, 'core/short.html', {'shorted_url': shorted_url})
    else:
        shorted_url = "Your Response Will appear Here..."
    return render(request, 'core/short.html', {'shorted_url': shorted_url})
