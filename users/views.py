from .forms import SignUpForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login as auth_login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# Create your views here.
@login_required
def index(request):
    user = request.user
    try :
        y_typ=Category.objects.get(slug=0,typ="سنوي")
    except:
        y_typ=Category.objects.create(slug=0,typ="سنوي")
    
    try :
        m_typ=Category.objects.get(slug=1,typ="شهري")
    except:
        m_typ=Category.objects.create(slug=1,typ="شهري")
    # cats = Category.objects.all()
    # for i in cats
    # membershib = get_object_or_404(Membershib,account=user)
    membershib = Membershib.objects.filter(account=user)
    has_membershib:bool =len(membershib)>0 
    print(has_membershib)
    if request.method == "POST":
        # print()
        option = request.POST.get("opt")
        # m_type = Category.objects.get()
        if option=="y":
            Membershib.objects.create(account=user,m_type=y_typ)        
        if option=="m":
            Membershib.objects.create(account=user,m_type=m_typ)        
        messages.add_message(request, messages.SUCCESS, "تم الاشتراك بنجاح ")
        membershib = Membershib.objects.filter(account=user)
        print(membershib,"ss")
        has_membershib:bool =len(membershib)>0 
    c={
        "known":has_membershib,
        
    }
    if has_membershib:
        c["membershib"]=membershib[0]
    return render (request=request,template_name="index.html",context=c)




@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name','last_name','email',)
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user










def signup(request):
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')

    return render(request,'signup.html',{'form':form})
