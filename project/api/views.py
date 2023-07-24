from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

from rest_framework.parsers import JSONParser


from .utils import save_car_images
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
        car_data = {
            'Name': req.POST.get('Name', ''),
            'Brand': req.POST.get('Brand', ''),
            'Model': req.POST.get('Model', ''),
            'Year': req.POST.get('Year', ''),
            'Location': req.POST.get('Location', ''),
            'Transmission': req.POST.get('Transmission', ''),
            'Price': req.POST.get('Price', ''),
            'DiscountPrice': req.POST.get('DiscountPrice', ''),
            'Mileage': req.POST.get('Mileage', ''),
            'Color': req.POST.get('Color', ''),
            'Seat': req.POST.get('Seat', ''),
            'Fuel': req.POST.get('Fuel', ''),
            'User': req.POST.get('User', ''),
        }

        car_images = {
            'front': req.FILES.get('front', None),
            'left': req.FILES.get('left', None),
            'right': req.FILES.get('right', None),
            'back': req.FILES.get('back', None),
            'inside': req.FILES.get('inside', None),
        }

        car_folder = save_car_images(car_data, car_images) 
        car_data['ImageFile'] = car_folder
        
        car_data = {key: value for key, value in car_data.items() if value}
        
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
    file=req.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)