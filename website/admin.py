from django.contrib import admin
from status.models import Post, Comment, Like

# Register your models here.


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)


class PostAdmin(admin.ModelAdmin):
    list_display = ('author')
    fieldsets = [
        (None, { 'fields': [('author','text')] } ),
    ]

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
