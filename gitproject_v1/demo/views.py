from django.shortcuts import render

def top_page(request):
    return render(request, 'demo/top_page.html')

def nakabayashi(request):
    return render(request, 'demo/nakabayashi.html')

def takeuti(request):
    return render(request, 'demo/takeuti.html')

def yamada(request):
    return render(request, 'demo/yamada.html')

def ogasawara(request):
    return render(request, 'demo/ogasawara.html')
 
# Create your views here.
