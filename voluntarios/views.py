from django.utils.timezone import now
from .models import Evento, Voluntario
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AsignarEventosForm, AsignarVoluntariosForm, EventoForm, VoluntarioForm

def dashboard(request):
    eventos = Evento.objects.filter(fecha__gte=now().date()).order_by('fecha')
    return render(request, 'dashboard.html', {'eventos': eventos})


def detalle_evento(request, id):
    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':
        form = AsignarVoluntariosForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', id=evento.id)
    else:
        form = AsignarVoluntariosForm(instance=evento)

    return render(request, 'detalle_evento.html', {
        'evento': evento,
        'form_asignar': form
    })

def editar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('detalle_evento', id=evento.id)
    else:
        form = EventoForm(instance=evento)

    return render(request, 'editar_evento.html', {
        'form': form,
        'evento': evento
    })


def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventoForm()

    return render(request, 'crear_evento.html', {'form': form})

def editar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)

    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        form_asignar = AsignarEventosForm(request.POST)

        if form.is_valid() and form_asignar.is_valid():
            form.save()
            voluntario.eventos.set(form_asignar.cleaned_data['eventos'])
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm(instance=voluntario)
        form_asignar = AsignarEventosForm(
            initial={'eventos': voluntario.eventos.all()}
        )

    return render(request, 'editar_voluntario.html', {
        'form': form,
        'form_asignar': form_asignar,
        'voluntario': voluntario
    })


def borrar_evento(request, id):
    evento = get_object_or_404(Evento, id=id)

    if request.method == 'POST':
        evento.delete()
        return redirect('dashboard')

    return render(request, 'borrar_evento_confirm.html', {'evento': evento})


def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all().order_by('-fecha_registro')
    return render(request, 'lista_voluntarios.html', {'voluntarios': voluntarios})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_voluntarios')
    else:
        form = VoluntarioForm()

    return render(request, 'crear_voluntario.html', {'form': form})


def borrar_voluntario(request, id):
    voluntario = get_object_or_404(Voluntario, id=id)

    if request.method == 'POST':
        voluntario.delete()
        return redirect('lista_voluntarios')

    return render(request, 'borrar_voluntario_confirm.html', {
        'voluntario': voluntario
    })
