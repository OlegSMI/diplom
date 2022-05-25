from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class InfoUserAdmin(admin.ModelAdmin):
    list_display = ('num_user', 'user_id', 'name', 'online_status', 'status', 'get_photo', 'town', 'languages' )
    # fields = ('num_user', 'user_id', 'name', 'online_status', 'status', 'get_photo', 'town', 'languages' )
    # readonly_fields = ('get_photo', )

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото отсутствует'

    get_photo.short_description = 'Фото профиля'

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_user', 'groups')

class UserGeolocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_user', 'location')

class UserFriendsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_user', 'friends')

class UserPostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_user', 'posts')

class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'num_user', 'comments')


admin.site.register(InfoUser, InfoUserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(Friends, UserFriendsAdmin)
admin.site.register(Posts, UserPostsAdmin)
admin.site.register(Comments, UserCommentsAdmin)
admin.site.register(Geolocation, UserGeolocationAdmin)
