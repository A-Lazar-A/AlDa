from django.contrib import admin
from .models import PassportOfObject, Jobs, SubJobs, CounterParty


class PassportOfObjectAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    filter_horizontal = ('Jobs',)


class CounterPartyAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Value')
    filter_horizontal = ('Accreditation',)


class JobsAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    filter_horizontal = ('CategoryOfWork',)


class SubJobsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'CostForOne', 'Quantity')


admin.site.register(PassportOfObject, PassportOfObjectAdmin)
admin.site.register(CounterParty, CounterPartyAdmin)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(SubJobs, SubJobsAdmin)

# Register your models here.
