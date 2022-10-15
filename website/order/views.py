from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import mysql.connector as sql
fn=''
ln=''
g=''
em=''
pn=''
it=''
qn=''
ad=''
pr=''
gr=''
mr=''

# Create your views here.

def orderaction(request):
    global fn,ln,g,em,pn,it,qn,ad
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="root", database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             if key=="first_name":
                 fn=value
             if key=="last_name":
                 ln=value
             if key=="gender":
                 g=value
             if key=="email":
                 em=value
             if key=="phone_no":
                 pn=value
             if key=="items":
                 it=value
             if key=="quantity":
                 qn=value
             if key=="address":
                 ad=value

        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,g,em,pn,it,qn,ad)
        cursor.execute(c)
        m.commit()
        if request.method == "POST":
            to = request.POST.get('email')
            fno = request.POST['first_name']
            lna = request.POST['last_name']
            eml= request.POST['email']
            phn =request.POST['phone_no']
            itm= request.POST['items']
            qun= request.POST['quantity']
            add=request.POST['address']
        # content = request.POST.get('content')
        #print(to,content)
            send_mail(
                'Order Confirmed',
                'First Name:-'+fno+' Last Name:-'+lna+' Email:-'+eml+' Phone No:-'+phn+' Items:-'+itm+ ' Quantity:-'+qun+' Address:-'+add,
                settings.EMAIL_HOST_USER,
                [to,'shashankdeep.647@gmail.com']

            )
        
            return render(
                request,
                'order_page.html',
                {
                    'title': 'Send an email',
                }
            )
        else:    
            return render(
                    request,
                    'order_page.html',
                    {
                        'title': 'Send an email',
                    }
                )

    return render(request, 'order_page.html')    


def home(request):
    return render(request, 'home.html')

def home1(request):
    return render(request, 'home.html')    

def booked(request):
    return render(request, 'booked.html')

def contact(request):
    if request.method == "POST":
        name= request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'you Some one want Contact',
            'Name :-' + name +' Email :-' + email + ' Message :-' + message,
            email,
            ['shashankdeep.647@gmail.com'],
        )

        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')        

def sell(request):
    return render(request, 'index1.html')

def register(request):
    global fn,ln,em,pr,gr,mr,pn
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", passwd="root", database='registration')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
             if key=="first_name":
                 fn=value
             if key=="last_name":
                 ln=value
             if key=="email":
                 em=value
             if key=="page_rate":
                 pr=value
             if key=="glass_rate":
                 gr=value
             if key=="metal_rate":
                 mr=value
             if key=="phone_no":
                 pn=value
            

        c="insert into register Values('{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,em,pr,gr,mr,pn)
        cursor.execute(c)
        m.commit()
    return render(request, 'register.html')             
