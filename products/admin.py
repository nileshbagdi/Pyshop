from django.contrib import admin
from .models import Deployable_Pool,RRDump
from import_export.admin import ImportExportModelAdmin


class Deployable_PoolAdmin(ImportExportModelAdmin):
    list_display = ('PSNO', 'Name', 'Grade', 'DeptLoc', 'Billedstatus', 'Skill', 'ActionCategory',
                    'ActionSubCategory', 'ActiveAccount', 'ProposedAccounts', 'Remarks',
                    'SelectedDate', 'CustomerName', 'ReleaseToPUDate', 'StartDate',
                    'EndDate', 'UnbilledAgeInCurrentBU', 'Mobile', 'AgingBucket'
                    )


class RRDumpAdmin(ImportExportModelAdmin):
    list_display = ('RR','RRno','RRSno','ProjectID','OpportunityID','ProposeID','DeliveryBU'
                    ,'Description','NeedByDate','Location',
                    'MandatorySkill','DesiredSkill','BilledStatus','NoOfPos','Status',
                    'BillingStartDate','BillingEndDate','JobDescription',
                    'ClientLoc'

    )

admin.site.register(Deployable_Pool, Deployable_PoolAdmin)
admin.site.register(RRDump,RRDumpAdmin)
