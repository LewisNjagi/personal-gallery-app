from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(name = '')