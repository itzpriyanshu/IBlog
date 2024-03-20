from django.contrib import admin
from .models import Category,Post

#Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'desc', 'url', 'add_date')
    search_fields = ('title','desc', 'url')

#Post Admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('postimage_tag','title', 'url',)
    search_fields = ('title','content', 'url')
    list_filter = ('cat',)
    list_per_page = 10

    class Media:
        js = ("https://cdn.tiny.cloud/1/oj3l21icqihuh5felj3b1fpozloaszbagwb14eg90wcr2yw4/tinymce/6/tinymce.min.js","js/static.js",)

# Register your models here.

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)
