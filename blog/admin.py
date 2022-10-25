from django.contrib import admin
from . import models

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'updated',
    )

    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )


admin.site.register(models.Post, PostAdmin)
