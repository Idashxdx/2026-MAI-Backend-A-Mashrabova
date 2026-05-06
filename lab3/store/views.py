from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def profile(request):
    return JsonResponse({
        "status": "success",
        "data": {
            "username": "test_user",
            "email": "user@example.com"
        }
    })


@require_http_methods(["GET"])
def products(request):
    return JsonResponse({
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Casio G-Shock",
                "price": 12000,
                "category": "sport"
            },
            {
                "id": 2,
                "name": "Seiko Classic",
                "price": 25000,
                "category": "classic"
            }
        ]
    })


@require_http_methods(["GET"])
def category(request):
    return JsonResponse({
        "status": "success",
        "category": "sport",
        "products": [
            {
                "id": 1,
                "name": "Casio G-Shock",
                "price": 12000
            }
        ]
    })


@csrf_exempt
@require_http_methods(["POST"])
def add_favorite(request):
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
