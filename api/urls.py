from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView ,SpectacularSwaggerView

urlpatterns = [
    path("create_lesson/", views.createLesson.as_view(), name="create_lesson"),
    path("l-crud/<int:pk>", views.lesson_crud.as_view(), name="l-crud"),
    path("buy-lesson/<int:pk>", views.Buylessons.as_view(), name="buy"),
    path("home/", views.seeLessons.as_view(), name="see-lessons"),
    path("see-b-lessons/", views.seeBoughtLessons.as_view(), name=""),
    path("docs/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),
]
