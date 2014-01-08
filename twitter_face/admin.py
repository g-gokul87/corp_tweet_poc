from django.contrib import admin
from django.contrib.auth.models import User
from models import TweetData


class TweetDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'tweeted_by', 'content', 'tweeted_content', 'submitted_on', 'category',
                    'generic_item_type', 'specific_item_type', 'published_on')
    list_display_links = ('id', 'tweeted_by')


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'date_joined')


admin.site.register(TweetData, TweetDataAdmin)
admin.site.unregister(User)  # Unregistering the default User table in admin.
admin.site.register(User, CustomUserAdmin)
