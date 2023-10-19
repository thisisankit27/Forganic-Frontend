from django.shortcuts import render

# Create your views here.

def item(request):
    return render(request, 'Item/itemAdmin.html')

def itemDetail(request):
    item_id = request.GET.get('item-id')
    return render(request, 'Item/itemDetail.html', {'item_id': item_id})

def itemPOST(request):
    return render(request, 'Item/itemPOST.html')