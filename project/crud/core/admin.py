from django.contrib import admin
from.models import jobnew
# Register your models here.
@admin.register(jobnew)
class jobAdmin(admin.ModelAdmin):
    list = ['id','position','job_time','job_type','place_of_work','posted_date','deadline']
    