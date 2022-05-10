from django.urls import path

from backend.search import views

urlpatterns = [path("", views.SearchListView.as_view(), name="search")]
