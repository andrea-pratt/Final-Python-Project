import requests
import docx
from PIL import Image, ImageFont, ImageDraw
from docx.shared import Inches

try:
    image = Image.open('taco_image.jpg')
    image.thumbnail((800, 800))
    font = ImageFont.truetype('DejaVuSans.ttf', 40)
    img_draw = ImageDraw.Draw(image)
    img_draw.text([80, 100], 'Random Taco Cookbook', fill='white', font=font)
    image.save('taco_thumbnail.jpg')

    document = docx.Document()
    document.add_paragraph('Random Taco Cookbook', 'Title')
    document.add_picture('taco_thumbnail.jpg', width=Inches(5.5))
    document.add_paragraph('Credits', 'Heading 1')
    document.add_paragraph('(who took the picture?)\n(what website did the pic come from)\n(who wrote the code?)')
    document.add_page_break()
    document.save('random_taco_recipes.docx')
    try:
        for number in range(3):
            data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
            base_layer_recipe = data['base_layer']['recipe']
            seasoning_recipe = data['seasoning']['recipe']
            mixin_recipe = data['mixin']['recipe']
            condiment_recipe = data['condiment']['recipe']
            shell_recipe = data['shell']['recipe']
            base_layer_name = data['base_layer']['name']
            seasoning_name = data['seasoning']['name']
            mixin_name = data['mixin']['name']
            condiment_name = data['condiment']['name']
            shell_name = data['shell']['name']
            document.add_paragraph(f'{base_layer_name} with {seasoning_name}, {mixin_name} and {condiment_name} in {shell_name}', 'Heading 1')
            document.add_paragraph(f'{base_layer_name}', 'Heading 1')
            document.add_paragraph(f'{base_layer_recipe}')
            document.add_paragraph(f'{seasoning_name}', 'Heading 1')
            document.add_paragraph(f'{seasoning_recipe}')
            document.add_paragraph(f'{mixin_name}', 'Heading 1')
            document.add_paragraph(f'{mixin_recipe}')
            document.add_paragraph(f'{condiment_name}', 'Heading 1')
            document.add_paragraph(f'{condiment_recipe}')
            document.add_paragraph(f'{shell_name}', 'Heading 1')
            document.add_paragraph(f'{shell_recipe}')
            document.add_page_break()
    except requests.exceptions.ConnectionError:
        print('There seems to be a problem with your internet connection. Cannot get recipe data.')

    document.save('random_taco_recipes.docx')
except PermissionError:
    print('Please close the existing word document and try again.')
