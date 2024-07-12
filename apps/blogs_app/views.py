from django.shortcuts import render
from elasticsearch_dsl import Q
from django.views import View
from apps.blogs_app.documents import BlogModelDocument

from django.core.paginator import PageNotAnInteger,EmptyPage, Paginator

# Create your views here.

# get paginated reponse
def get_paginated_response(result_objects, page_size, request):
    
    page_num = request.GET.get('page')

    paginator = Paginator(result_objects, page_size)

    try:
        paginated_result = paginator.page(page_num)
    
    except PageNotAnInteger:
        paginated_result = paginator.page(1)
    
    except EmptyPage:
        paginated_result = paginator.page(paginator.num_pages)
    
    finally:
        return paginated_result


class BlogSearchview(View):

    def get(self, request):

        search_query = request.GET.get('search_query')

        print(search_query)

        if search_query:
            # search with multiple-model fields here
            q = Q(
                'multi_match',
                query=search_query,
                fields=['name', 'description', 'category', 'author']
            )
            search_result = BlogModelDocument.search().query(q)
        else:
            search_result = BlogModelDocument.search().query('match_all')
        


        
        return render(request, 'blog_search.html', {'paginated_result': search_result})