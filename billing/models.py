from django.db import models

class ModelWala(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_no=models.IntegerField()
    emp_design=models.CharField(max_length=20)
    mob_no=models.IntegerField()
    
    def __str__(self):
        return f"NAME:{self.emp_name},NO:{self.emp_no}"

