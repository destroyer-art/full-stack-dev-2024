from django.shortcuts import render
from django.http import JsonResponse
from .models import fda_data, eudamed_data

# Search view for the web page
def search_device(request):
    query = request.GET.get('device_name', '').strip()
    # Case-insensitive search for device_name in both tables
    fda_results = fda_data.objects.all().filter(device_name__iexact=query).values("device_name", "manufacturer_name").distinct()
    eudamed_results = eudamed_data.objects.filter(device_name__iexact=query).values("device_name", "manufacturer_name").distinct()
   
    context = {
        'query': query,
        'fda_results': fda_results,
        'eudamed_results': eudamed_results,
        'not_found_in_fda': not fda_results.exists(),
        'not_found_in_eudamed': not eudamed_results.exists(),
    }

    return render(request, 'devices/search_results.html', context)

# API endpoint to return search results in JSON format
def api_search_device(request):
    query = request.GET.get('device_name', '').strip()

    fda_results = fda_data.objects.filter(device_name__iexact=query)
    eudamed_results = eudamed_data.objects.filter(device_name__iexact=query)

    data = {
        'device_name': query,
        'fda_results': list(fda_results.values('device_name', 'manufacturer_name')),
        'eudamed_results': list(eudamed_results.values('device_name', 'manufacturer_name')),
    }

    return JsonResponse(data)