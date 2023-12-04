from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_html_content(city):
    import requests

    city=city.replace(' ','+')

    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36 Edg/94.0.992.50"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content

def homepage(request):
    weather=dict()
    if 'city_name' in request.GET:
        city =request.GET.get('city_name')
        html_content = get_html_content(city)
        print(html_content)

        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content,'html.parser')
        
        weather['region'] = soup.find('span',attrs={'class': 'BBwThe'})
        # weather['temperature'] = soup.find('span',attrs={'class':'wob_tm'})
        print(weather)
    return render(request,'home.html',weather)