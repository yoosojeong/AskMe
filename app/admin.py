from django.contrib import admin
from . import models

@admin.register(models.UserBox)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'message',
        'creator',
        'created_at'
    )

@admin.register(models.ReComment)
class ReCommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'reuserbox',
        'remessage',
        'created_at'
    )
