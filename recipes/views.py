from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse
from recipes.models import Author, Recipe
from .forms import UserRecipeForm, AuthorForm, LoginForm, SignupForm, AdminRecipeForm, EditRecipes
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    recipes = Recipe.objects.all()
    # context = {"title": title}
    return render(request, 'main.html', {"recipes": recipes})


def authors(request, author_id):
    authorInfo = Author.objects.filter(id=author_id).first()
    favorited = authorInfo.favorites.all()
    my_recipes = Recipe.objects.filter(author=author_id)
    context = {"name": authorInfo.name, "bio": authorInfo.bio, "recipes": my_recipes, "favorites": authorInfo.favorites}
    return render(request, 'authorDetail.html', {"details": context, "favorited":favorited})


def favorite_button(request, recipe_id):
    filtered_recipe = Recipe.objects.filter(id=recipe_id).first()
    request.user.author.favorites.add(filtered_recipe)
    return HttpResponseRedirect (request.META.get("HTTP_REFERER", '/'))


def recipes(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, 'recipeDetail.html', {"recipe": recipe})


@login_required
def recipe_form_view(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AdminRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Recipe.objects.create(
                    title=data.get('title'),
                    author=data.get('author'),
                    description=data.get('description'),
                    time_Required=data.get('time_Required'),
                    instructions=data.get('instructions')
                )
                return HttpResponseRedirect(reverse('homepage'))
        form = AdminRecipeForm()
    else:
        if request.method == "POST":
            form = UserRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Recipe.objects.create(
                    title=data.get('title'),
                    author=request.user.author,
                    description=data.get('description'),
                    time_Required=data.get('time_Required'),
                    instructions=data.get('instructions')
                )
                return HttpResponseRedirect(reverse('homepage'))
        form = UserRecipeForm()

    return render(request, "recipe_form.html", {'form': form})


@login_required
def author_form_view(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
            Author.objects.create(name=data.get('username'), user=new_user, bio=data.get('bio'))
            return HttpResponseRedirect(reverse('homepage'))
            
    form = AuthorForm()

    return render(request, 'author_form.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get('username'), password=data.get('password'))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse('homepage'))
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, 'login_form.html', {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get('username'), password=data.get('password'))
            Author.objects.create(name=data.get('username'), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('homepage'))
    
    form = SignupForm()
    return render(request, "signup_form.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def edit_recipe_view(request, recipe_id):
    recipe_instance = Recipe.objects.filter(id=recipe_id).first()
    if request.user.is_staff or request.user.author == recipe_instance.author:
        form = EditRecipes(instance=recipe_instance)
        if request.method == "POST":
            form = EditRecipes(request.POST, instance=recipe_instance)
            form.save()
            return HttpResponseRedirect(reverse('homepage'))
        return render(request, 'generic_form.html', {'form': form})
    else: 
        return HttpResponse('Access Denied.')
        




    