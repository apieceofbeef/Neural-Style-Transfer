from google.colab import files
import os

os.makedirs('images/style-images', exist_ok=True)
uploaded = files.upload()

for fn in uploaded.keys():

    extension = os.path.splitext(fn)[1]
    style_image_name = "style_image" + extension
    os.rename(fn, f'images/style-images/{style_image_name}')
    print(f'Style image saved as: {style_image_name}')
