from django.shortcuts import render

# Create your views here.
def article(request):
    return render(request, 'Article/article-list.html')

def articleDetail(request):
    article_id = request.GET.get('article-id')
    return render(request, 'Article/article-detail.html', {'article_id': article_id})