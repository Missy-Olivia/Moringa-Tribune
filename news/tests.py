from django.test import TestCase
from .models import Editor, tags, Article

# Create your tests here.
class EditorTestClass(TestCase):

    #setup method
    def setUp(self):
        self.Missy = Editor(first_name = 'Missy', last_name = 'Olivia', email = 'ngamissia@gmail.com')
    
    #Testing Instance

    def test_instance(self):
        self.assertTrue(isinstance(self.Missy, Editor))

    #testing save method
    def test_save_method(self):
        self.Missy.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)> 0 )