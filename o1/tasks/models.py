from django.db import models

# Create your models here.
class Task(models.Model):
    
    name = models.CharField(max_length = 20)
    detail = models.CharField(max_length = 200)
    is_completed = models.BooleanField(default = False)
    completed_at = models.DateTimeField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name