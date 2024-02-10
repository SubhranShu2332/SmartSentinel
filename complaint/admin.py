from django.contrib import admin
from complaint.models import Complaint

# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
    list_display=('__str__','place','violation_date','status','uploaded_file')
    search_fields = ('user','place','violation_date' )
    list_editable = ('status', )
    list_filter = ('status','district','state','violation_date')
admin.site.register(Complaint,ComplaintAdmin)