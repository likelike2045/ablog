from django.contrib import admin
from .models import Post, Category, Category_2

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('category','title','author','post_date')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Category_2)