from django.contrib import admin
from .models import ChaiVariety , ChaiReview , Store , ChaiCertification

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2
    
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type' , 'date_added')
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)
    
class ChaiCertificationAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certification_number', 'date_issued', 'valid_till')
    
admin.site.register(ChaiVariety , ChaiVarietyAdmin)
# admin.site.register(ChaiReview)
admin.site.register(Store , StoreAdmin)
admin.site.register(ChaiCertification , ChaiCertificationAdmin)
