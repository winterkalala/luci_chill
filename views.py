from django.shortcuts import render, redirect
#from django.conf import settings
from django.contrib.auth import authenticate, login
from .forms import registrationForm_Et, loginForm_Et, registrationForm_Us, loginForm_Us, ContactForm
from django.contrib import messages

# Create your views here.
def accueil(request):
    return render(request,"index_1.html")


#Creation et connexion compte utilisateur 
def auth_user(request):
    reg_form = registrationForm_Us()
    login_form = loginForm_Us()
    if request.method == 'POST': 
        if 'register_Us' in request.POST:
            reg_form = registrationForm_Us(request.POST)
            if reg_form.is_valid():
                reg_form.save()
                print(" Utilisateur enregistré avec succès !! ")
                return redirect('homEt')  # Redirection vers la page d'accueil User
            else:
                print(" Utilisateur non-enregistré ECHEC !! ", reg_form.errors)
                return redirect('accueil') # Rediriger sur la page d'accueil initial
        else:
            login_form = loginForm_Us(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                pwd = login_form.cleaned_data['pwd']
                user = authenticate(request, username=username, password=pwd)
                if user is not None:
                    login(request, user)
                    print(" Utilisateur connecté avec succès !! ")
                    return redirect('homUs')  # Redirection vers la page d'accueil
                else:
                    print(" Utilisateur n'a pas pu se connecté !! ")
                    return redirect('accueil') # Rediriger sur la page d'accueil initial
        
    else:
        reg_form = registrationForm_Us()
        login_form = loginForm_Us()

    return render(request, "ConnUs.html", {'reg_form': reg_form, 'login_form': login_form})


#Creation et connexion compte Etablissement 
def auth_view(request):
    reg_form = registrationForm_Et()
    login_form = loginForm_Et()
    if request.method == 'POST':
        if 'register_Et' in request.POST:
            reg_form = registrationForm_Et(request.POST)
            if reg_form.is_valid():
                reg_form.save()               
                return redirect('homEt')  # Redirection vers la page d'accueil Etablissement
            else:
                return redirect('accueil') # Rediriger sur la page d'accueil initial
        else:
            login_form = loginForm_Et(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                pwd = login_form.cleaned_data['pwd']
                user = authenticate(request, username=username, password=pwd)
                if user is not None:
                    login(request, user)
                    return redirect('homEt')  # Redirection vers la page d'accueil
              
    else:
        reg_form = registrationForm_Et()
        login_form = loginForm_Et()
    
    return render(request, 'ConnEt.html', {'reg_form': reg_form, 'login_form': login_form})



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            # Traitement du formulaire (envoi d'email, sauvegarde en BDD, etc.)
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Exemple: sauvegarde en base de données
            # Contact.objects.create(
            #     full_name=full_name,
            #     email=email,
            #     subject=subject,
            #     message=message
            # )
            
            messages.success(request, 'Votre message a été envoyé avec succès ! Nous vous répondrons dans les plus brefs délais.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'contact_form': form})


# Accueil Etablissement 
def homEt(request):
    return render(request,"home_one.html")

#Accueil UserOrdi
def homUs(request):
    return render(request,"home_two.html")

#Page categori Visiteur 
def Catevis(request):
    return render(request,"cate_vis.html")

#Page categorie UserOrdi
def Cateus(request):
    return render(request,"cate_us.html")


#Page Voir plus Visiteur 
def Voisiteur(request):
    return render(request, "voir_vis.html")

#Page Voir plus Utilisateur 
def Voisateur(request):
    return render(request, "voir_us.html")

#Page Publication etablissement et formulaire 
def PublicEt(request): 
    return render(request, "pub_one.html")

#Page Publication visiteur
def visitep(request): 
    return render(request, "pubisiteur.html")

#Page Publication visiteur
def utilip(request): 
    return render(request, "pubisateur.html")




