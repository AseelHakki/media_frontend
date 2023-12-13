from django.contrib import admin
from .models import Department, FileBook, Governorate, MediMessages, MediaAtt, MediaIfad


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
   list_display = ['id', 'name']


@admin.register(FileBook)
class FileBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Governorate)
class GovernorateAdmin(admin.ModelAdmin):
    list_display = ['idG', 'title']


@admin.register(MediMessages)
class MediMessagesAdmin(admin.ModelAdmin):
    list_display = ['id','msg_user', 'msg_title', 'msg_date', 'msg_time', 'msg_content',
                    'msg_governorate', 'msg_fileBook', 'msg_jih', 'msg_procedures', 'msg_newseditor',
                    'msg_editdate', 'msg_receiveteam', 'msg_secretary',
                    'msg_secretary', 'msg_Minister', 'msg_published', 'msg_tracking', 'created_at', 'created_by']


@admin.register(MediaAtt)
class MediaAttAdmin(admin.ModelAdmin):
    list_display = ['idattch', 'id_relt', 'attch_title', 'attch_path']


@admin.register(MediaIfad)
class MediaIfadAdmin(admin.ModelAdmin):
    list_display = ['idifada', 'id_relb', 'ifada_title', 'ifada_path']
