from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name='homepage'),
    path('post/<int:id>', views.single_page, name='single')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

