from django.shortcuts import render,redirect
from .models import Userdata,Product,Cart,Payment
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request,method = ['GET','POST']):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')

        user=Userdata.objects.filter(email=email) 

        if user:
            messages.info(request,'User is already exists')
        elif password1 != password2:
            messages.info(request,'Passwords did not match')
        else:
            Userdata.objects.create(email=email,password=password1)       
            return render(request,'login.html')            
    
    return render(request,'signup.html')

def login_page(request,method = ['GET','POST']):
    if request.method == 'POST':
        email = request.POST.get('email')
        password =request.POST.get('password')
        users=Userdata.objects.filter(email=email,password=password)
        
        if users.exists():
            request.session["email"]=email
            return redirect('/main/')
        else:
            messages.info(request,'Email and password is incorrect')
            return render(request,'login.html')         
                          

    return render(request,'login.html')


def main(request):
    email=request.session["email"]
    products=Product.objects.all()
    return render(request,'main.html',{'products':products,'email':email})

def cart(request,id):
    email=request.session["email"]
    user=Userdata.objects.get(email=email)
    prod=Product.objects.get(id=id)

    cart_item , created = Cart.objects.get_or_create(user=user,product=prod)

    if not created:
        cart_item.quantity+=1
        cart_item.save()
    return redirect('/view_cart/') 


def view_cart(request):
    email=request.session["email"]
    user=Userdata.objects.get(email=email)
    cart_item = Cart.objects.filter(user=user)
    total_prize = sum(item.product.dcost*item.quantity for item in cart_item)
    return render(request,'cart.html',{'cart_item':cart_item,'total_prize':total_prize})


def billing(request):
    email=request.session["email"]
    total_prize=request.GET.get('amount') 

    return render(request,'billing.html',{'total_prize':total_prize,'email':email})

def payment(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        username=request.POST.get('username')
        address=request.POST.get('address')
        country=request.POST.get('country')
        state=request.POST.get('state')
        zipcode=request.POST.get('zip')
        paymentMethod=request.POST.get('paymentMethod')
        totalamount=request.POST.get('total_prize')
        Payment.objects.create(firstName=firstName,lastName=lastName,username=username,address=address,country=country,state=state,zipcode=zipcode,paymentMethod=paymentMethod,totalamount=totalamount)
        return render(request,'success.html')
            
          
     

def logout(request):
    return render(request,'index.html') 



