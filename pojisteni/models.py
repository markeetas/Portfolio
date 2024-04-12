from django.db import models

class Insured(models.Model):
    name = models.CharField(max_length=100)
    
    
class Insurance(models.Model):
    insured_person = models.ForeignKey(Insured, on_delete=models.CASCADE)
    policy_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
class InsuranceEvent(models.Model):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    event_date = models.DateField()
    description = models.TextField()       
