from django.shortcuts import render
from googletrans import Translator
# Create your views here.

def home(request):
    if request.method == 'POST':
        translator = Translator()
        txt = request.POST['text']
        out = translator.translate(txt, dest='bn')
        answer = out.text
        return render(request,'index.html',{'txt':answer}) 
    return render(request, 'index.html')