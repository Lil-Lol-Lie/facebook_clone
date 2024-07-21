from django.contrib import admin
from core.models import Post, Gallery, Comment, Friend, FriendRequest, ReplyComment, Notification, Group, Page, PagePost, GroupPost, ChatMessage

class GalleryAdmin(admin.TabularInline):
    model = Gallery

class CommentTabAdmin(admin.TabularInline):
    model = Comment
    
class GroupPostTabAdmin(admin.TabularInline):
    model = GroupPost
    
class PostAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin, CommentTabAdmin]
    list_editable = ['user', 'title', 'visibility']
    list_display = ['thumbnail', 'user', 'title', 'visibility']
    prepopulated_fields = {"slug": ("title", )}

class GroupAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}
    
class FriendRequestAdmin(admin.ModelAdmin):
    list_editable = ['status']
    list_display = ['sender', 'receiver', 'status']
    
class GroupAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}

class PageAdmin(admin.ModelAdmin):
    # inlines = [GroupPostTabAdmin]
    list_editable = ['user', 'name', 'visibility']
    list_display = ['thumbnail', 'user', 'name', 'visibility']
    prepopulated_fields = {"slug": ("name", )}

class FriendAdmin(admin.ModelAdmin):
    list_display = ['user', 'friend']
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'comment', 'active']
    
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'active']
    
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'sender', 'post', 'comment', 'seen']
    
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'sender', 'reciever' ,'message','date', 'is_read']
    
admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Gallery)
admin.site.register(Friend, FriendAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(GroupPost)
admin.site.register(PagePost)
admin.site.register(ChatMessage, ChatMessageAdmin)



