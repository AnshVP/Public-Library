from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Admin  
    path("admin/", admin.site.urls),
    # path("base/", views.BASE, name="base"),
    path("login/", views.LOGIN, name="login"),
    path("", views.BASE, name="base"),
    path("doLogin/", views.doLogin, name="doLogin"),
    path("doLogout/", views.doLogout, name="logout"),
    path("Profile/", views.PROFILE, name="profile"),
    path("Profile/update/", views.PROFILE_UPDATE, name= "profile_update"),
    path("Search/books/", views.FETCH_BOOK_DATA, name= "search_query"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
