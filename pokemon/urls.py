from django.urls import path
from .views import PokemonList, PokemonDetail

urlpatterns = [
    path('', PokemonList.as_view(), name='pokemon_list'),
    path('<int:pk>', PokemonDetail.as_view(), name='pokemon_detail')
]