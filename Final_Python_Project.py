import requests

# TODO add try/except block and add code to create word document out of this data
for number in range(3):
    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    base_layer_recipe = data['base_layer']['recipe']
    seasoning_recipe = data['seasoning']['recipe']
    mixin_recipe = data['mixin']['recipe']
    condiment_recipe = data['condiment']['recipe']
    shell_recipe = data['shell']['recipe']
    print(f'{base_layer_recipe}\n{seasoning_recipe}\n{mixin_recipe}\n')
    print(f'{condiment_recipe}\n{shell_recipe}')
