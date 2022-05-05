from unittest import TestCase
from django.contrib.auth.models import User
from app_my_blog.models import Post, Image


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_01',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_post = Post.objects.create(post_author=self.user,
                                             post_title='Some post title',
                                             post_content='Some post content'
                                             )

    def test(self):
        self.assertEqual(str(self.test_post), 'Some post title')
        self.user.delete()
        self.test_post.delete()


class TestImageModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_username_02',
                                        email='test@test.com')

        self.user.set_password('some_password123')
        self.user.save()

        self.test_post = Post.objects.create(post_author=self.user,
                                             post_title='Some post title',
                                             post_content='Some post content'
                                             )

    def test(self):
        test_image = Image.objects.create(post_id=self.test_post,
                                          images="media/files/php.jpg")

        self.assertEquals(str(test_image), 'Some post title')
        self.user.delete()
        self.test_post.delete()
        test_image.delete()
