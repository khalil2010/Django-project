from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login

from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def couleur_search(request):
    if request.method == 'POST':
        form = CouleurForm(request.POST)
        if form.is_valid():
            marque = form.cleaned_data['marque']
            modele = form.cleaned_data['voiture']
            color_code = form.cleaned_data['color_code']

            couleurs = voiture.objects.filter(parent=marque, name=modele, code__color_code=color_code)
            formule_peinture = Formule_Base_Couleur.objects.all()

            context = {'form': form, 'couleurs': couleurs, 'formule_peinture': formule_peinture}
            return render(request, 'accueil.html', context)
    else:
        form = CouleurForm()
    context = {'form': form}
    return render(request, 'accueil.html', context)



from django.shortcuts import render, get_object_or_404
from .models import couleur

def couleur_details(request, couleur_id):
    couleur_obj = get_object_or_404(couleur, id=couleur_id)
    formule_couleur = Formule_Base_Couleur.objects.filter(formule=couleur_obj)
    context = {'couleur': couleur_obj,'formule_couleur': formule_couleur}
    return render(request, 'couleur_details.html', context)












def formules_couleurs(request):
    formule_base_couleur_list = Formule_Base_Couleur.objects.all()
    context = {'formule_base_couleur_list': formule_base_couleur_list}
    return render(request, 'accueil.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)    
                return redirect('couleur_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})







def couleur_list(request):
    couleurs = couleur.objects.all()
    return render(request,'couleur_list.html', {'couleurs': couleurs})




def add_couleur(request):
    if request.method == 'POST':
        form = AjoutcouleurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('couleur_list')
    else:
        form = AjoutcouleurForm()
    return render(request, 'add_couleur.html', {'form': form})




def couleur_update(request, couleur_id):
    couleurs = couleur.objects.get(id = couleur_id)
    if request.method == 'POST':
        couleurs.name = request.POST['name']
        couleurs.color_code = request.POST['color_code']
        couleurs.save()
        return redirect('couleur_list')
    return render(request, 'update_couleur.html', {'couleur': couleurs})

def couleur_delete(request, couleur_id):
    couleurs = get_object_or_404(couleur, id=couleur_id)
    if request.method == 'POST':
        couleurs.delete()
        return redirect('couleur_list')
    return render(request, 'couleur_delete.html', {'couleur': couleurs}) 