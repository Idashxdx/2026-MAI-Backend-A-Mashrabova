from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Category, Watch


def watch_to_dict(watch):
    return {
        "id": watch.id,
        "name": watch.name,
        "description": watch.description,
        "price": watch.price,
        "category": watch.category.name
    }


def category_to_dict(category):
    return {
        "id": category.id,
        "name": category.name
    }


@require_http_methods(["GET"])
def profile(request):
    User = get_user_model()
    user = User.objects.first()

    if user is None:
        return JsonResponse({
            "status": "error",
            "message": "user not found"
        })

    favorites = []

    for watch in user.favorites.all():
        favorites.append(watch_to_dict(watch))

    return JsonResponse({
        "status": "success",
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "favorites": favorites
        }
    })


@require_http_methods(["GET"])
def products(request):
    watches = Watch.objects.all()

    data = []

    for watch in watches:
        data.append(watch_to_dict(watch))

    return JsonResponse({
        "status": "success",
        "data": data
    })


@require_http_methods(["GET"])
def category(request):
    categories = Category.objects.all()

    data = []

    for category_item in categories:
        watches = Watch.objects.filter(category=category_item)

        products = []

        for watch in watches:
            products.append(watch_to_dict(watch))

        data.append({
            "id": category_item.id,
            "name": category_item.name,
            "products": products
        })

    return JsonResponse({
        "status": "success",
        "data": data
    })


@require_http_methods(["GET"])
def category_detail(request, category_id):
    category_item = Category.objects.get(id=category_id)
    watches = Watch.objects.filter(category=category_item)

    products = []

    for watch in watches:
        products.append(watch_to_dict(watch))

    return JsonResponse({
        "status": "success",
        "data": {
            "id": category_item.id,
            "name": category_item.name,
            "products": products
        }
    })


@require_http_methods(["GET"])
def watch_detail(request, watch_id):
    watch = Watch.objects.get(id=watch_id)

    return JsonResponse({
        "status": "success",
        "data": watch_to_dict(watch)
    })


@csrf_exempt
@require_http_methods(["POST"])
def add_favorite(request):
    User = get_user_model()
    user = User.objects.first()
    watch_id = request.POST.get('watch_id')

    if user is None:
        return JsonResponse({
            "status": "error",
            "message": "user not found"
        })

    watch = Watch.objects.get(id=watch_id)
    user.favorites.add(watch)

    return JsonResponse({
        "status": "success",
        "message": "watch added to favorite"
    })


@require_http_methods(["GET"])
def search(request):
    q = request.GET.get('q', '')

    watches = Watch.objects.filter(
        Q(name__icontains=q) | Q(description__icontains=q)
    )

    data = []

    for watch in watches:
        data.append(watch_to_dict(watch))

    return JsonResponse({
        "status": "success",
        "data": data
    })


@require_http_methods(["GET"])
def watches(request):
    watches = Watch.objects.all()

    data = []

    for watch in watches:
        data.append(watch_to_dict(watch))

    return JsonResponse({
        "status": "success",
        "data": data
    })


@csrf_exempt
@require_http_methods(["POST"])
def create_watch(request):
    name = request.POST.get('name')
    description = request.POST.get('description', '')
    price = request.POST.get('price')
    category_id = request.POST.get('category_id')

    category = Category.objects.get(id=category_id)

    watch = Watch.objects.create(
        name=name,
        description=description,
        price=price,
        category=category
    )

    return JsonResponse({
        "status": "success",
        "data": watch_to_dict(watch)
    })


@require_http_methods(["GET"])
def web_main(request):
    return JsonResponse({
        "status": "success",
        "message": "watch store main page"
    })
