from django.conf import settings
import os

# Função ultilizada em views para auxiliar na criação da view CarApi em criar pasta com id do usuario e salvar imagens dos carros dentro
def save_car_images(car, images):
    user_folder = os.path.join(settings.MEDIA_ROOT, str(car['User']))
    
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    car_name = car['Name'].replace(" ", "-") 
    car_folder = os.path.join(user_folder, car_name)

    if not os.path.exists(car_folder):
        os.makedirs(car_folder)

    image_paths = {
        'front': os.path.join(car_folder, 'front.jpg'),
        'left': os.path.join(car_folder, 'left.jpg'),
        'right': os.path.join(car_folder, 'right.jpg'),
        'back': os.path.join(car_folder, 'back.jpg'),
        'inside': os.path.join(car_folder, 'inside.jpg'),
    }

    for key, image in images.items():
        destination_path = image_paths[key]        
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        with open(destination_path, 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

    return car_folder

