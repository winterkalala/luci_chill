from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views
#from .views import auth_view

urlpatterns=[
    path("",views.accueil,name='accueil'),
    path("auth/result_1",views.auth_view,name="auth_view"),
    path("auth/result_2",views.auth_user,name="auth_user"),
    path("result_3",views.homEt,name="homEt"),
    path("result_4",views.homUs,name="homUs"),
    path("result_5",views.Catevis,name="Catevis"),
    path("result_6",views.Cateus,name="Cateus"),
    path("result_7",views.Voisiteur,name="Voisiteur"),
    path("result_8",views.Voisateur,name="Voisateur"),
    path("result_9",views.PublicEt,name="PublicEt"), 
    path("result_10",views.visitep,name="visitep"), 
    path("result_11",views.utilip,name="utilip"), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

