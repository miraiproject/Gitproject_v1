from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.top_page, name='top_page'),
    path('nakabayashi',views.nakabayashi,name='nakabayashi'),
    path('takeuti',views.takeuti,name='takeuti'),
    path('yamada',views.yamada,name='yamada'),
    path('ogasawara',views.ogasawara,name='ogasawara'),
    
]