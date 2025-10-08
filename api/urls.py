from django.urls import path
from . import views

urlpatterns = [
    path("c_lesson/", views.createLesson.as_view(), name="c_lesson"),
    path("l-crud/<int:pk>", views.lesson_crud.as_view(), name="l-crud"),
    path("buy-lesson/<int:pk>", views.Buylessons.as_view(), name="buy"),
    path("home/", views.seeLessons.as_view(), name="see-lessons"),
    path("see-b-lessons/", views.seeBoughtLessons.as_view(), name="")
]
