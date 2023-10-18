from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'Client/homepage.html')

def item(request):
    item_id = request.GET.get('item-id')
    return render(request, 'Client/item.html', {'item_id': item_id})