from django.urls import path
from .views import signup_view

urlpatterns = [
    path('<path:name>/<str:last_name>/<int:age>/', signup_view)
]
