# For communication with the API
import requests
# For resizing an image and converting to base64
from io import BytesIO
from PIL import Image
import base64

# Returns a PIL format image
def resize(image):
    image = base64_to_pil(image)
    resized = resize_image(image)
    im_64 = pil_to_64(image)
    return im_64

def JPEG_to_PIL(image):
    # if type is JPEG
    im = Image.open(image)
    rgb_im = im.convert('RGB')
    return rgb_im

# Magic function that actually does the thing
def resize_image(image):
    # calculate new dimensions
    x, y = image.size
    small = min(x, y)
    factor = small / 600 if small > 600 else 1.0
    resize_dimensions = int(x / factor), int(y / factor)

    # resize (using LANCZOS resampling/interpolation)
    image = image.resize(resize_dimensions, resample=Image.LANCZOS)
    return image


# def image_to_64(image):

#     with open(image, "rb") as img_file:
#         b64_string = base64.b64encode(img_file.read())
#     return b64_string

def pil_to_64(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str

def base64_to_pil(image):
    # base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    # binary_data = base64.b64decode(base64_data)
    # img_data = StringIO(binary_data)
    # img = Image.open(img_data)
    image = base64.b64decode(image)
    image = BytesIO(image)
    image = Image.open(image)
    return image

def image_score(im_64):
    response = req_64_condition(im_64)
    return response.json().get('response', {}).get('solutions', {}).get('re_condition', {}).get('score', {})

def req_64_condition(im_64):
    url = 'https://api-eu.restb.ai'
    endpoint = '/vision/v2/predict'
    params = {
        'client_key': '668e94100dc9e3598afe9294abac3379e73e3c306c8d9e1b29dbce0ad505a90a',
        'model_id': 're_condition',
        'image_base64': im_64
    }
    
    # Key communication with the API
    query_params = dict(client_key=params['client_key'])  # client_key should always be passed as a query parameter
    ans = requests.post(url=url+endpoint, params=query_params, data=params, allow_redirects=False, timeout=60)
    return ans

# Should take a JPEG or PNG file and return its score
def luxury(image):
    image = resize(image)
    score = image_score(image)
    return score


def price(image):
    return 12*luxury(image)
