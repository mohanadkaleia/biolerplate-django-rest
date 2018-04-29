from django.conf.urls import url, include
from rest_framework import routers
from project.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'universities', views.UniversityViewSet)
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'customview', views.CustomView.as_view()),
    url(r'^docs/', schema_view),
]
