from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from mainapp.models import Ideas
from mainapp.serializers import IdeasSerializer


@csrf_exempt
def idea_list(request):
    if request.method == 'GET':
        ideas = Ideas.objects.all()
        serializer = IdeasSerializer(ideas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdeasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def idea_detail(request, pk):
    try:
        idea = Ideas.objects.get(pk=pk)
    except Ideas.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IdeasSerializer(idea)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IdeasSerializer(idea, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        idea.delete()
        return HttpResponse(status=204)
