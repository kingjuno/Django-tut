from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    
    def __str(self):
        return self.name
    objects = models.Manager()
    
class Item(models.Model):
    toDoList = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str(self):
        return self.text
    
    