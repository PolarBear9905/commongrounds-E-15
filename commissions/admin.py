from django.contrib import admin
from .models import CommissionType, Commission


class CommissionTypeAdmin(admin.ModelAdmin):
    model = CommissionType
    list_display = ['name', 'description']
    ordering = ["name"]


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    list_display = [
        'title',
        'description',
        'people_required',
        'commission_type',
        'created_on',
        'updated_on'
    ]
    ordering = ["created_on"]


admin.site.register(CommissionType, CommissionTypeAdmin)
admin.site.register(Commission, CommissionAdmin)
