from django.urls import path
from .views import home, upload, salvar, editar, update, delete

urlpatterns = [
    path('', home),
    path('upload/', upload, name='upload'),
    path('salvar/', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]