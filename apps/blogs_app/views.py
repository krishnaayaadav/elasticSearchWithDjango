from django.shortcuts import render
from django.views import View
from apps.blogs_app.documents import BlogModelDocument

# Create your views here.


class BlogSearchview(View):

    def get(self, request):

        search_query = request.GET.get('search_query')

        print(search_query)

        if search_query:
            results = BlogModelDocument.search().query('match', category=search_query)
        
        else:
            results = BlogModelDocument.search().query('match_all')
        
        return render(request, 'blog_search.html', {'search_results': results})