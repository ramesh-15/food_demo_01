from django.shortcuts import render, HttpResponseRedirect
from .forms import logform, regform, userform, donateform, contactform
from .models import Users_donations, Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.
def donar_home(request):
    return render(request, 'Donar_home.html')


def NGO_home(request):
    data = Users_donations.objects.filter(flag=False)
    return render(request, 'NGO_home.html', {'data': data})
    # for i in data:
    #     pt = Users_donations.objects.get(food_name=i)
    #     print(pt.flag )
    #     if pt.flag == 'Fasle':
    #         print(pt.flag,type(pt.flag))
    # print(data,type(data),data[0],data[1])
    # temp = FoodSerializer(data,many=True)
    # for i in range(len(temp.data)):
    #     if temp.data[i]['flag']==True:
    # print(temp.data[0]['flag'],len(temp.data))




def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        fm = contactform(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['name']
            fmail = fm.cleaned_data['email']
            fphone = fm.cleaned_data['phone']
            fsub = fm.cleaned_data['subject']
            fmsg = fm.cleaned_data['message']
            user = Contact(name=fname, email=fmail, phone=fphone, subject=fsub, message=fmsg)
            user.save()
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'contact.html', {'data': fm})
    else:
        fm = contactform()
        return render(request, 'contact.html', {'data': fm})


def register(request):
    if request.method == 'POST':
        f = regform(request.POST)
        if f.is_valid():
            f.save()
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'reg.html', {'data': f})
    else:
        f = regform()
        return render(request, 'reg.html', {'data': f})


def loginview(request):
    if request.method == 'POST':
        f = logform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['username']
            fpwd = f.cleaned_data['password']
            user = authenticate(request, username=fname, password=fpwd)
            if user is not None:
                login(request, user)
                if user.is_Donar:
                    return HttpResponseRedirect('/donar_home')
                elif user.is_NGO:
                    return HttpResponseRedirect('/NGO_home')


    else:
        f = logform()
        return render(request, 'log.html', {'data': f})


def logoutpage(request):
    logout(request)
    return render(request, 'home.html')


def setpwd(request):
    if request.method == "POST":
        print(request.user)
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'Password Changed Successfully')
            return HttpResponseRedirect('/login')
        else:
            return render(request, 'changepwd.html', {'data': fm})
    else:
        fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepwd.html', {'data': fm})


def edituser(request):
    if request.method == 'POST':
        f = userform(request.POST, instance=request.user)
        if f.is_valid():
            f.save()
            if request.user.is_Donar:
                return HttpResponseRedirect('/donar_home')
            elif request.user.is_NGO:
                return HttpResponseRedirect('/NGO_home')
    else:
        f = userform(instance=request.user)
        return render(request, 'editprofile.html', {'data': f})


# donate food
def donatefood(request):
    if request.method == 'POST':
        f = donateform(request.POST)
        if f.is_valid():
            fname = f.cleaned_data['food_name']
            ftype = f.cleaned_data['food_type']
            fqty = f.cleaned_data['quantity']

            fcont = f.cleaned_data['donar_contact']
            fpic = f.cleaned_data['food_pick_up']
            fpin = f.cleaned_data['pincode']
            user = Users_donations(food_name=fname, food_type=ftype, quantity=fqty, donar_contact=fcont,
                                   food_pick_up=fpic, pincode=fpin)
            user.save()
            return HttpResponseRedirect('/donar_home')
    else:
        f = donateform()
        return render(request, 'donatefood.html', {'data': f})


#  view food of NGO

def NGOrequest(request, id):
    fr = Users_donations.objects.get(id=id)
    fr.flag='True'
    fr.save()
    ft = Users_donations.objects.get(id=id)
    ft.username=request.user
    ft.save()

    return HttpResponseRedirect('/Cart_NGO')
    # print(id)
    # data = Users_donations.objects.get(id=id)
    # stu = FoodSerializer(data)
    # print(stu.data)
    # print(stu.data['id'])
    #
    # var = {
    #     'food_id': stu.data['id'],
    #     'username': request.user,
    #     'food_name': stu.data['food_name'],
    #     'pickup_point': stu.data['food_pick_up'],
    #     'donar_contact': stu.data['donar_contact']
    #
    # }
    # if request.method == ('POST'):
    #     fm = NGO_request(request.POST or None)
    #     if fm.is_valid():
    #         exist = food_requests.objects.get(id=id)
    #         print(exist)
    #
    #         if not exist:
    #             messages.success(request, 'requested Successfully... ')
    #             fg = Users_donations.objects.get(id=id)
    #             print(fg.flag)
    #             fg.flag = 'True'
    #             print(fg.flag)
    #             fm.save()
    #
    #             # dele = Users_donations.objects.get(id=id)
    #             # dele.delete()
    #             return HttpResponseRedirect('/NGO_home')
    #         else:
    #             messages.error(request, 'already requested...')
    #             return render(request, 'NGO_request.html', {'data': fm})
    # else:
    #     fm = NGO_request()
    #     return render(request, 'NGO_request.html', {'data': fm})


# NGO_ view request

def Cart_NGO(request):
    print(request.user)
    data = Users_donations.objects.filter(flag=True)
    return render(request, 'NGO_cart.html', {'data': data})


def Cancel_NGO(request, id):

    fr = Users_donations.objects.get(id=id)
    fr.flag = 'True'
    # print(dt.food_id)

    return HttpResponseRedirect('/Cart_NGO')


# search
# def search(request):
#     query = request.GET.get('query', '')
#     products = Users_donations.objects.filter(Q(product_name__icontains=query) | Q(product_description__icontains=query))
#     data=[]
#     for i in products:
#         prodDetails={}
#         prodDetails["product_name"] =i.product_name
#         prodDetails["product_id"] =i.product_id
#         prodDetails["product_description"] =i.product_description
#         prodDetails["product_price"] =i.product_price
#         pid = i.product_id
#         vendobj = Vendor.objects.get(vendor_id=i.vendor_id)
#         prodDetails["vendobj"]=vendobj.vendor_id
#         try:
#             imgobj = ProductImages.objects.filter(img_product=pid).first()
#         except:
#             imgobj = ProductImages.objects.get(img_product=38).first()
#             prodDetails["imgobj"] =imgobj
#             data.append(prodDetails)
#     return render(request, 'UserAccounts/search.html', {'query': query,'data':data})







