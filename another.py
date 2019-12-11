import requests
import docx
import shutil
from PIL import Image
import os
# from docx.shared import Inches


response = requests.get('https://api.unsplash.com/photos/?client_id=3a31301fc8edce2497d0e0dd001ec1bfbed7a207b9207dd2ccc5c87baade2b12').json()
image_url = response[0]['links']['download']
print(image_url)

image_url = "https://www.dev2qa.com/demo/images/green_button.jpg"

resp = requests.get(image_url, stream=True)
local_file = open('local_image.jpg', 'wb')
resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
image = Image.open('local_image.jpg')
image.save()

document = docx.Document()
document.add_picture('local_image.jpg')
document.save('thisisadocument.docx')

