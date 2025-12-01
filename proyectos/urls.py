from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("habilidades/", views.habilidades, name="habilidades"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),

    # Autenticación
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # CRUD protegido
    path("proyectos/crear/", views.crear_proyecto, name="crear_proyecto"),
    path("proyectos/editar/<int:pk>/", views.editar_proyecto, name="editar_proyecto"),
    path("proyectos/eliminar/<int:pk>/", views.eliminar_proyecto, name="eliminar_proyecto"),

    # Reporte SQL
    path("reportes/sql/", views.consulta_sql, name="consulta_sql"),
]