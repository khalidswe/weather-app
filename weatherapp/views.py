from django.shortcuts import render,redirect
import datetime, requests

# Create your views here.

def IndexPage(request):

    try:
        if 'cityname' in request.POST:
            cityname = request.POST['cityname']
        else:
            
            cityname = 'Dhaka'

        api_id = '0a9ea7602e4a85d5f8f03d2efa0ee7d4'
        api_url = 'http://api.openweathermap.org/data/2.5/weather'

        parameter = {'q': cityname, 'appid' : api_id, 'units': 'metric' }

        r = requests.get(url=api_url, params= parameter)
        res = r.json()
        description = res['weather'][0]['description']
        temparature = res['main']['temp']
        city = res['name']
        country = res['sys']['country']
        feels = res['main']['feels_like']
        min_temp = res['main']['temp_min']
        max_temp = res['main']['temp_max']
        date = datetime.date.today()
        day = datetime.date.today().strftime("%A")

        return render(request,"weather/index.html",{'description': description,'temp': temparature,'date':date,'day':day,'country':country,'city':city,
        'feels': feels,'max_temp':max_temp,'min_temp':min_temp})
    except:
        
        return redirect('index')

