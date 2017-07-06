from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import auth
from django.views.decorators import csrf
from app.forms import (
    UserRegisterForm,
    UserLoginForm,
    AdvertForm,
    )
from django.contrib.auth.models import User
from app.models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime,date
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import (
	authenticate,
	login,
	logout
)



# Create Your Views Here

@login_required
def index(request):
    title = 'my custom'
    return render(request, 'index.html', {'title':title})

@login_required
def Computer_Science(request):
    q = Computer_Science_Quiz_Beginners.objects.order_by('?')[:1]
    return render(request,'test/Computer_Science.html',{'q':q})
    # request.session['fav_color'] = 'blue'
    # fav_color = request.session['fav_color']
    # del request.session['%!7_4y2ppvx_q2^w!y&51q0!v=e5$9tl+(5&*4i$14na$q2ezy']

@login_required
def Computer_Science_Options(request):
    return render(request,'test/Computer_Science_Options.html')


@login_required
def Networking_Options(request):
    return render(request,'test/Networking_Options.html')


@login_required
def Linux_Options(request):
    return render(request,'test/Linux_Options.html')

@login_required
def Electronic_Options(request):
    return render(request,'test/Electronic_Options.html')

@login_required
def Computer_Science_Intermediate(request):
    q = Computer_Science_Quiz_Intermediate.objects.order_by('?')[:1]
    return render(request,'test/Computer_Science_Intermediate.html',{'q':q})

@login_required
def Computer_Science_Advance(request):
    q = Computer_Science_Quiz_Advance.objects.order_by('?')[:1]
    return render(request,'test/Computer_Science_Advance.html',{'q':q})



@login_required
def Networking(request):
    q = Networking_Quiz_Beginners.objects.order_by('?')[:1]
    return render(request,'test/Networking.html',{'q':q})


@login_required
def Networking_Intermediate(request):
    q = Networking_Quiz_Intermediate.objects.order_by('?')[:1]
    return render(request,'test/Networking_Intermediate.html',{'q':q})


@login_required
def Networking_Advance(request):
    q = Networking_Quiz_Advance.objects.order_by('?')[:1]
    return render(request,'test/Networking_Advance.html',{'q':q})

@login_required
def Linux(request):
    q = Linux_Quiz_Beginners.objects.order_by('?')[:1]
    return render(request,'test/Linux.html',{'q':q})


@login_required
def Linux_Intermediate(request):
    q = Linux_Quiz_Intermediate.objects.order_by('?')[:1]
    return render(request,'test/Linux_Intermediate.html',{'q':q})


@login_required
def Linux_Advance(request):
    q = Linux_Quiz_Advance.objects.order_by('?')[:1]
    return render(request,'test/Linux_Advance.html',{'q':q})



@login_required
def Electronic_Principal(request):
    q = Electronic_Principal_Quiz.objects.order_by('?')[:1]
    return render(request,'test/Electronic_Principal.html',{'q':q})


@login_required
def Solution(request):
    r="Right Answer"
    w="Wrong Answer"	
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/CS/')
#        if(l):
#            return JsonResponse(r,safe=False)
#        else:
#            return JsonResponse(w,safe=False)


@login_required
def SolutionCSI(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/CSI/')


@login_required
def SolutionCSA(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/CSA/')


@login_required
def SolutionNWA(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/NWA/')


@login_required
def SolutionNWI(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/NWI/')

@login_required
def SolutionNW(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/NW/')

@login_required
def SolutionLX(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/LX/')


@login_required
def SolutionLXI(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/LXI/')


@login_required
def SolutionLXA(request):
    r="Right Answer"
    w="Wrong Answer"    
    if 'an' in request.POST and request.POST['an']:
        obj = request.POST['an']
        x = Stored_Answer(answer=obj)
        x.save()
        l = Correct.objects.filter(answer__icontains=obj)
    return HttpResponseRedirect('/LXA/')


@login_required
def compare(request):
    score = 0
    x = Correct.objects.all()
    y = Stored_Answer.objects.all()
    for n in range(0,len(x)):
        for m in range(0,len(y)):
            if x.answer[n] == y.answer[m]:
                score = score + 1
            m = m + 1
        n = n + 1
    return render(request, "test/compare.html", {score:"score"})


def login_view(request):
    print(request.user.is_authenticated())
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request,'index.html')
    return render(request, "login.html", {"form":form, "title":title})



def register_view(request):
    print(request.user.is_authenticated())
   
    form = UserRegisterForm(request.POST, request.FILES or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        im = form.cleaned_data.get('image')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return render(request, 'register_sucessfull.html',{})
    
    context = {
        "form": form,
        
    }
    return render(request, 'register.html', context)



def logout_view(request):
    logout(request)
    return render(request, 'logout.html')




def sessionss(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    else:
        request.session.delete() 
    return HttpResponse(request.session.session_key)
        


# To get current user id
@login_required
def Current_user_id(request):
    current_user = request.user
    return HttpResponse(current_user.id)



# def ToDoForm(request):
#     if request.method == 'POST':
#         form = ToDoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('uts working')
#         else:
#             form = ToDoForm()
#             return render(request, 'forms.html', {'form':form})

# from django.contrib.sessions.models import Session
# from django.contrib.auth.models import User
# session_key = '8cae76c505f15432b48c8292a7dd0e54'
# session = Session.objects.get(session_key=session_key)
# session_data = session.get_decoded()
# print session_data
# uid = session_data.get('_auth_user_id')
# user = User.objects.get(id=uid)




import json
from django.shortcuts import *
from django.template import RequestContext

# def advert(request):
#     if request.method == "POST":
#         form = AdvertForm(request.POST)

#         message = 'something wrong!'
#         if(form.is_valid()):
#             print(request.POST['title'])
#             message = request.POST['title']

#         return HttpResponse(json.dumps({'message': message}))

#     return render_to_response('forms.html',
#             {'form':AdvertForm()}, RequestContext(request))


def advert(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            form = AdvertForm()      
            return render(request, 'ajax.html',{'form':form}) 
