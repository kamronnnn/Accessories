from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, GamingBuilds, LapTop, Keyboard, Armchair, Mice, Monitor

from .forms import LoginForm, RegisterForm, CommentForm

from .utils import CartAuthenticatedUser


# Create your views here.

def index(request):
    context = {
        'categories': Category.objects.all(),
        'gamingbuilds': GamingBuilds.objects.all(),
        'laptops': LapTop.objects.all(),
        'keyboards': Keyboard.objects.all(),
        'armchairs': Armchair.objects.all(),
        'mices': Mice.objects.all(),
        'monitors': Monitor.objects.all()
    }

    return render(request, 'shop/index.html', context)


def gaming_build_detail(request, gaming_id):
    gaming_build = GamingBuilds.objects.get(pk=gaming_id)
    form = CommentForm()

    context = {
        'gaming_build': gaming_build,
        'form': form
    }
    return render(request, 'shop/gaming_detail.html', context)


def laptop_detail(request, laptop_id):
    laptop = LapTop.objects.get(pk=laptop_id)
    form = CommentForm()

    context = {
        'laptop': laptop,
        'form': form
    }
    return render(request, 'shop/laptop_detail.html', context)


def armchair_detail(request, armchair_id):
    armchair = Armchair.objects.get(pk=armchair_id)
    form = CommentForm()

    context = {
        'armchair': armchair,
        'form': form
    }
    return render(request, 'shop/armchair_detail.html', context)


def mice_detail(request, mice_id):
    mice = Mice.objects.get(pk=mice_id)
    form = CommentForm()

    context = {
        'mice': mice,
        'form': form
    }
    return render(request, 'shop/mice_detail.html', context)


def keyboard_detail(request, keyboard_id):
    keyboard = Keyboard.objects.get(pk=keyboard_id)
    form = CommentForm()

    context = {
        'keyboard': keyboard,
        'form': form
    }
    return render(request, 'shop/keyboard_detail.html', context)


def monitor_detail(request, monitor_id):
    monitor = Monitor.objects.get(pk=monitor_id)
    form = CommentForm()

    context = {
        'monitor': monitor,
        'form': form
    }
    return render(request, 'shop/monitor_detail.html', context)


def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'shop/user_login.html', context)


def register(request):
    form = RegisterForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')

    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'shop/register.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def all_products(request):
    context = {
        'categories': Category.objects.all(),
        'gamingbuilds': GamingBuilds.objects.all(),
        'laptops': LapTop.objects.all(),
        'keyboards': Keyboard.objects.all(),
        'armchairs': Armchair.objects.all(),
        'mices': Mice.objects.all(),
        'monitors': Monitor.objects.all()
    }

    return render(request, 'shop/all_products.html', context)


def filter_by_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    gamingbuilds = GamingBuilds.objects.filter(category=category)
    laptops = LapTop.objects.filter(category=category)
    keyboards = Keyboard.objects.filter(category=category)
    armchairs = Armchair.objects.filter(category=category)
    mices = Mice.objects.filter(category=category)
    monitors = Monitor.objects.filter(category=category)

    context = {
        'category': category,
        'gamingbuilds': gamingbuilds,
        'laptops': laptops,
        'keyboards': keyboards,
        'armchairs': armchairs,
        'mices': mices,
        'monitors': monitors
    }
    return render(request, 'shop/filter_by_category.html', context)




def cart(request):
    cart_info = CartAuthenticatedUser(request)
    context = {
        'order_products': cart_info.get_cart_info()['order_products']
    }
    return render(request, 'shop/cart.html', context)


def to_cart(request, gaming_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, gaming_id, action)
    return redirect('index')



