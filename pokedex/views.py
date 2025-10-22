from django.shortcuts import render

# Create your views here.
def index(request):
    pokemons = ['Pikachu', 'Charmander', 'Bulbasaur', 'Squirtle', 'Eevee', 'Jigglypuff']
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_details(request, pokemon):
    return render(request, 'pokemon_details.html', {'pokemon': pokemon})