import io
import requests
from PIL import Image

def download(id):
    url = f'http://xkcd.com/{id}/info.0.json'
    data = requests.get(url).json()
    img = data['img']
    response = requests.get(img)
    image =  Image.open(io.BytesIO(response.content))
    return image

def comics(s,e):
    for id in range(s, e+1):
        try:
            image = download(id)
            filename = f'{id}.png'
            image.save(filename, 'PNG')
            print(f'Saved {filename}')
        except Exception as e:
            print(f'Error downloading! {id}: {e}')

comics(1,10)

