from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from django.core.exceptions import MultipleObjectsReturned


# Vista para la página principal
def home(request):

    # Obteniendo todos los miembros del equipo
    teams = Team.objects.all()

    # Obteniendo todos los autos destacados y ordenándolos por fecha de creación
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)

    # Obteniendo todos los autos y ordenándolos por fecha de creación
    all_cars = Car.objects.order_by('-created_date')

    # Para el formulario de búsqueda
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    # Preparando el contexto para enviar a la plantilla
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }

    # Renderizando la plantilla de la página principal con el contexto
    return render(request, 'pages/home.html', data)

# Vista para la página de "About"
def about(request):
    teams = Team.objects.all()

    data = {
        'teams': teams,
    }

    return render(request, 'pages/about.html', data)

# Vista para la página de "Services"
def services(request):
    return render(request, 'pages/services.html')

# Vista para la página de "Contact"
def contact(request):

    # Si la petición es POST, procesamos el formulario
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        # Intentamos obtener el correo electrónico del administrador
        try:
            admin_info = User.objects.get(is_superuser=True)
        except MultipleObjectsReturned:
            # Si hay múltiples superusuarios, obtenemos el primero
            admin_info = User.objects.filter(is_superuser=True).first()
        finally:
            admin_email = admin_info.email
        

        # Preparando el correo para enviar
        email_subject = "You have a new message from Carzone website regarding " + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        # Enviamos el correo electrónico
        # - email_subject: Asunto del correo
        # - message_body: Cuerpo del mensaje
        # - "luisestebansantamaria@outlook.com": El correo desde el cual se envía
        # - [admin_email]: Lista de destinatarios. Solo se envía al correo del administrador en este caso
        # - fail_silently=False: Si ocurre un error al enviar el correo, se levantará una excepción
        send_mail(
                email_subject,
                message_body,
                "luisestebansantamaria@outlook.com", 
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly.')
        return redirect('pages:contact')
        
    return render(request, 'pages/contact.html')