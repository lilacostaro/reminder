from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Lista
from .forms import ListaForm
from django.contrib import messages
import datetime
from django.db.models import Sum
import json

@login_required
def itemList(request):
    item_list = Lista.objects.filter(user=request.user, done='Comprar').order_by('-created_at')

    paginator = Paginator(item_list, 20)

    page = request.GET.get('page')

    items = paginator.get_page(page)

    return render(request, 'lista/list.html', {'items': items})
@login_required
def history(request):
    search = request.GET.get('search')

    if search:
        items = Lista.objects.filter(produto__icontains=search, user=request.user, done='Comprado')
    else:
        items_list = Lista.objects.filter(user=request.user, done='Comprado').order_by('-created_at')

        paginator = Paginator(items_list, 20)

        page = request.GET.get('page')
        items = paginator.get_page(page)

    return render(request, 'lista/history.html', {'items': items})

@login_required
def listaView(request, id):
    lista = get_object_or_404(Lista, pk=id)
    return render(request, 'lista/produto.html', {'lista':lista})

@login_required
def newItem(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)

        if form.is_valid():
            item = form.save(commit=False)
            item.done = 'Comprar'
            item.user = request.user
            item.save()
            messages.info(request, 'Item adicionado com Sucesso')
            return redirect('/')
    else:
        form = ListaForm()
        return render(request, 'lista/additem.html', {'form':form})

@login_required()
def editItem(request, id):
    item = get_object_or_404(Lista, pk=id)
    form = ListaForm(instance=item)

    if(request.method == 'POST'):
        form = ListaForm(request.POST, instance=item)

        if (form.is_valid()):
            item.save()

            messages.info(request, 'Item editado com Sucesso')

            return redirect('/')
        else:
            return render(request, 'lista/edititem.html', {'form': form, 'item': item})
    else:
        return render(request, 'lista/edititem.html', {'form': form, 'item': item})

@login_required
def deleteItem(request, id):
    item = get_object_or_404(Lista, pk=id)
    item.delete()

    messages.info(request, 'Item deletado com Sucesso')

    return redirect('/')

@login_required
def changeStatus(request, id):
    item = get_object_or_404(Lista, pk=id)

    if(item.done == 'Comprar'):
        item.done = 'Comprado'
    else:
        item.done = 'Comprar'

    item.save()

    return redirect('/')

@login_required()
def dashboard(request):
    valorGastoRecently = Lista.objects.filter(user=request.user, valor__isnull=False,
                                              updated_at__gt=datetime.datetime.now() - datetime.timedelta(
                                                  days=30)).aggregate(Sum('valor'))
    itensComprar = Lista.objects.filter(user=request.user, done='Comprar').count()
    itensComprado = Lista.objects.filter(user=request.user, done='Comprado').count()


    return render(request, 'lista/dashboard.html', {'valorgastorecently': valorGastoRecently, 'itenscomprar': itensComprar, 'itenscomprado': itensComprado})
