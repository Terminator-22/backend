from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Project', ProjectViewset, basename='Project')
urlpatterns = router.urls



#urlpatterns = [
#   path('', home)
#]
