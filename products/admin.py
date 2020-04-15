from django.contrib import admin
from .models import products,Deployable_Pool, offers, Manpower, Rotation, RRDump, Academy
from import_export.admin import ImportExportModelAdmin



class OffersAdmin(ImportExportModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(ImportExportModelAdmin):
    list_display = ('Name', 'RollNo', 'Class','Address')


class Deployable_PoolAdmin(ImportExportModelAdmin):
    list_display = ('PSNO', 'Name', 'Grade', 'DeptLoc', 'Billedstatus', 'Skill', 'ActionCategory',
                    'ActionSubCategory', 'ActiveAccount', 'ProposedAccounts', 'Remarks',
                    'SelectedDate', 'CustomerName', 'ReleaseToPUDate', 'StartDate',
                    'EndDate', 'UnbilledAgeInCurrentBU', 'Mobile', 'AgingBucket'
                    )


class ManpowerAdmin(ImportExportModelAdmin):
    pass


class RRDumpAdmin(ImportExportModelAdmin):
    list_display = ('RR','RRno','RRSno','ProjectID','OpportunityID','ProposeID','DeliveryBU'
                    ,'Description','NeedByDate','Location',
                    'MandatorySkill','DesiredSkill','BilledStatus','NoOfPos','Status',
                    'BillingStartDate','BillingEndDate','JobDescription',
                    'ClientLoc'

    )

class AcademyAdmin(ImportExportModelAdmin):
    pass

class RotationAdmin(ImportExportModelAdmin):
    pass



admin.site.register(offers, OffersAdmin)
admin.site.register(products, ProductAdmin)
admin.site.register(Deployable_Pool, Deployable_PoolAdmin)
admin.site.register(Manpower, ManpowerAdmin)
admin.site.register(RRDump,RRDumpAdmin)
admin.site.register(Academy,AcademyAdmin)
admin.site.register(Rotation,RotationAdmin)
