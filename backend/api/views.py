from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body
    print(body)
    print(request.GET)
    return JsonResponse({"message": "hey, saul"})

