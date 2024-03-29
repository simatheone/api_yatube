from django.contrib import admin

from .models import Comment, Group, Post
from yatube_api.settings import EMPTY_VALUE_DISPLAY


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Класс для отображения постов в админ панели.
    """
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        'image'
    )
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """
    Класс для отоброжения групп в админ панели.
    """
    list_display = ('title',)
    empty_value_display = EMPTY_VALUE_DISPLAY


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Класс для отоброжения комментариев в админ панели.
    """
    list_display = (
        'post',
        'text',
        'author',
        'created'
    )
    search_fields = ('text',)
    list_filter = ('created',)
    empty_value_display = EMPTY_VALUE_DISPLAY
