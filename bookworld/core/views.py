from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from .forms import signupform,loginform,book_category_form,available_book_form,buy_book_form,search_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import book_category,available_book,buy_book_model
from django.db.models import Q

# Create your views here.

# view function for home page
def home(request):
    return render(request,'core/home.html')

# view function for sign up form
def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/core/dashboard/')
    else:
        if request.method=="POST":
            fm=signupform(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,"You Have Successfuly Signed Up !!!")
        else:
            fm=signupform()
    return render(request,'core/signup.html',{'form':fm})


# view function for login form
def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/core/dashboard/')
    else:
        if request.method=="POST":
            fm=loginform(request=request,data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user !=None:
                    login(request,user)
                    return HttpResponseRedirect('/core/dashboard/')
        else:
            fm=loginform()
    return render(request,'core/login.html',{'form':fm})

# view function for logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/core/login/')
   


# view function for Dashboard 

def user_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users=User.objects.all()
            return render(request,'core/admindashboard.html',{'users':users})
        else:
            if request.method=="POST":
                searchform=search_form(request.POST)
                if searchform.is_valid():
                    req=searchform.cleaned_data['search']
                    allbooks=available_book.objects.filter(Q(title__icontains=req)|Q(author__icontains=req)|Q(category__icontains=req)|Q(publisher__icontains=req))
                    category=book_category.objects.all()
                    cnt=allbooks.count()
                    if cnt==0:
                        messages.warning(request,"No results Found !!")
                    return render(request,'core/searchresult.html',{'req':req,'allbooks':allbooks,'category':category})
                    
                    """if req is not None:
                        return render(request,'core/searchresult.html',{'searchform':searchform,'req':req})
                    else:
                        return HttpResponseRedirect('/core/dashboard/')"""
            else:
                searchform=search_form()
                category=book_category.objects.all()
                books=available_book.objects.all()[:25]
                return render(request,'core/userdashboard.html',{'category':category,'books':books,'searchform':searchform})
    else:
        return HttpResponseRedirect('/core/login/')
    return HttpResponseRedirect('/core/dashboard/')

# view function to delete user
def delete_user(request,id):
    pi=User.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/core/dashboard/')

# view function to edit user
def edit_user(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=signupform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Successfully Updated !!")
    else:
        pi=User.objects.get(pk=id)
        fm=signupform(instance=pi)
    return render(request,'core/updateuser.html',{'form':fm,'id':id})

# view function to show book category in admin panel
def book_category_admin_panel(request):
    books=book_category.objects.all()
    return render(request,'core/bookcategory.html',{'books':books})

# view function to delete user
def delete_book_category(request,id):
    pi=book_category.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/core/bookcategory/')

# view function to edit book category
def edit_book_category(request,id):
    if request.method=="POST":
        pi=book_category.objects.get(pk=id)
        fm=book_category_form(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Successfully Updated !!")
    else:
        pi=book_category.objects.get(pk=id)
        fm=book_category_form(instance=pi)
    
    return render(request,'core/updatebookcategory.html',{'form':fm,'id':id})

# view function to add book category
def add_book_category(request):
    if request.method=="POST":
        fm=book_category_form(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Book Category Successfully Added !!")
    else:
        fm=book_category_form()
    return render(request,'core/addbookcategory.html',{'form':fm})


# view function to show available books
def available_book_function(request):
    availablebooks=available_book.objects.all()
    return render(request,'core/availablebook.html',{'availablebooks':availablebooks})

# view function to delete avilable book
def delete_available_book(request,id):
    pi=available_book.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/core/availablebook/')

#  view function to edit available book
def edit_available_book(request,id):
    if request.method=="POST":
        pi=available_book.objects.get(pk=id)
        fm=available_book_form(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Successfully Updated !!")
    else:
        pi=available_book.objects.get(pk=id)
        fm=available_book_form(instance=pi)
    
    return render(request,'core/editavailablebook.html',{'form':fm})


#  view function to add book
def add_book(request):
    if request.method=="POST":
        fm=available_book_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Successfully Added !!")
    else:
        fm=available_book_form()
    
    return render(request,'core/addbook.html',{'form':fm})

# view function to buy book
def buy_book_function(request,id):
    if request.method=="POST":
        pi=available_book.objects.get(pk=id)
        fm=buy_book_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Thank You For Shopping ,Book Will Be Delivered Soon !!')
            #return render(request,'core/buybook.html')
    else:
        pi=available_book.objects.get(pk=id)
        fm=buy_book_form()
    return render(request,'core/buybook.html',{'form':fm,'pi':pi})

# view function to show ordered books and assign worker
def show_ordered_book(request):
    books=buy_book_model.objects.all()
    return render(request,'core/showbooks.html',{'books':books})

# view function to delete requests
def delete_request(request,id):
    pi=buy_book_model.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/core/showbook/')

# view function to assign the request to worker
def assign_request(request,id):
    pi=buy_book_model.objects.get(pk=id)
    fm=buy_book_form(instance=pi)
    return render(request,'core/assignwork.html',{'form':fm})

# viw function to select category on click user dashboard
def select_category(request,category):
    bookcategory=book_category.objects.all()
    allbooks=available_book.objects.filter(Q(title__iexact=category)|Q(author__iexact=category)|Q(publisher__iexact=category)|Q(category__iexact=category))
    return render(request,'core/selectedcategory.html',{'allbooks':allbooks,'category':category,'bookcategory':bookcategory})


# view function for contact us
def contact_us(request):
    return render(request,'core/contact.html')
    
