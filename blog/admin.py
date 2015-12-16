from django.contrib import admin

from blog.models import Blog,Post
# Register your models here.
class post(admin.TabularInline):
    model = Post
    extra = 1


class inlines(admin.ModelAdmin):
    fields = ['title','text','date']
    inlines = [post]



admin.site.register(Blog,inlines)