import requests
import docx
from docx.shared import Pt
from PIL import Image, ImageFont, ImageDraw
# import PIL
from docx.shared import Inches

image = Image.open('taco_image.jpg')
resized_image = image.thumbnail((800, 800))
font = ImageFont.truetype('DejaVuSans.ttf', 40)
img_draw = ImageDraw.Draw(image)
img_draw.text([80, 100], 'Random Taco Cookbook', fill='white', font=font)
image.save('taco_thumbnail.jpg')
# TODO add try/except block
document = docx.Document()
document.add_paragraph('Random Taco Cookbook', 'Title')
document.add_picture('taco_thumbnail.jpg', width=Inches(5.5))
document.add_paragraph('Credits', 'Heading1')
document.add_paragraph('(who took the picture?)\n(what website did the pic come from)\n(who wrote the code?)')
document.add_page_break()
document.save('random_taco_recipes.docx')
for number in range(3):
    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    base_layer_recipe = data['base_layer']['recipe']
    seasoning_recipe = data['seasoning']['recipe']
    mixin_recipe = data['mixin']['recipe']
    condiment_recipe = data['condiment']['recipe']
    shell_recipe = data['shell']['recipe']
    document.add_paragraph(f'Recipe Number {number + 1}')
    document.add_paragraph(f'{base_layer_recipe}\n\n\n{seasoning_recipe}\n\n\n{mixin_recipe}\n\n\n{condiment_recipe}\n\n\n{shell_recipe}')
    document.save('random_taco_recipes.docx')
