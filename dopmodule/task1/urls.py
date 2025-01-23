from django.contrib import admin
from django.urls import path
from .views import main, magazine, cart, sign_up_by_html, sign_up_by_django

app_name = 'myapp_admin'
urlpatterns = [
    path('admin1/', admin.site.urls),
    path('', main),
    path('catalog/', magazine),
    path('cart/', cart),
    path('sign_by_html/', sign_up_by_html),
    path('sign_by_django/', sign_up_by_django),
]
