
from django.contrib import admin
from .models import *

from .models import MyRating

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'published_year', 'average_rating', 'num_pages', 'ratings_count', 'price')
    search_fields = ('title', 'authors', 'categories')
    list_filter = ('categories',)

admin.site.register(Author)
admin.site.register(Category)




admin.site.register(MyRating)


# admin.site.register(MyRating, MyratingAdmin)

