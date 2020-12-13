from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from knox import views as knox_views
from . import views

router = routers.DefaultRouter()
router.register(r'articles', views.ArticlesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login', views.LoginApiView.as_view(), name = 'api login'),
    path('logout', knox_views.LogoutView.as_view(), name = 'logout'),
]