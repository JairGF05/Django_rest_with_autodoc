from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
#registrar
router.register('programmers', views.ProgrammerViewSet)

urlpatterns = router.urls