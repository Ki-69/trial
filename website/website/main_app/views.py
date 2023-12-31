from datetime import date
from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
import requests
from django.urls import reverse
from django.core.mail import send_mail
# Create your views here.

def index(request):
    if request.method == 'POST':
        email=request.POST['email'] 
        phone=request.POST['phone']
        message=request.POST['message']
        send_mail(
            'Feedback form submitted',
            f"Message: {message} \nPhone Number:  {phone}  \nEmail Address:  {email} \nThis is an auto-generated message",
            email,
            ['eoikvkathmandu@gmail.com']
        )
        return HttpResponseRedirect(reverse('index'))
    else:
        quotes=quote.objects.get()
        if date.today() != quotes.last_updated:
            api_url = 'https://api.api-ninjas.com/v1/quotes?category=inspirational'
            response = requests.get(api_url, headers={'X-Api-Key': 'W0FQSDaLu2ED6wnd+pkcnA==KAQ9M2sJJyNPqYUL'})
            if response.status_code == requests.codes.ok:
                response=response.json()
                quote_to_be_displayed=response[0]['quote']
                author=response[0]['author']
                quotes.author=author
                quotes.quote=quote_to_be_displayed
                quotes.last_updated=date.today()
                quotes.save()
            else:
                print("Error:", response.status_code, response.text)
        else:
            quote_to_be_displayed=quotes.quote
            author=quotes.author
        notice=Notice.objects.all()[::-1][:5]
        carousel_image=Carousel_image.objects.get()
        return render(request,"website/index.html",{
            "notice":notice,
            "carousel_image":carousel_image,
            "quote":quote_to_be_displayed,
            "author":author
        })
def principal_message(request):
    message = principals_message.objects.get()
    return render(request,"website/principal_message.html",
                  {'message':message,
                   })
def about_kv(request):
    return render(request,"website/about_kv.html")
def contact_us(request):
    return render(request,"website/contact_us.html")
def holidays(request):
    holiday=Holiday.objects.filter(category='holiday')
    summer_vacation=Holiday.objects.filter(category='summer_vacation')
    winter_vacation=Holiday.objects.filter(category='winter_vacation')
    autum_vacation=Holiday.objects.filter(category='autum_vacation')
    return render(request,"website/holidays.html",{
                      'holiday':holiday,
                      'summer_vacation':summer_vacation,
                      'winter_vacation':winter_vacation,
                      'autum_vacation':autum_vacation,
                  })
def tc_issued(request):
    if request.method == "POST":
        name=request.POST['name']
        if not name:
            tcs_issued=TC.objects.all()[::-1][:400]
            return render(request,"website/tc_issued.html",{
                'tc':tcs_issued
            })
        try:
            tcs_issued=TC.objects.filter(name__contains=f'{name}')[::-1][:400]
            return render(request,"website/tc_issued.html",{
            'tc_search':tcs_issued
        })
        except:
            tcs_issued=None  
            return render(request,"website/tc_issued.html",{
                'tc_search':tcs_issued
                })
    else:
        tcs_issued=TC.objects.all()[::-1][:400]
        return render(request,"website/tc_issued.html",{
            'tc':tcs_issued
        })
def vmc_members(request):
    vmc_members=vmc_member.objects.all()
    return render(request,"website/vmc_members.html",{
        'members':vmc_members
    })
def committees(request):
    committee=Committies.objects.all()
    return render(request,"website/committes.html",
                  {
                      "committee":committee
                  })
def notice(request):
    notice_data=Notice.objects.all()[::-1][:10]
    return render(request,"website/notice.html",{
        'notice_data':notice_data,
    })
def news_and_events(request):
    events = News_and_Events.objects.all()
    length=len(events)
    page=int(request.GET['page'])
    if page == 1:
        if events:
            events=events[:8]
            return render(request,"website/news_and_events.html",{
        'events':events,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    elif page == 2:
        if events[8:16]:
            events=events[8:16]
            return render(request,"website/news_and_events.html",{
        'events':events,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    elif page == 3:
        if events[16:24]:
            events=events[16:24]
            return render(request,"website/news_and_events.html",{
        'events':events,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))
def class_1(request):
    try:
        fee=class1.objects.get()
        return HttpResponseRedirect(f'{fee.file.url}')
    except:
        return render(request,"website/class_1.html")
def class_11(request):
    try:
        fee=class11.objects.get()
        return HttpResponseRedirect(f'{fee.file.url}')
    except:
        return render(request,"website/class_11.html")
def other_class(request):
    data=Admissions.objects.all()
    return render(request,"website/other_class.html",{
        "data":data
    })
def alumni(request):
    if request.method == 'POST':
        name=request.POST['name'] 
        phone=request.POST['phone']
        year_passed=request.POST['year']
        describe=request.POST['description']
        email=request.POST['email']
        send_mail(
            'Alumni form submitted',
            f"Name: {name} \nPhone Number:  {phone}  \nYear Passed:  {year_passed} \nCurrent Position: {describe} \nEmail: {email} \nAn Alumni form has been submitted to the website please contact the alumnus and add their data to the website \nThis is an auto-generated message",
            name,
            ['eoikvkathmandu@gmail.com']
        )
        return HttpResponseRedirect(reverse('index'))
    else:
        alumni_data=Alumni.objects.all()[::-1][:10]
        return render(request,"website/alumni.html",{
            'alumni_data':alumni_data,
        })
def achievements(request):
    achive=achievement.objects.all()[::-1][:10]
    return render(request,"website/achievement.html",{
        'achievements':achive
    })
def newsletter(request):
    news_letter=News_letter.objects.all()[::-1][:20]
    return render(request,"website/newsletter.html",{
        'news_letter':news_letter
    })
def members_list(request):
    members_list=member_list.objects.all()
    return render(request,"website/members_list.html",{
        'members':members_list
    })
def vacancy(request):
    vacany_post=None
    vacany_present=False
    vacany_post=Vacancy.objects.all()
    if vacany_post:
        vacany_present=True
    return render(request,"website/vacancy.html",{
        "vacancy":vacany_post,
        "vacant":vacany_present
    })
def gallery(request):
    gallery = News_and_Events.objects.all()
    length=len(gallery)
    page=int(request.GET['page'])
    if page == 1:
        if gallery:
            gallery=gallery[:8]
            return render(request,"website/gallery.html",{
        'gallery':gallery,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    elif page == 2:
        if gallery[8:16]:
            gallery=gallery[8:16]
            return render(request,"website/gallery.html",{
        'gallery':gallery,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    elif page == 3:
        if gallery[16:24]:
            gallery=gallery[16:24]
            return render(request,"website/gallery.html",{
        'gallery':gallery,
        'length':length,
        'page':page,
        'next':page+1,
        'previous':page-1,})
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))
def fees(request):
    fee=Fee_structure.objects.get()
    return HttpResponseRedirect(f'{fee.file.url}')
def show_event(request,pk):
    return render(request,'website/show_event.html',{
        "event":News_and_Events.objects.get(pk=pk)
    })