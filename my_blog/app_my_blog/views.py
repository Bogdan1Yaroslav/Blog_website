from _csv import reader
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from app_my_blog.forms import PostForm, RegisterForm, UserForm, ProfileForm, UploadPostForm, MultipleFilesLoadForm
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from app_my_blog.models import Post, Profile, Image
from django.views.generic import DetailView
from django.db.models import Q


# ----------------------------------------------------------------------------------------------------------------------
# Логин
class LogInView(LoginView):
    template_name = "my_blog/login.html"


# Логаут
class LogOutView(LogoutView):
    next_page = "/"


# ----------------------------------------------------------------------------------------------------------------------
#  Регистрация пользователя
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get("date_of_birth")
            city = form.cleaned_data.get("city")
            email = form.cleaned_data.get("email")
            phone_number = form.cleaned_data.get("phone_number")

            Profile.objects.create(user=user,
                                   date_of_birth=date_of_birth,
                                   city=city,
                                   email=email,
                                   phone_number=phone_number
                                   )

            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "my_blog/register.html", {"form": form})


# ----------------------------------------------------------------------------------------------------------------------
# Главная страница
def home(request):
    if "search_request" in request.GET:
        search_request = request.GET["search_request"]
        multiple_search_request = Q(Q(post_title__icontains=search_request))

        posts = Post.objects.filter(multiple_search_request)

    else:
        posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, "my_blog/home.html", context)


# ----------------------------------------------------------------------------------------------------------------------
# Профиль пользователя
def profile(request):
    return render(request, "my_blog/profile.html")


# ----------------------------------------------------------------------------------------------------------------------
# Редактирование профиля пользователя
class ProfileEditFormView(View):

    def get(self, request, profile_id):
        # if not request.user.has_perm("app_news.change_news"):  # ОТРЕДАКТИРОВАТЬ!!!!
        #     raise PermissionDenied()
        profile = Profile.objects.get(id=profile_id)

        user_form = UserForm(instance=request.user)

        profile_form = ProfileForm(instance=profile)
        return render(request, "my_blog/edit_profile.html",
                      context={"profile_form": profile_form,
                               "user_form": user_form,

                               "profile_id": profile_id})

    def post(self, request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=request.user)

        profile_form = ProfileForm(request.POST, instance=profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile.save()
            return HttpResponseRedirect("/")

        return render(request, "my_blog/edit_profile.html",
                      context={"profile_form": profile_form,
                               "user_form": user_form,

                               "profile_id": profile_id})


# ----------------------------------------------------------------------------------------------------------------------
# Создание записи блога
class PostFormView(View):

    def get(self, request):
        # if not request.user.has_perm("app_news.add_news"):  # ОТРЕДАКТИРОВАТЬ!!!!
        #     raise PermissionDenied()
        post_form = PostForm()

        return render(request, "my_blog/create_post.html",
                      context={"post_form": post_form})

    def post(self, request):
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.post_author = request.user
            instance.save()

            number_of_publications = Profile.objects.get(user=request.user)

            number_of_publications.number_of_publications += 1
            number_of_publications.save()

            return HttpResponseRedirect("/")
        return render(request, "my_blog/create_post.html", context={"post_form": post_form})


# ----------------------------------------------------------------------------------------------------------------------
# Создание пост(ы) через csv файл

class UploadPostFormView(View):

    def get(self, request):
        # if not request.user.has_perm("app_news.add_news"):  # ОТРЕДАКТИРОВАТЬ!!!!
        #     raise PermissionDenied()
        upload_file_form = UploadPostForm()

        return render(request, "my_blog/upload_post_file.html",
                      context={"upload_file_form": upload_file_form})

    def post(self, request):
        upload_file_form = UploadPostForm(request.POST, request.FILES)
        if upload_file_form.is_valid():

            post_file = upload_file_form.cleaned_data["file"].read()
            post_str = post_file.decode("utf-8").split("\n")
            csv_reader = reader(post_str, delimiter=",", quotechar='"')

            for row in csv_reader:
                if len(row) == 3:
                    if row[0] != "Заголовок":
                        Post.objects.create(post_author=request.user,
                                            post_title=row[0],
                                            post_content=row[1],
                                            publication_date=row[2])
            return HttpResponse(content="Посты успешно загружены!", status=200)


# ----------------------------------------------------------------------------------------------------------------------
# Редактирование записи блога


class PostEditFormView(View):

    def get(self, request, post_id):
        # if not request.user.has_perm("app_news.change_news"):  # ОТРЕДАКТИРОВАТЬ!!!!
        #     raise PermissionDenied()

        posts = Post.objects.get(id=post_id)
        post_form = PostForm(instance=posts)
        return render(request, "my_blog/edit_post.html",
                      context={"post_form": post_form, "post_id": post_id})

    def post(self, request, post_id):
        posts = Post.objects.get(id=post_id)
        post_form = PostForm(request.POST, instance=posts)

        if post_form.is_valid():
            posts.save()
            return HttpResponseRedirect("/")

        return render(request, "my_blog/edit_post.html",
                      context={"post_form": post_form, "post_id": post_id})


# ----------------------------------------------------------------------------------------------------------------------
# Страница поста

class PostDetailView(DetailView):
    model = Post
    template_name = 'my_blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(post_id=self.get_object())
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("post_detail",
                            kwargs={"pk": self.get_object().id,
                                    "images": self.get_context_data()})


# ----------------------------------------------------------------------------------------------------------------------

# Загрузка изображений к посту

def multiple_img_upload(request, post_id):
    posts = Post.objects.get(id=post_id)

    images = Image.objects.all()
    upload_images_form = MultipleFilesLoadForm()
    if request.method == 'POST':
        upload_images_form = MultipleFilesLoadForm(request.POST, request.FILES)
        files = request.FILES.getlist('images')
        if upload_images_form.is_valid():

            for img in files:
                gallery = Image(post_id=posts, images=img)
                gallery.save()

            return HttpResponseRedirect('/')

    context = {'upload_images_form': upload_images_form, 'images': images, "post_id": post_id}

    return render(request, 'my_blog/upload_images.html', context)

# ----------------------------------------------------------------------------------------------------------------------
