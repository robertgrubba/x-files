from django.urls import path
from person import views
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views

app_name='person'

urlpatterns = [ 
    path('login/', auth_views.LoginView.as_view(template_name='person/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='person:login'),name='logout'),
    path('',views.PersonListView.as_view(),name='list'),
    path('<int:pk>/',views.PersonDetailView.as_view(),name='detail'),
    path('note/create/<int:pk>',views.NoteCreate.as_view(),name='create-note'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
