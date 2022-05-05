from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app_my_blog.urls import *


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, home)

    def test_profile_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, profile)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, register_view)

    def test_create_post_url_is_resolved(self):
        url = reverse('create_post')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, PostFormView)

    def test_upload_post_file_url_is_resolved(self):
        url = reverse('upload_posts')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, UploadPostFormView)

    def test_upload_images_url_is_resolved(self):
        url = reverse('upload_images', args=[100])
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func, multiple_img_upload)

    def test_edit_post_url_is_resolved(self):
        url = reverse('edit_post', args=[4])
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, PostEditFormView)

    def test_post_detail_url_is_resolved(self):
        url = reverse('post_detail', args=[2])
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_edit_profile_url_is_resolved(self):
        url = reverse('edit_profile', args=[30])
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, ProfileEditFormView)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, LogInView)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        print(resolve(url), end="\n\n")
        self.assertEquals(resolve(url).func.view_class, LogOutView)
