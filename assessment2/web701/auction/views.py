from django.shortcuts import render, redirect

dummy_auction_items = {
    "Items": [
        {
            "name": "strawberries",
            "quantity": 100,
            "price": 1.35,
            "bidders": []
        },
        {
            "name": "blueberries",
            "quantity": 70,
            "price": 2.10,
            "bidders": []
        },
        {
            "name": "blackberries",
            "quantity": 130,
            "price": 3.99,
            "bidders": []
        },
        {
            "name": "kiwiberries",
            "quantity": 50,
            "price": 6.82,
            "bidders": []
        },
    ]
}

def auction(request):
    context = {'listings': dummy_auction_items}
    return render(request, 'auction/auction.html', context=context)

def bid_item(request):
    if request.method == 'POST':
        form_data = request.POST.dict()

        bidder = form_data.get('user')
        quantity = int(form_data.get('quantity'))
        listing = form_data.get('listing')
        price = float(form_data.get('price'))
        total_price = price * quantity

        for val in dummy_auction_items.values():
            for item in val:
                if listing == item['name']:
                    item['bidders'].append({
                                        'name': bidder, 
                                        'quantity': quantity, 
                                        'price': total_price})
                    item['quantity'] -= quantity
        return redirect('auction')

    return redirect('auction')

def sell_item(request):
    if request.method == 'POST':
        form_data = request.POST.dict()

        item_data = {
            'name': form_data.get('name'),
            'quantity': int(form_data.get('quantity')),
            'price': float(form_data.get('price')),
            'bidders': []
        }

        dummy_auction_items["Items"].append(item_data)
        return redirect('auction')

    return render(request, 'auction/sell.html')