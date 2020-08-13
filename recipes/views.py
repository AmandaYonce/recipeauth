from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from .forms import RecipeForm, AuthorForm

def home(request):
    recipes = Recipe.objects.all()
    # context = {"title": title}
    return render(request, 'main.html', {"recipes": recipes})


def authors(request, author_id):
    authorInfo = Author.objects.filter(id=author_id).first()
    my_recipes = Recipe.objects.filter(author=author_id)
    context = {"name": authorInfo.name, "bio": authorInfo.bio, "recipes": my_recipes}
    return render(request, 'authorDetail.html', {"details": context})


def recipes(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipeDetail.html', {"recipe": recipe})


def recipe_form_view(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_Required=data.get('timr_Required'),
                instructions=data.get('instructions')
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = RecipeForm()

    return render(request, "recipe_form.html", {'form': form})

def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data.get('name'),
                bio = data.get('bio')
            )
            return HttpResponseRedirect(reverse('homepage'))
            
    form = AuthorForm()

    return render(request, 'author_form.html', {'form': form})