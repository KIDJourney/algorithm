from PIL import Image
import os

def image_hash(image):
    image = image.convert('L')

    image_size_x  , image_size_y = image.size
    
    lights = list(image.getdata())
    avg_light = sum(lights) / len(lights)

    pixels = image.load()

    for x in range(image_size_x) :
        for y in range(image_size_y) :
            if pixels[x,y] >  avg_light :
                pixels[x,y] = 255
            else :
                pixels[x,y] = 0

    image = image.resize((8,8))

    lights = list(image.getdata())

    hash_string = ''.join(['0' if i == 255 else '1' for i in lights])

    return hash_string

if __name__ == "__main__" :
    examples = os.listdir('ok2')
    goals = os.listdir('2')

    example_path = "./ok2/"
    goal_path = "./2/"

    goals_hash = [image_hash(Image.open(goal_path + file_name)) for file_name in goals]
    examples_hash = [image_hash(Image.open(example_path + file_name)) for file_name in examples]

    ans = 0
    
        