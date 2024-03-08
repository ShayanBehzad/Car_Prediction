from django.shortcuts import render, redirect
from django.http import HttpResponse,  HttpResponseNotFound
from django.views.decorators.csrf import csrf_protect
from django.core import serializers
from django.http import HttpResponseBadRequest, JsonResponse
from django.urls import reverse
from django.contrib import messages
from polls.ML import m_206, m_l90, m_pride

# Create your views here.
cars = ['پژو، 206', 'L90', '141 پراید', '132 پراید','131 پراید', ' پراید هاچ بک', 'پراید صندوق دار', '151 پراید', '111 پراید']

def index(request):
    context = {'cars':cars}
    return render(request, "polls/home.html",context)

@csrf_protect
def handle_choice(request):
    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        user_trim = request.POST.get('trim')
        user_mileage = request.POST.get('mileage')
        user_model = request.POST.get('model')
        

        print("the user choice: " + str(user_choice) + ' ' + str(user_trim) + ' ' + str(user_mileage) + ' ' + str(user_model))
            
        if not user_choice or not user_trim or not user_mileage or not user_model:
            messages.warning(request, 'Please fill in all the blanks')
            return redirect('/#info')
        

        if int(user_choice) == 1:
            request.session['pred'] = m_206(int(user_mileage) / 1000, int(user_model) - 1380, int(user_trim) * 100)[0]
            request.session['acc'] = m_206(int(user_mileage) / 1000, int(user_model) - 1380, int(user_trim) * 100)[1]
            return redirect('prediction')  # Redirect to the 'prediction' view
        elif int(user_choice) == 2:
            request.session['pred'] = m_l90(int(user_mileage) / 1000, int(user_model) - 1385, int(user_trim) * 100)[0]
            request.session['acc'] = m_l90(int(user_mileage) / 1000, int(user_model) - 1385, int(user_trim) * 100)[1]
            return redirect('prediction')  # Redirect to the 'prediction' view
        elif int(user_choice) >= 3:
            request.session['pred'] = m_pride(int(user_mileage) / 1000, int(user_model) - 1372, (int(user_choice) + int(user_trim)) * 10)[0]
            request.session['acc'] = m_pride(int(user_mileage) / 1000, int(user_model) - 1372, (int(user_choice) + int(user_trim)) * 10)[1]
            return redirect('prediction')  # Redirect to the 'prediction' view

    return render(request, "polls/home.html")



def prediction(request):

    return render(request, "polls/pred.html",{'pred':request.session.get('pred'),'acc':request.session.get('acc')})



