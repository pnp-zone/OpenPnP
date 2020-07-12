from django.urls import path
from dashboard.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('gamemaster', GameMasterView.as_view()),
    path('template', TemplatesView.as_view()),
    path('create_template', CreateTemplateView.as_view()),
    path('player', PlayerView.as_view()),
]