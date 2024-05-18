from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="chat-home"),
    path('chat/<username>', views.get_or_create_chatroom, name="start-chat"),
    path('chatroom/<chatroom_name>', views.index, name="chatroom"),
    path('new_groupchat/', views.create_groupchat, name="new-groupchat"),
    path('edit/<chatroom_name>', views.chatroom_edit_view, name="edit-chatroom"),
    path('delete/<chatroom_name>', views.chatroom_delete_view, name="chatroom-delete"),
    path('leave/<chatroom_name>', views.chatroom_leave_view, name="chatroom-leave"),
    path('fileupload/<chatroom_name>', views.chat_file_upload, name="chat-file-upload"),
]