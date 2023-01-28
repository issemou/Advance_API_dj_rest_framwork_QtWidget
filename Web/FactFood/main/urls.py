from django.urls import path, include
from main import views
from main.Api_routes import router

urlpatterns = [
    path('api/', include(router.urls)),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]
