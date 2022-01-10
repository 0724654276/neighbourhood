from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,null=True)
    occupant_count = models.IntegerField(null=True)
    
    def save_neighborhood(self):
        self.save()
        
    @classmethod
    def delete_neighborhood(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def update_neighborhood(cls,id,new_name):
        cls.objects.filter(id=id).update(hood_name = 'newname')
   
    @classmethod
    def update_family_count(cls,id,new_occupant):
       cls.objects.filter(id=id).update(family_size = new_occupant) 

    @classmethod
    def search_hood(cls,id):
       search= cls.objects.filter(neighborhood_name__icontains=id)
       return search