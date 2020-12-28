from django.shortcuts import render
from .models import *
from django.utils.safestring import mark_safe
import markdown
from .forms import MessageForm
from django.http import HttpResponseRedirect
import telepot

token = '1212716658:AAFMEBth1fyC-miiafHV8rSIRwNaMgMAGEE'
my_id = -348899178
telegramBot = telepot.Bot(token)


def send_message(text):
    telegramBot.sendMessage(-348899178, text, parse_mode="Markdown")


def markdown_format(text):
    return mark_safe(markdown.markdown(text))


def base(request):
    message = Message.objects.all()
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            company_message = "*ЗАЯВКА APPLE*:" + "\n" + "*ФИО*: " + str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone) + \
                              "\n" + "*EMAIL*: " + str(email) + "\n" + "*ГОРОД*: " + str(address)
            send_message(company_message)
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()

    return render(request, 'summary/index.html', {
        'form': form,
    })


def design(request):
    return render(request, 'summary/design.html', {

    })

