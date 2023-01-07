from django.contrib import admin
from .models import Tag,Blog,BookmarkedBlog,BlogPic
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(BookmarkedBlog)
admin.site.register(BlogPic)
# Register your models here.
