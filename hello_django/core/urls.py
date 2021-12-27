from . import views
from django.urls import path

urlpatterns = [
    path('somar/<int:a>/<int:b>', views.somar),
    path('subt/<int:a>/<int:b>', views.subtrair),
    path('mult/<int:a>/<int:b>', views.multiplicar),
    path('div/<int:a>/<int:b>', views.dividir),
]