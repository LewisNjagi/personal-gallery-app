from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Religion')
        self.category.save_category()
        self.location = Location(name = 'Nairobi')
        self.location.save_location()
        self.image = Image(id=1,image='media/gallery/Jesus_wallpaper.png',name='religion',description='Jesus',location=self.location,category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.category,Category))
        self.assertTrue(isinstance(self.location,Location))

    # Testing Save Method
    def test_save_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image.save_image()
        image = Image.objects.filter(name='religion')
        Image.delete_image(image)
        images = Image.objects.all()
        self.assertTrue(len(images) <= 0)

    def test_update_method(self):
        self.image.save_image()
        new_image = Image.objects.filter(id = 1).update(name = 'Jesus')
        new_name = Image.objects.get(name = 'Jesus')
        self.assertTrue(new_name.name,'Jesus')

    def test_get_image_by_id(self):
        self.image.save_image()
        image_id = Image.get_image_by_id(1)
        self.assertEqual(image_id.id,1)

    def test_get_image_by_category(self):
        self.image.save_image()
        image_category = Image.objects.get(category = 2)
        self.assertTrue(image_category.category,2)

    # def test_filter_by_location(self):
    #     self.image.save_image()        
    #     fetch_specific = Location.objects.get(name = 'Nairobi')
    #     self.assertTrue(fetch_specific.name == 'Nairobi')