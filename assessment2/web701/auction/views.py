from django.shortcuts import render

def auction(request):
    return render(request, 'auction/auction.html')