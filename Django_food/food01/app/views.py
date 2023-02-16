from django.shortcuts import render,HttpResponseRedirect
from .forms import FoodRequestForm
from .models import Users_donations,food_requests
from .serializers import FoodSerializer
from django.contrib import messages

# Create your views here.

def NGOHome(request):
    fm = Users_donations.objects.filter(flag=False)
    return render(request,'NGOHome.html',{"data":fm})
# def DonarDonate(request):
#     if request.method == 'POST':
#         fm = food_requests(request.POST or None)

def FoodRequest(request,id):
    fm = Users_donations.objects.filter(id=id).update(flag=True)
    return render(request,'NGOHome.html',{'data':fm})
    # data = Users_donations.objects.get(id=id)
    # stu = FoodSerializer(data)
    # print(stu.data)
    # print(stu.data['id'])
    #
    # var = {
    #     'food_id':stu.data['id'],
    #     'username':request.user,
    #     'food_name':stu.data['food_name'],
    #     'pickup_point':stu.data['food_pick_up'],
    #     'donar_contact':stu.data['donar_contact']
    #
    # }
    # if request.method =='POST':
    #     fr = FoodRequestForm(request.POST)
    #     if fr.is_valid():
    #         fg = Users_donations.objects.get(id=id)
    #         print(fg.flag)
    #         fg.flag = 'True'
    #         print(fg.flag)
    #         fg.save()
    #         fr.save()
    #         messages.success(request, 'requested Successfully... ')
    #         return HttpResponseRedirect('/NGOHome')
    #         # else:
    #         #     messages.error(request,'already requested...')
    #         #     return render(request,'NGO_home.html'})
    # else:
    #     fr = FoodRequestForm(var)
    #     return render(request, 'FoodRequest.html',{'data':fr})
def Cart_NGO(request):
    print(request.user)

    # data = food_requests.objects.filter(username=request.user )

    cl = Users_donations.objects.filter(flag=True)
    return render(request,'NGO_cart.html',{'data':cl})





def FoodCancel(request,id):
    Users_donations.objects.filter(id=id).update(flag=False)

    return HttpResponseRedirect('/Cart_NGO')
    # print(food_id,type(food_id))
    # stu = Users_donations.objects.all()
    # # print(stu)
    # serializer = FoodSerializer(stu, many=True)
    #
    # # print(list(serializer.data))
    # for i in serializer.data:
    #
    #     temp =list(i.items())
    #     print(temp[0],type(temp))
    #     if int(temp[0][1])==food_id:
    #         print(food_id,temp[i])
    #     # else:
    #     #     print('no')

    #

