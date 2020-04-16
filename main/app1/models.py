from django.db import models

# Create your models here.
class info(models.Model):
    Course_Name = models.CharField(max_length = 200)
    Course_Description = models.CharField(max_length = 500)
    Course_Information = models.TextField(null=True, blank=True)
    Additional_Information = models.URLField(max_length = 250, null=True, blank=True)

    def __str__(self):
        return self.Course_Name