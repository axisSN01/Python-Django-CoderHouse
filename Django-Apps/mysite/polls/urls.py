from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"), # Teacher question: why I can not use question_id here???
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"), # Teacher question: why I can not use question_id here???
    path("<int:question_id>/vote/", views.vote, name="vote"),
]