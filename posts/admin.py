from django.contrib import admin
from posts.models import Post, Comment
# Register your models here.


class AdminPost(admin.ModelAdmin):
    list_display = ('id', 'title', 'rate', 'created_date', 'modified_date',)
    sortable_by = ('id', 'title', 'rate', 'created_date', 'modified_date',)


admin.site.register(Post,AdminPost)
admin.site.register(Comment)

