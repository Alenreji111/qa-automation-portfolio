from django.shortcuts import render

from django.http import JsonResponse , HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json

@csrf_exempt
def user_create(request):
    if request.method =="POST":
        data = json.loads(request.body)

    

        if 'name' not in data or 'email'not in data:
            return JsonResponse({
                "error":"please complete the requirment ",
            } ,status=400)


        user = User.objects.create(
            name = data["name"],
            email = data["email"]
        )
          
    

        return JsonResponse({
            "id":user.id ,
            "name": user.name ,
            "email":user.email 
        }, status=201)

                

    return JsonResponse({"error":"not correct url"}, status=404)

@csrf_exempt 
def user_details(request,user_id):

    if request.method == "GET":
        try:

            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return JsonResponse({
                "message":"user not found"
            }, status=404)

        return JsonResponse({
            "id":user.id,
            "name":user.name,
            "email":user.email
        }, status= 200)

    elif request.method == "PUT":
        data = json.loads(request.body)
        try :
            user = User.objects.get(id=user_id)
            
        except User.DoesNotExist:
            return JsonResponse({
                "error":"user is not exist"
            },status= 404)

        user.name = data["name"]
        user.email = data["email"]
        user.save()

        return JsonResponse({
            "id":user.id ,
            "name": user.name ,
            "email":user.email 
        },status=200)

    elif request.method == "DELETE":
        try :
            user = User.objects.get(id=user_id)

        except User.DoesNotExist:
            return JsonResponse({
                "error":"user not existed"
            }, status=404)


        user.delete()

        return HttpResponse({}, status=204)


    return JsonResponse({
        "error":"not allowed method"
    }, status=404)








    



    
# Create your views here.




