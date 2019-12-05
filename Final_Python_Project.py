import requests

for number in range(1):
    data = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
    base_layer_name = data['base_layer']['name']
    base_layer_recipe = data['base_layer']['recipe']
    seasoning_name = data['seasoning']['name']
    seasoning_recipe = data['seasoning']['recipe']
    mixin_name = data['mixin']['name']
    mixin_recipe = data['mixin']['recipe']
    condiment_name = data['condiment']['name']
    condiment_recipe = data['condiment']['name']
    shell_name = data['shell']['name']
    shell_recipe = data['shell']['name']
    print(f'{base_layer_recipe}\n{seasoning_recipe}\n{mixin_recipe}\n')
    print(f'{condiment_recipe}\n{shell_recipe}')
