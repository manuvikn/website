from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Usuario
from django.views import generic

# Create your views here.


def homePage(request):
    data = None
    if request.user.is_authenticated:
        userPk = request.user.pk
        data = Usuario.objects.get(user_id=userPk)



    return render(
        request,
        'index.html',
        context={
            'data': data,
        }
    )

def profile(request, pk):
    return render(
        request,
        'profile.html',
        context={
            'numero': pk,
        }
    )


class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = '__all__'
    #fields = ['fondo', 'letra',]


class UserDetailView(generic.DetailView):
    model = User
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserDetailView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        usuario = context['user'].pk
        num = Usuario.objects.filter(user_id=usuario).count()
        data = Usuario.objects.get(user_id=usuario)


        context['usuario'] = usuario
        context['data'] = data
        context['num'] = num


        return context

class UsuarioCreate(CreateView):
    model = Usuario
    fields = ['fondo', 'letra']


def Apariencia(request):
    return render(
        request,
        'myapp/apariencia.html'
    )

def AparienciaUno(request):
    request.session['fondo'] = 'blue'
    request.session['letra'] = 'yellow'

    return HttpResponseRedirect(reverse('apariencia'))

def AparienciaDos(request):
    request.session['fondo'] = 'green'
    request.session['letra'] = 'pink'

    return HttpResponseRedirect(reverse('apariencia'))