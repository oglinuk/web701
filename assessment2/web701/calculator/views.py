from django.shortcuts import render

def calculator(request):
    if request.method == 'POST':
        form_data = request.POST.dict()

        prices = [
            form_data.get('size'), 
            form_data.get('taste'), 
            form_data.get('yield'), 
            form_data.get('sugar'), 
            form_data.get('calories'), 
            form_data.get('protein'), 
            form_data.get('fiber'), 
            form_data.get('vitaminc')
        ]

        total = 0

        for price in prices:
            total += int(price)

        total = total / len(prices)

        return render(request, 'calculator/calculator.html', {'price':total})
    
    return render(request, 'calculator/calculator.html', {'price': 0})