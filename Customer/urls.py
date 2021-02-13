from django.contrib import admin
from django.urls import path,include
from detail import viewsets
from rest_framework.routers import DefaultRouter  # automatic URL routing to Django
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

"""
 It will keep track of the view sets we register 
 and the urls property will generate all the url patterns required for those view sets to work.
"""

router=DefaultRouter()    #Creating Router Objects
router.register('user',viewsets.UserViewSet,basename='user')   
#router.register('profile',viewsets.ProfileViewSet,basename='profile') 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
   
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))

 
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
