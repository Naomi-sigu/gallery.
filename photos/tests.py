from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.

class LocationTestClass(TestCase):
    '''
    Tests for the class Location
    '''
    
    def setUp(self):
        '''
        Runs before each test
        '''
        
        self.location = Location(id = 20, name = 'new-york')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the class Location 
        '''
        
        self.assertTrue(isinstance(self.location, Location))
        
        
    def test_save_method(self):
        '''
        Test whether the object is saved in the database.
        '''
        
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
        
    def test_update_method(self):
        '''
        Test if the object can be updated.
        '''
        self.location.save_location()
        self.location = Location.objects.filter(name = 'new-york').update(name = 'Rwanda')
        self.updated_location = Location.objects.get(name = 'Rwanda')
        self.assertEqual(self.updated_location.name,"Rwanda")
        
class CategoryTestClass(TestCase):
    '''
    Tests for Category class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.category = Category(id = 20, name = 'shoes')
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Category class.
        '''
        
        self.assertTrue(isinstance(self.category, Category))
        
      
    def test_save_method(self):
        '''
        Test whether the object is saved in the database.
        '''
        
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
        
    def test_update_method(self):
        '''
        Test if the object can be updated.
        '''
        self.category.save_category()
        self.category = Category.objects.filter(name = 'shoes').update(name = 'vans')
        self.updated_category = Category.objects.get(name = 'vans')
        self.assertEqual(self.updated_category.name,"vans")
        
         
class ImageTestClass(TestCase):
    '''
    Tests for Image class.
    '''
    
    def setUp(self):
        '''
        Runs before each test.
        '''
        
        self.location = Location(name = 'New-york')
        self.location.save_location()
        self.category = Category(name = 'shoes')
        self.category.save_category()
        
        self.image = Image(id = 20, image_path = 'image/location1', image_name = 'Image1', image_description = 'Test', location = self.location, category = self.category)
        
        
    def test_instance(self):
        '''
        Checks if object is an instance of the Image class.
        '''
        
        self.assertTrue(isinstance(self.image, Image))
        
    
    def test_save_image(self):
        '''
        Test whether the object is saved in the database.
        '''
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)
         
    def test_search_by_category(self):
        '''
        Test whether images can be searched based on their category.
        '''
        self.image.save_image()
        self.category = Category(name = "shoes")
        self.category.save_category()
        self.searched_images = Image.search_by_category('shoes')
        self.assertTrue(len(self.searched_images) > 0)