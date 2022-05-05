from django.urls import path
from app_my_blog.views import *

urlpatterns = [

    # Главная страница
    path("", home, name="home"),

    # Страница профиля
    path("profile/", profile, name="profile"),

    # Страница регистрации
    path('register/', register_view, name="register"),

    # Создать пост дефолтным способом
    path('my_blog/create_post', PostFormView.as_view(), name="create_post"),

    # Создать пост(ы) через csv-файл
    path('my_blog/upload_post_file', UploadPostFormView.as_view(), name="upload_posts"),

    # Загрузить изображения к посту
    path('my_blog/upload_images/<int:post_id>', multiple_img_upload, name="upload_images"),

    # Страница редактирования поста
    path('my_blog/edit_post/<int:post_id>', PostEditFormView.as_view(), name="edit_post"),

    # Страница поста
    path('my_blog/<int:pk>', PostDetailView.as_view(), name="post_detail"),

    # Страница редактирования профиля
    path('my_blog/edit_profile/<int:profile_id>', ProfileEditFormView.as_view(), name="edit_profile"),

    # Страница логина
    path('login/', LogInView.as_view(), name="login"),

    # Страница логаута
    path('logout/', LogOutView.as_view(), name="logout"),

]
