import dj_rest_auth.views
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSets)
router.register(r'post_2', views.PostViewSetsAlternate, basename='post_2')
