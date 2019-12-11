# Importing necessary modules for program
import requests  # Importing requests for API calls
import docx  # Allows for creation of Word documents
from PIL import Image, ImageFont, ImageDraw  # Importing Pillow image manipulation library
from docx.shared import Inches # Importing the Inches module to use when sizing the image in the word doc
"""
In the following block I'll be resizing, and adding a title to the taco image. I will then add the title, image and 
credits to the first page of the document
"""
# Try to begin creating a word document. If the document is currently open. An error message will print
try:
    image = Image.open('taco_image.jpg')  # Opening the original taco image
    image.thumbnail((800, 800))  # Resizing the image to a thumbnail
    font = ImageFont.truetype('DejaVuSans.ttf', 40)  # Getting the font for the image text and choosing it's size
    img_draw = ImageDraw.Draw(image)  # Creating new object to draw on image
    # Defining the look and position of text on the image
    img_draw.text([80, 100], 'Random Taco Cookbook', fill='white', font=font)
    image.save('taco_thumbnail.jpg')  # Saving the image with a new file name

# This portion of code is focused on creating the first page of the Word document

    document = docx.Document()  # Creating a Word document
    document.add_paragraph('Random Taco Cookbook', 'Title')  # Adding a title to first page with the 'Title' style
    document.add_picture('taco_thumbnail.jpg', width=Inches(5.5))  # Adding the taco image with a width of 5.5 inches
    document.add_paragraph('Credits', 'Heading 1')  # Adding a paragraph with the word 'credits'
    # This paragraph will give credit to the API and the person who took the photo
    document.add_paragraph('(who took the picture?)\n(what website did the pic come from)\n(who wrote the code?)')
    document.add_page_break()  # Adding a page break after the credits
    document.save('Random_Taco_Cookbook.docx')  # Saving the document before trying to call the API
# Try to call the API and add the data to word document. If it fails there will be an error message
    try:
        # This loop will be responsible for creating 3 separate and random taco recipes
        for number in range(3):
            # Calling the taco recipe API (once for each recipe)
            data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
            """For each of these recipes, I'm retrieving the 'recipe' key and the 'name' key
            from the API call and saving each one in a variable named accordingly"""
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
            # Here I'm adding a header for each of the taco recipes that lists all 5 ingredients
            document.add_paragraph(f'{base_layer_name} with {seasoning_name}, {mixin_name} and {condiment_name} '
                                   f'in {shell_name}', 'Heading 1')
            # Adding taco base layer name with the heading 1 style
            document.add_paragraph(f'{base_layer_name}', 'Heading 4')
            # Adding a paragraph that is the base layer recipe
            document.add_paragraph(f'{base_layer_recipe}')
            # Adding a heading paragraph for the seasoning recipe name
            document.add_paragraph(f'{seasoning_name}', 'Heading 4')
            # Adding a paragraph for the seasoning recipe
            document.add_paragraph(f'{seasoning_recipe}')
            # Adding a heading paragraph with the mixin recipe name
            document.add_paragraph(f'{mixin_name}', 'Heading 4')
            # Adding a paragraph with the mixin recipe
            document.add_paragraph(f'{mixin_recipe}')
            # Adding a header paragraph for the condiment name
            document.add_paragraph(f'{condiment_name}', 'Heading 4')
            # Adding a paragraph for the condiment recipe
            document.add_paragraph(f'{condiment_recipe}')
            # Adding a header paragraph for the shell name
            document.add_paragraph(f'{shell_name}', 'Heading 4')
            # Adding a paragraph for the shell recipe
            document.add_paragraph(f'{shell_recipe}')
            # Adding a page break between each of the 3 recipes
            if not number == 2:
                document.add_page_break()
        document.save('Random_Taco_Cookbook.docx')
    # If the internet connection fails, this error message will print
    except requests.exceptions.ConnectionError:
        print('There seems to be a problem with your internet connection. Cannot get recipe data.')

# If the word document is already opening when running this code, this error message will print
except PermissionError:
    print('Please close the existing word document and try again.')
