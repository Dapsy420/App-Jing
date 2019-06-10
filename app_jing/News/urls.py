from django.urls import path
from django.views.generic import TemplateView

app_name = 'news'

urlpatterns = [
    path('', TemplateView.as_view(template_name="Noticias/baseNoticias.html"), name='non-auth-news'),
]
