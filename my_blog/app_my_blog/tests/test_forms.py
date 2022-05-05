from unittest import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from app_my_blog.forms import AuthForm, RegisterForm, UploadPostForm, UserForm, ProfileForm, PostForm, \
    MultipleFilesLoadForm


class TestAuthForm(TestCase):
    def test_auth_form_is_valid(self):
        form = AuthForm(data={
            "username": "User_01",
            "password": "Somepassword_231"
        })

        self.assertTrue(form.is_valid())

    def test_auth_form_not_valid(self):
        form = AuthForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class TestRegisterForm(TestCase):
    def test_register_form_is_valid(self):
        form = RegisterForm(data={"username": "User_01",
                                  "first_name": "Jonh",
                                  "last_name": "James",
                                  "password1": "Somepassword_231",
                                  "password2": "Somepassword_231",
                                  "email": "jonh.james@gmail.com",
                                  "date_of_birth": "10/10/1990",
                                  "city": "Chicago",
                                  "phone_number": "+0000000000",
                                  })

        self.assertTrue(form.is_valid())

    def test_register_form_not_valid(self):
        form = RegisterForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)


class TestUploadPostForm(TestCase):

    def test_upload_post_form_is_valid(self):
        upload_file = open('posts.csv', 'rb')
        file_dict = {'file': SimpleUploadedFile(upload_file.name, upload_file.read())}
        form = UploadPostForm(files=file_dict)
        self.assertTrue(form.is_valid())

    def test_upload_post_form_not_valid(self):
        form = UploadPostForm(files={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class TestUserForm(TestCase):

    def test_user_form_is_valid(self):
        form = UserForm(data={"username": "User_name_01",
                              "first_name": "Jonh",
                              "last_name": "James"})

        self.assertTrue(form.is_valid())

    def test_user_form_not_valid(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class TestProfileForm(TestCase):

    def test_profile_form_is_valid(self):
        form = ProfileForm(data={"date_of_birth": "10/10/1990",
                                 "city": "Moscow",
                                 "email": "test@test.com",
                                 "phone_number": "+88888888"})

        self.assertTrue(form.is_valid())

    def test_profile_form_not_valid(self):
        form = UserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


class TestPostForm(TestCase):

    def test_post_form_is_valid(self):
        form = PostForm(data={"post_title": "Some title",
                              "post_content": "Some content"})

        self.assertTrue(form.is_valid())

    def test_post_form_not_valid(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class TestMultipleFilesLoadForm(TestCase):

    def test_multiple_files_load_form_is_valid(self):
        image = SimpleUploadedFile(name='some_img',
                                   content=open('media/files/3c0cefa6f99fda8d9596da474fc7e264.jpg', 'rb').read(),
                                   content_type='image/jpeg')

        form = MultipleFilesLoadForm(files={'images': image})
        self.assertTrue(form.is_valid())

    def test_multiple_files_load_form_not_valid(self):
        form = MultipleFilesLoadForm(files={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
