from django.test import TestCase, Client
from django.urls import reverse
from app_my_blog.models import Profile, Post
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='user_01',
                                             email='user_01@test.com',
                                             password='Somebody_password_01')

        self.logged_in = self.client.login(username='user_01', password='Somebody_password_01')

        self.profile = Profile.objects.create(user=self.user,
                                              date_of_birth="1990-10-10",
                                              city="Moscow",
                                              email="user@user.com",
                                              phone_number="+88805553535"
                                              )

        self.post = Post.objects.create(post_author=self.user,
                                        post_title='Some title',
                                        post_content='Some content')

    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/home.html')

    def test_profile(self):
        response = self.client.get(reverse("profile"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/profile.html')

    def test_register_GET(self):
        response = self.client.get(reverse("register"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/register.html')

    def test_register_POST(self):
        response = self.client.post(reverse("register"), {"username": "User_01",
                                                          "first_name": "Jonh",
                                                          "last_name": "James",
                                                          "password1": "Somepassword_231",
                                                          "password2": "Somepassword_231",
                                                          "email": "jonh.james@gmail.com",
                                                          "date_of_birth": "10/10/1990",
                                                          "city": "Chicago",
                                                          "phone_number": "+0000000000",
                                                          })
        self.assertRedirects(response, reverse('home'))
        self.assertEquals(response.status_code, 302)

    def test_profile_edit_GET(self):
        response = self.client.get(reverse("edit_profile", args=[self.profile.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/edit_profile.html')

    def test_profile_edit_POST(self):
        response = self.client.post(reverse("edit_profile", args=[self.profile.id]),
                                    {"username": "user_02",
                                     "first_name": "Jonh",
                                     "last_name": "James",
                                     "date_of_birth": "1990-10-11",
                                     "city": "Chicago",
                                     "email": "user@1user.com",
                                     "phone_number": "+88805553535"
                                     })

        self.assertRedirects(response, reverse('home'))
        self.assertEquals(response.status_code, 302)

    def test_create_post_view_GET(self):
        response = self.client.get(reverse("create_post"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/create_post.html')

    def test_create_post_view_POST(self):
        response = self.client.post(reverse("create_post"), {
            "post_title": "Some title",
            "post_content": "Some content"
        })
        self.assertRedirects(response, reverse('home'))
        self.assertEquals(response.status_code, 302)

    def test_upload_posts_view_GET(self):
        response = self.client.get(reverse("upload_posts"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/upload_post_file.html')

    def test_post_edit_view_GET(self):
        response = self.client.get(reverse("edit_post", args=[self.post.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/edit_post.html')

    def test_post_edit_view_POST(self):
        response = self.client.post(reverse("edit_post", args=[self.post.id]),
                                    {"post_title": "Some title",
                                     "post_content": "Some content"
                                     })

        self.assertRedirects(response, reverse('home'))
        self.assertEquals(response.status_code, 302)

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", args=[self.post.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/post_detail.html')

    def test_multiple_img_upload_view_GET(self):
        response = self.client.get(reverse("upload_images", args=[self.post.id]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_blog/upload_images.html')

    def test_multiple_img_upload_view_POST(self):
        with open('media/files/1592990176.jpg', 'rb') as img:
            response = self.client.post(reverse("upload_images", args=[self.post.id]),
                                        {'images': img})

        self.assertRedirects(response, reverse('home'))
        self.assertEquals(response.status_code, 302)
