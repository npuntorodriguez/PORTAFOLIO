from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db import connection

from .models import Proyecto, Habilidad
from .forms import ProyectoForm


# ---------------------------------------------------------
# PÁGINAS PÚBLICAS
# ---------------------------------------------------------

def index(request):
    return render(request, "index.html")


def habilidades(request):
    habilidades = Habilidad.objects.all()
    return render(request, "habilidades.html", {"habilidades": habilidades})


def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, "proyectos.html", {"proyectos": proyectos})


def contacto(request):
    return render(request, "contacto.html")


# ---------------------------------------------------------
# AUTENTICACIÓN
# ---------------------------------------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect("index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    messages.info(request, "Has cerrado sesión.")
    return redirect("login")


# ---------------------------------------------------------
# CRUD — SOLO ADMINISTRADORES (STAFF)
# ---------------------------------------------------------

@staff_member_required
def crear_proyecto(request):
    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto creado correctamente.")
            return redirect("proyectos")
    else:
        form = ProyectoForm()

    return render(request, "proyectos/crear_proyecto.html", {"form": form})


@staff_member_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == "POST":
        form = ProyectoForm(request.POST, request.FILES, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, "Proyecto actualizado correctamente.")
            return redirect("proyectos")
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, "proyectos/editar_proyecto.html", {"form": form, "proyecto": proyecto})


@staff_member_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == "POST":
        proyecto.delete()
        messages.success(request, "Proyecto eliminado.")
        return redirect("proyectos")

    return render(request, "proyectos/eliminar_proyecto.html", {"proyecto": proyecto})


# ---------------------------------------------------------
# REPORTE SQL — SOLO ADMIN
# ---------------------------------------------------------

@staff_member_required
def consulta_sql(request):

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT p.id, p.titulo, h.nombre, h.experiencia
            FROM proyectos_proyecto p
            JOIN proyectos_proyecto_habilidades ph ON p.id = ph.proyecto_id
            JOIN proyectos_habilidad h ON h.id = ph.habilidad_id
            ORDER BY p.fecha_publicacion DESC;
        """)
        resultados = cursor.fetchall()

    return render(request, "sql.html", {"resultados": resultados})