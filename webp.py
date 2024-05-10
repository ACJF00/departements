import os
from PIL import Image

directory_path = 'public/images'

for filename in os.listdir(directory_path):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".avif"):
        img = Image.open(os.path.join(directory_path, filename))
        img.save(os.path.join(directory_path, os.path.splitext(filename)[0] + '.webp'), 'webp')