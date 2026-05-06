from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Category, Watch, Favorite


@require_http_methods(["GET"])
def profile(request):
    user = User.objects.first()

    if user is None:
        return JsonResponse({
            "status": "success",
            "data": None
        })

    return JsonResponse({
        "status": "success",
        "data": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    })


@require_http_methods(["GET"])
def products(request):
    watches = Watch.objects.all()

    data = []

    for watch in watches:
        data.append({
            "id": watch.id,
            "name": watch.name,
            "price": watch.price,
            "category": watch.category.name
        })

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
            products.append({
                "id": watch.id,
                "name": watch.name,
                "price": watch.price
            })

        data.append({
            "id": category_item.id,
            "name": category_item.name,
            "products": products
        })

    return JsonResponse({
        "status": "success",
        "data": data
    })


@csrf_exempt
@require_http_methods(["POST"])
def add_favorite(request):
    user = User.objects.first()
    watch_id = request.POST.get('watch_id')

    if user is None:
        return JsonResponse({
            "status": "error",
            "message": "user not found"
        })

    watch = Watch.objects.get(id=watch_id)

    Favorite.objects.create(
        user=user,
        watch=watch
    )

    return JsonResponse({
        "status": "success",
        "message": "watch added to favorite"
    })


@require_http_methods(["GET"])
def web_main(request):
    return JsonResponse({
        "status": "success",
        "message": "main page"
    })
