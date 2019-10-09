from django.db import models


# Create your models here.    

class Category(models.Model):
    name = models.CharField(max_length = 20)
    
    
    def save_category(self):
        '''
        Method to save categories of the images
        '''
        
        self.save()
    
        
        
    def update_category(self, test):
        '''
          Method to update the category to the database
        '''
        self.update(name = test)
    
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=50)
    
    
    def save_location(self):
        '''
        Method used to save the location
        '''
        
        self.save()
        
        
        
    def update_location(self, test):
        '''
          Method to update the location
        '''
        self.update(name = test)
        
    
    @classmethod
    def get_all_locations(cls):
        '''
          Method to filter and return all the locations
        '''
        locations = cls.objects.all()
        return locations
    
    
    def __str__(self):
        return self.name
          
  
class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/', default='default.png')
    image_name = models.CharField(max_length = 30)
    image_description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    
    def save_image(self):
        '''
        Method used to save images
        '''
        
        self.save()
        
        
        
    def update_image(self, test):
        '''
          Method to update the images
        '''
        self.update(name = test)
    
    
    @classmethod
    def get_images(cls):
        '''
          Method to get an image using its id.
        '''
        images = cls.objects.all()
        print(images)
        return images
        
        
    @classmethod
    def search_by_category(cls,search_term):
        '''
          Method to search for images based on their category.
        '''
        images = cls.objects.filter(category__name__icontains = search_term)
        
        return images
    
    
    @classmethod
    def get_all_images(cls):
        '''
          Method to return all the images.
        '''
        images = cls.objects.all()
        return images
        
    
    class Meta:
        ordering = ['image_name']
    
    
    def __str__(self):
        return self.image_name