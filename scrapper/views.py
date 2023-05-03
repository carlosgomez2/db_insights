import json
from django.http import JsonResponse


def scrape(request):
    print(request)

    context = {
        'message': 'Scrapping data from the web',
        'code': 200,
    }

    json_data = json.dumps(context)

    return JsonResponse(json_data, safe=False)
