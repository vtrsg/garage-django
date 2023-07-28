from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

import os

from .models import (
    User,
    Brand,
    ModelType,
    Year,
    Car,
)
from .serializers import (
    UserSerializer,
    BrandSerializer,
    ModelTypeSerializer,
    YearSerializer,
    CarSerializer,
)

@csrf_exempt
def UserApi(req, id=0):
    if req.method == 'GET':
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return JsonResponse(users_serializer.data, safe=False)    
    elif req.method == 'POST':
        user_data = JSONParser().parse(req)
        user_serializer = UserSerializer(data=user_data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        user_data = JSONParser().parse(req)
        user = User.objects.get(id=id)
        
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            user = User.objects.get(id=id)
            user.delete()
            return JsonResponse({'message': 'Deleted successfully!!'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid method'}, status=400)

@csrf_exempt
def BrandApi(req, id=0):
    if req.method == 'GET':
        brand = Brand.objects.all()
        brands_serializer = BrandSerializer(brand, many=True)

        return JsonResponse(brands_serializer.data, safe=False)    
    elif req.method == 'POST':
        brand_data = JSONParser().parse(req)
        brand_serializer = BrandSerializer(data=brand_data)

        if brand_serializer.is_valid():
            brand_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        brand_data = JSONParser().parse(req)
        brand = Brand.objects.get(id=id)
        
        brand_serializer = BrandSerializer(brand, data=brand_data)
        if brand_serializer.is_valid():
            brand_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            brand = Brand.objects.get(id=id)
            brand.delete()
            
            return JsonResponse('Deleted successfully!!', safe=False)
        except Brand.DoesNotExist:
            return JsonResponse('Brand not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)

@csrf_exempt
def ModelTypeApi(req, id=0):
    if req.method == 'GET':
        model = ModelType.objects.all()
        models_serializer = ModelTypeSerializer(model, many=True)

        return JsonResponse(models_serializer.data, safe=False)    
    elif req.method == 'POST':
        model_data = JSONParser().parse(req)
        model_serializer = ModelTypeSerializer(data=model_data)

        if model_serializer.is_valid():
            model_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        model_data = JSONParser().parse(req)
        model = ModelType.objects.get(id=id)
        
        model_serializer = ModelTypeSerializer(model, data=model_data)
        if model_serializer.is_valid():
            model_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            model = ModelType.objects.get(id=id)
            model.delete()

            return JsonResponse('Deleted successfully!!', safe=False)
        except ModelType.DoesNotExist:
            return JsonResponse('Model not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)

@csrf_exempt
def YearApi(req, id=0):
    if req.method == 'GET':
        year = Year.objects.all()
        years_serializer = YearSerializer(year, many=True)

        return JsonResponse(years_serializer.data, safe=False)    
    elif req.method == 'POST':
        year_data = JSONParser().parse(req)
        year_serializer = YearSerializer(data=year_data)

        if year_serializer.is_valid():
            year_serializer.save()

            return JsonResponse('Added successfully!!', safe=False)
        
        return JsonResponse('Failed add!!', safe=False) 
    elif req.method == 'PUT':
        year_data = JSONParser().parse(req)
        year = Year.objects.get(id=id)
        
        year_serializer = YearSerializer(year, data=year_data)
        if year_serializer.is_valid():
            year_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        
        return JsonResponse('Failed update!!', safe=False) 
    elif req.method == 'DELETE':
        try:
            year = Year.objects.get(id=id)
            year.delete()

            return JsonResponse('Deleted successfully!!', safe=False)
        except Year.DoesNotExist:
            return JsonResponse('Year not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)

@csrf_exempt
def CarApi(req, id=0):
    if req.method == 'GET':
        car = Car.objects.all()
        cars_serializer = CarSerializer(car, many=True)

        return JsonResponse(cars_serializer.data, safe=False)    
    elif req.method == 'POST':
        car_data = JSONParser().parse(req)
        
        car_serializer = CarSerializer(data=car_data, partial=True)
        if car_serializer.is_valid():
            car = car_serializer.save()
            
            return JsonResponse('Added successfully!!', safe=False)
        
        return JsonResponse(car_serializer.errors, status=400, safe=False) 
    elif req.method == 'PUT':
        car_data = JSONParser().parse(req)
        car = Car.objects.get(id=id)
        
        car_serializer = CarSerializer(car, data=car_data, partial=True)
        if car_serializer.is_valid():
            car_serializer.save()

            return JsonResponse('Updated successfully!!', safe=False)
        
        return JsonResponse('Failed update!!', safe=False)   
    elif req.method == 'DELETE':
        try:
            car = Car.objects.get(id=id)
            car.delete()

            return JsonResponse('Deleted successfully!!', safe=False)
        except Car.DoesNotExist:
            return JsonResponse('Car not found.', status=404, safe=False)
    else:
        return JsonResponse('Invalid request.', status=400, safe=False)
    
@csrf_exempt
def SaveFile(req):
    car_images = {
        'front': req.FILES.get('front', None),
        'left': req.FILES.get('left', None),
        'right': req.FILES.get('right', None),
        'back': req.FILES.get('back', None),
        'inside': req.FILES.get('inside', None),
    }

    # Pegar o ID e o nome do carro na requisição
    user_id = "1"  
    car_name = "carro novo".replace(" ", "-")  
    car_folder = f'{user_id}/{car_name}'

    for image_name, image_file in car_images.items():
        if image_file is not None:
            file_extension = os.path.splitext(image_file.name)[1]
            new_file_name = f"{image_name}{file_extension}"

            destination_path = os.path.join(settings.MEDIA_ROOT, car_folder, new_file_name)

            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            with open(destination_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
    return JsonResponse({'success': 'Car images saved successfully'})