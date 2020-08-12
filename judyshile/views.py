from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import send_mail
from articles.models import Contact , About,Article


def index(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)

        if form.is_valid():
            
            #getting values of the form field
            first_name = form.cleaned_data['firstname']
            last_name = form.cleaned_data['lastname']
            email_address = form.cleaned_data['email']
            mail_message = form.cleaned_data['message']
        
            #saving the contacts
            contact = Contact(firstName=first_name,lastname=last_name,email=email_address,message=mail_message)
            #sending the email
            send_mail(
                ''+first_name+''+last_name+''+email_address+'Hi Judy Im reaching you from leshi blog',
                mail_message,
                email_address,
                ['leshiblog@gmail.com'],
                fail_silently = False,
            )
            print (first_name,last_name,email_address,mail_message)
            return redirect('/')
    else:
        form = ContactForm()
    articles = Article.objects.all().order_by('date')[:3]
    abouts = About.objects.all()
    return render(request,'index.htm',{'form':form,'abouts':abouts,'articles':articles})