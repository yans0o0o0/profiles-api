from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
