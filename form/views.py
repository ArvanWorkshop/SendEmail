from django.shortcuts import render,redirect
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from .models import Form
import smtplib


def home(request):
    return render(request, 'form/home.html')

def form(request):
    if request.method == 'POST':
        if request.POST['company'] and request.POST['add1'] and request.POST['add2'] and request.POST['city'] and request.POST['zipC'] and request.POST['state'] and request.FILES['image'] and request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['phone']:
            formadd = Form()
            formadd.company = request.POST['company']
            formadd.add1 = request.POST['add1']
            formadd.add2 = request.POST['add2']
            formadd.city = request.POST['city']
            formadd.zipC = request.POST['zipC']
            formadd.state = request.POST['state']

            formadd.image = request.FILES['image']
            formadd.first_name = request.POST['first_name']
            formadd.last_name = request.POST['last_name']
            formadd.email = request.POST['email']
            formadd.phone = request.POST['phone']
            formadd.save()

            # configure your email address
            # step1:
            email_user = 'aefefewf223@gmail.com'
            email_password = '123!@#qweDFG'
            email_send = 'bishwas19299@gmail.com'

            # step2:
            # https://myaccount.google.com/lesssecureapps
            # Allow less secure apps: ON (remember you must be on for sending email)

            subject = 'Partner From'
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject

            msg.attach(MIMEText('<html><body>' + "<h2>ArvanWorkshop Partner Informations</h2><hr>" + "<br><br>" + \
             "<h3>BASIC INFO</h3>" +"<strong>Company Name: </strong>" + formadd.company + \
             '<br><strong> Address1: </strong>' + formadd.add1 + '<br><strong> Address2: </strong>' + \
             formadd.add2 + '<br><strong> City: </strong>' + formadd.city + '<br><strong> Zip Code: </strong>' + \
             formadd.zipC +'<br><strong>State: </strong>'+ formadd.state +'<br>'+ \
            '<h3> Contact Info </h3> '+'<strong> First Name: </strong>'+ formadd.first_name + '<br><strong> Last Name: </strong>' + formadd.last_name + '<br><strong> Email: </strong>' + \
            formadd.email + '<br><strong> Mobile Number: </strong>' + formadd.phone + "</html></body>", 'html', 'utf-8'))

            # configure your own file path
            filename = 'C:/Users/Arvan Bishwas/PycharmProjects/SendingEmails' + formadd.image.url
            attachment  =open(filename,'rb')

            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+filename)

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)
            server.sendmail(email_user,email_send,text)
            server.quit()

            return redirect(home)
        else:
            return render(request, 'form/form.html',{'error':'All fields are required.'})
    else:
        return render(request, 'form/form.html')
