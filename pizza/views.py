from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPizzaForm, EatPizzaForm
from .models import Pizza
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    context = {'pizzas': Pizza.objects.all()}
    return render(request, 'pizza/index.html', context)

# Make pizza show route only accessible to logged in users
# @login_required
# def show(request, pizza_id):
#     # Implicitely says that the first pizza in list has id of 1
#     # The .objects retrieves instances of the Pizza class
#     context = {'pizza': Pizza.objects.get(pk=pizza_id)}
#     return render(request, 'pizza/show.html', context)

@login_required
def create(request):
    # When the form is submitted in the template, we set the method='POST'
    if request.method == 'POST':
        pizza = NewPizzaForm(request.POST)
        if pizza.is_valid():
            pizza_id = pizza.save().id 
            return HttpResponseRedirect(f'/pizzas/{pizza_id}')
    else:
        form = NewPizzaForm()
    data = {'form': form }
    return render(request, 'pizza/new.html', data)

@login_required
def show2(request, pizza_id):
    pizza = get_object_or_404(Pizza, pk=pizza_id)
    if request.method == 'POST':
        form = EatPizzaForm(request.POST)
        if form.is_valid():
            if pizza.eater == request.user:
                pizza.eater = None
                pizza.save()
                return HttpResponseRedirect(f'/pizzas/{pizza_id}')
            else:
                pizza.eater = request.user
                pizza.save()
                return HttpResponseRedirect(f'/pizzas/{pizza_id}')
    else:
        # Not sure what this bit does
        form = EatPizzaForm(initial={'eater': request.user})
    data = { 'pizza': pizza, 'form': form }
    return render(request, 'pizza/show.html', data)
    # Form added, view added, look at template before trying out

def handler404(request, exception):
    data = {'err': exception}
    return render(request, 'pizza/404.html', data)

def handler500(request):
    return render(request, 'pizza/500.html')