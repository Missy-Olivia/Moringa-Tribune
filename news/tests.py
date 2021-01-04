from django.test import TestCase
from .models import Editor, tags, Article
import datetime as dt
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

class ArticleTestClass(TestCase):
    #creating new editor and saving them
    def setUp(self):
        self.Missy = Editor(first_name = 'Missy', last_name = 'Olivia', email = 'ngamissia@gmail.com')
        self.Missy.save_editor()


        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.Missy)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2020-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)