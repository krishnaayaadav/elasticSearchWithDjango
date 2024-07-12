
from apps.blogs_app.models import Blog
from django_elasticsearch_dsl import Document, Index
from django_elasticsearch_dsl.registries import registry


blog_index = Index('blog')

# blog document for elastic search
@blog_index.document
class BlogModelDocument(Document):

    class Django:

        model  = Blog
        fields = [
            'id',
            'title',
            'description',
            'category',
            'author',
            'created'
        ]