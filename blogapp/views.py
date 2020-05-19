from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blogapp.forms import SignupForm,uploadform
from blogapp.models import upload
from django.conf import settings
from django.core.mail import send_mail
# Create your views here

def base(request):
    return render(request,'blogapp/base.html')
def home(request):
    return render(request,'blogapp/home.html')
@login_required
def viewsblog(request):
    return render(request,'blogapp/viewsblog.html')
@login_required
def postblog(request):
    return render(request,'blogapp/postblog.html')
def Signuppage(request):
    signupform=SignupForm();
    mydict={'signupform':signupform}
    if request.method=='POST':
        signupform=SignupForm(request.POST);
        if signupform.is_valid():
            user=signupform.save();
            user.set_password(user.password)
            user.save()
            #mydict.update({'msg':'Registered Successfully'})
            subject="Welcome mail"
            message="Welcome "+user.email+", you are registered"
            recipient_list=[user.email]
            email_from=settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Registered Successfully'})
    return render(request,'blogapp/Signup.html',context=mydict)
@login_required
def uploadview(request):
    uploadf=uploadform()
    mydict={'uploadform':uploadf}
    if request.method=="POST":
        uploadf=uploadform(request.POST,request.FILES);
        if uploadf.is_valid():
            data=uploadf.save(commit=False)
            data.author=request.user
            data.save()
            mydict.update({'msg':'Data saved Successfully'})
            mydict={'uploadform':uploadf}
    return render(request,'blogapp/upload.html',context=mydict)
@login_required
def viewFilesview(request):
    images=upload.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewfiles.html',{'images':images})
def Detailview(request,pid):
    images=upload.objects.get(id=pid)
    return render(request,'blogapp/detailview.html',{'images':images})

def Deleteproductview(request,pid):
    images=upload.objects.get(id=pid)
    images.delete();
    images=upload.objects.all().order_by('-upload_date')
    return render(request,'blogapp/viewfiles.html',{'images':images,'msg':'product deleted'})
