import requests
import docx

# TODO add try/except block and add code to create word document out of this data
document = docx.Document()

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
