from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register("meals", MealViewSet)
router.register("ratings", RateViewSet)
router.register("users", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
