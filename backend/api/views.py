import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs): # this is django HttpRequest
    # request.body

    print(request.GET)
    body = request.body  # a bite string of json data -- need to convert it to json
    data = {}
    try:
        data = json.loads(body) # string of json data => python dict
    except:
        pass

    print(data)
    data['params'] = request.GET
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)