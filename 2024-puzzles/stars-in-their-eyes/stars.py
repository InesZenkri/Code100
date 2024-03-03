import json

with open('stars.json', 'r') as file:
    stardata = json.load(file)
def calculate_pixels(star):
    return int(star['width'] * star['height'] - (3.14159 * star['width']/2 * star['height']/2))

pixels = sum(map(calculate_pixels, stardata))

with open('res.json', 'w') as file:
    json.dump(pixels, file, indent=4)