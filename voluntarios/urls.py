from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Eventos
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/<int:id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:id>/editar/', views.editar_evento, name='editar_evento'),
    path('evento/<int:id>/borrar/', views.borrar_evento, name='borrar_evento'),

    # Voluntarios
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/crear/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/<int:id>/editar/', views.editar_voluntario, name='editar_voluntario'),
    path('voluntarios/<int:id>/borrar/', views.borrar_voluntario, name='borrar_voluntario'),
]


