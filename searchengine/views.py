from django.shortcuts import render
from .models import Websites
from django.core.paginator import Paginator
from django.db import connection
from django.core.paginator import Paginator


def search(request): # add get query time
    if request.method == 'GET':

        message = 'no result'
        
        if search_quary := request.GET.get('search'):
            data = Websites.objects.filter(title__contains=search_quary)

            paginator = Paginator(data, per_page=20)
            page_number = request.GET.get('?page')
            page_obj = paginator.get_page(page_number)
 
            context = {'data':page_obj, 'count':data.count(), 'search':search_quary}
            
            return render(request, 'searchengine/index.html', context)
        
        return render(request, 'searchengine/index.html', {'message':message})