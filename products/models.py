from django.db import models



class products(models.Model):
    Name = models.CharField(max_length=255)
    RollNo = models.FloatField()
    Class = models.IntegerField()
    Address = models.CharField(max_length=3000)


class offers(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Deployable_Pool(models.Model):
    PSNO= models.FloatField(default='PS NO',null=True, blank=True)
    Name = models.CharField(max_length=2555, null=True, blank=True)
    Grade = models.CharField(max_length=2555, null=True, blank=True)
    DeptLoc = models.CharField('Dept Loc',max_length=2555, null=True, blank=True)
    Billedstatus = models.CharField(max_length=2555, null=True, blank=True)
    Skill = models.CharField(max_length=2555, null=True, blank=True)
    ActionCategory = models.CharField(max_length=2555, null=True, blank=True)
    ActionSubCategory = models.CharField(max_length=2555, null=True, blank=True)
    ActiveAccount = models.CharField(max_length=2555, null=True, blank=True)
    ProposedAccounts = models.CharField(max_length=2555, null=True, blank=True)
    Remarks = models.CharField(max_length=2555, null=True, blank=True)
    SelectedDate = models.DateField(null=True, blank=True)
    CustomerName = models.CharField(max_length=2555, null=True, blank=True)
    ReleaseToPUDate = models.DateField(null=True, blank=True)
    StartDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    UnbilledAgeInCurrentBU = models.IntegerField(null=True, blank=True)
    Mobile = models.TextField(null=True, blank=True)
    AgingBucket = models.CharField(max_length=2555, null=True, blank=True)



class RRDump(models.Model):
    RR = models.CharField(max_length=2555, null=True, blank=True)
    RRno = models.CharField(max_length=2555, null=True, blank=True)
    RRSno = models.CharField(max_length=2555, null=True, blank=True)
    ProjectID = models.CharField(max_length=2555, null=True, blank=True)
    OpportunityID = models.CharField(max_length=2555, null=True, blank=True)
    ProposeID = models.CharField(max_length=2555, null=True, blank=True)
    DeliveryBU = models.CharField(max_length=2555, null=True, blank=True)
    Description = models.CharField(max_length=2555, null=True, blank=True)
    NeedByDate = models.CharField(max_length=2555, null=True, blank=True)
   # Customername = models.CharField(max_length=2555, null=True, blank=True)
    Location = models.CharField(max_length=2555, null=True, blank=True)
   # Approver = models.CharField(max_length=2555, null=True, blank=True)
    MandatorySkill = models.CharField(max_length=2555, null=True, blank=True)
    DesiredSkill = models.CharField(max_length=2555, null=True, blank=True)
    BilledStatus = models.CharField(max_length=2555, null=True, blank=True)
    NoOfPos = models.CharField(max_length=2555, null=True, blank=True)
    Status = models.CharField(max_length=2555, null=True, blank=True)
   # OnsiteOffshore = models.CharField(max_length=2555, null=True, blank=True)
    BillingStartDate = models.CharField(max_length=2555, null=True, blank=True)
    BillingEndDate = models.CharField(max_length=2555, null=True, blank=True)
    JobDescription = models.CharField(max_length=2555, null=True, blank=True)
    ClientLoc = models.CharField(max_length=2555, null=True, blank=True)



class Manpower(models.Model):
    Customer_Namee = models.CharField(max_length=2555, null=True, blank=True)

class Rotation(models.Model):
    Customer_Nameee = models.CharField(max_length=2555, null=True, blank=True)

class Academy(models.Model):
    Customer_Namee = models.CharField(max_length=2555, null=True, blank=True)