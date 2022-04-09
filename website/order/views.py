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
        # content = request.POST.get('content')
        #print(to,content)
            send_mail(
                'Order Conform',
                'Your is placed successfully',
                settings.EMAIL_HOST_USER,
                [to]

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
