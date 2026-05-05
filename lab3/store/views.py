from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def profile(request):
    return JsonResponse({"message": "user profile"})


@require_http_methods(["GET"])
def products(request):
    return JsonResponse({"message": "watch list"})


@require_http_methods(["GET"])
def category(request):
    return JsonResponse({"message": "category page"})


@csrf_exempt
@require_http_methods(["POST"])
def add_favorite(request):
    return JsonResponse({"message": "added to favorite"})


@require_http_methods(["GET"])
def web_main(request):
    return JsonResponse({"message": "main page"})
