from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from .models import user_registration,product,Cart
# from django.contrib.auth import authenticate,login
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"index.html")

# def register(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=User.objects.create_user(username=username,password=password)
#         if user:
#             Profile.objects.create(user=user)
#             return redirect('user_login')
#         else:
#             return render(request,"registration.html")
#     return render(request,"registration.html")

# def user_login(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('user_home')
#         else:
#             return HttpResponse("invalid username or password!!")

#     return render(request,"login.html")


def registration(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        obj=user_registration.objects.create(
            username=uname,
            password=upass
        )
        if obj:
            return render(request,"login.html")
        else:
            return render(request,"registration.html")

    return render(request,"registration.html")

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        upass=request.POST.get('password')
        user=user_registration.objects.filter(username=uname,password=upass).first()
        if user:
            request.session['idl']=user.id
            request.session['eml']=user.username
            request.session['psd']=user.password
        
            if user.type=="admin":
                return render(request,"admin/adminHome.html")
            else:
                return render(request,"user/userHome.html")
        else:
            msg="invalid Credentials!!"
            return render(request,"login.html",{"error":msg})
    return render(request,"login.html")


def user_home(request):
    return render(request,"user/userHome.html")

def adminHome(request):
    return render(request,"admin/adminHome.html")

def add_product(request):
    if request.method=="POST":
        pnm=request.POST.get('pname')
        img=request.FILES.get('pimg')
        des=request.POST.get('pdes')
        prc=request.POST.get('price')
        obj=product.objects.create(
            pdt_name=pnm,
            image=img,
            description=des,
            price=prc
        )
        # return redirect ('view_mens')
    return render(request,"admin/product.html")

def view_product(request):
    obj=product.objects.all()
    return render(request,"user/view_products.html",{"data":obj})

def view_users(request):
    obj=user_registration.objects.all()
    return render(request,"admin/user.html",{"data":obj})

def edit_user(request):
    idn=request.GET.get('idno')
    obj=user_registration.objects.filter(id=idn)
    if request.method=="POST":
        usr=request.POST.get('usrnm')
        ids=request.POST.get('idno')
        psd=request.POST.get('psw')
        obb=user_registration.objects.filter(id=ids)
        obb.update(
            username=usr,id=ids,password=psd
        )
        return redirect('/usr')
    return render(request,"admin/edit_user.html",{"data":obj})

def delete_user(request):
    idn=request.GET.get('idno')
    obj=user_registration.objects.filter(id=idn)
    obj.delete()
    return render('/view_user')

def mens_product(request):
    obj=product.objects.filter(category='men')
    return render(request,"user/view_products.html",{"data":obj ,"title":"Mens"})

def womens_product(request):
    obj=product.objects.filter(category='women')
    return render(request,"user/view_products.html",{"data":obj ,"title":"Womens"})

def kids_product(request):
    obj=product.objects.filter(category='kids')
    return render(request,"user/view_products.html",{"data":obj ,"title":"Kids"})

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        user_id = request.session.get('idl')

        if not user_id:
            return redirect('login')  

        user = user_registration.objects.get(id=user_id)
        pdt = product.objects.get(id=product_id)
 
        # check if already in cart
        cart_item = Cart.objects.filter(user=user, product=pdt).first()

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
        else:
            Cart.objects.create(user=user, product=pdt, quantity=1)

        return redirect('view_cart')
    
def view_cart(request):
    user_id = request.session.get('idl')
    user = user_registration.objects.get(id=user_id)

    cart_items = Cart.objects.filter(user=user)

    return render(request, "user/cart.html", {"cart": cart_items})

def remove_from_cart(request):
    if request.method == "POST":
        cart_id = request.POST.get('cart_id')
        user_id = request.session.get('idl')

        try:
            cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
            cart_item.delete()
        except Cart.DoesNotExist:
            pass

        return redirect('view_cart')