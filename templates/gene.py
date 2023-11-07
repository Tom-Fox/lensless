import openai
import models
import rawPic

def getGenePic(input):
    openai.api_key = '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'
    response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)
    print('got img url')
    return image_url