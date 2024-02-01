from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import pickle
from joblib import load
import pandas as pd
from .models import PredResults
from .models import Contact

def home(request):
    return render(request, 'website.html')
def predict(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')

        contact.name=name
        contact.email=email
        contact.subject=subject

        contact.save()
        #return HttpResponse("thanks")
        
    return render(request, 'contact.html')

def question(request):
    return render(request, 'questions.html')


def jls_extract_def():
    
    return 


def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Age = float(request.POST.get('Age'))
        Object_Rating = int(request.POST.get('Object_Rating'))
        BodyPart_Rating = int(request.POST.get('BodyPart_Rating'))
        Gender = request.POST.get('Gender')
        Delivery = request.POST.get('Delivery')
        Birth_Injury = (request.POST.get('Birth_Injury'))
        Jaundice = request.POST.get('Jaundice')
        Cousin_Marriage = request.POST.get('Cousin_Marriage')
        Q1 = request.POST.get('Q1')
        Q2 = request.POST.get('Q2')
        Q3 = request.POST.get('Q3')
        Q4 = request.POST.get('Q4')
        Q5 = request.POST.get('Q5')
        Q6 = request.POST.get('Q6')
        Q7 = request.POST.get('Q7')
        Q8 = request.POST.get('Q8')
        Q9 = request.POST.get('Q9')
        Q10 = request.POST.get('Q10')
        Q11 = request.POST.get('Q11')

        if Gender == "male":
            gender=1
        else:
            gender=0

        if Delivery == "normal":
            delivery=1
        else:
            delivery=0

        if Birth_Injury == "yes":
            birth_Injury=1
        else:
            birth_Injury=0

        if Jaundice == "yes":
            jaundice=1
        else:
            jaundice=0

        if Cousin_Marriage == "yes":
            cousin_marriage=1
        else:
            cousin_marriage=0

        if Q1 == "no":
            q1=0
        else:
            q1=1

        if Q2 == "yes":
            q2=1
        else:
            q2=0

        if Q3 == "no":
            q3=0
        else:
            q3=1

        if Q5 == "no":
            q5=0
        else:
            q5=1
        
        if Q7 == "no":
            q7=0
        else:
            q7=1

        if Q8 == "yes":
            q8=1
        else:
            q8=0

        if Q9 == "no":
            q9=0
        else:
            q9=1

        if Q10 == "no":
            q10=0
        else:
            q10=1

        if Q4 == "aggressive":
            q4=0
        elif Q4=="cry":
            q4=1
        elif Q4=="good":
            q4=2
        elif Q4=="no response":
            q4=3
        else :
            q4=4


        if Q6 == "cry":
            q6=0
        elif Q6=="gesture":
            q6=1
        elif Q6=="push":
            q6=2
        elif Q6=="shake their head":
            q6=3
        else :
            q6=4


        if Q11 == "ball":
            q11=0
        elif Q11=="car":
            q11=1
        elif Q6=="mobile":
            q11=2
        elif Q11=="not specific":
            q11=3
        elif Q11=="spoon" :
            q11=4
        else:
            q11=5
        
        model = load('linmodel.joblib')
        # Make prediction
        result = model.predict([[Age, Object_Rating, BodyPart_Rating, gender, delivery, birth_Injury, jaundice, cousin_marriage, q1, q2, q3, q4, q5, q6,
                                 q7, q8, q9, q10, q11]])

        classification = result[0] 

        PredResults.objects.create(Age=Age, Object_Rating=Object_Rating, BodyPart_Rating=BodyPart_Rating, Gender=Gender, Delivery=Delivery, Birth_Injury=Birth_Injury,
                                   Jaundice=Jaundice,Cousin_Marriage=Cousin_Marriage, Q1=Q1, Q2=Q2, Q3=Q3, Q4=Q4, Q5=Q5,
                                   Q6=Q6, Q7=Q7, Q8=Q8, Q9=Q9, Q10=Q10, Q11=Q11, classification=classification)

        return JsonResponse({'result': classification, 'Age': Age,'Object_Rating':Object_Rating,
                             'BodyPart_Rating':BodyPart_Rating, 'Gender': Gender, 'Delivery': Delivery,
                             'Birth_Injury': Birth_Injury, 'Jaundice': Jaundice, 'Cousin_Marriage': Cousin_Marriage,
                             'Q1': Q1, 'Q2': Q2, 'Q3': Q3, 'Q4': Q4, 'Q5': Q5, 'Q6': Q6, 'Q7': Q7, 'Q8': Q8, 'Q9': Q9,
                             'Q10': Q10, 'Q11': Q11}, safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)
