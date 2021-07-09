from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = "NoticeBoard"
urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path("", views.index, name = "index"),
    path("past", views.past, name = "past"),
    path("future", views.future, name = "future"),
    path("searchPresent", views.modIndex, name = "modIndex"),
    path("searchPast", views.modPast, name = "modPast"),
    path("searchFuture", views.modFuture, name = "modFuture")
]