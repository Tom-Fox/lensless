import getpass, os
import io
import warnings
import time
from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from get_l_image import get_latest_image

os.environ['STABILITY_HOST'] = 'grpc.stablility.ai:443'

# stability api key
os.environ['STABILITY_KEY'] = 'sk-RhLYaogozhfYu3xqcNAZPUvzFPsktdB0yEpI7jlxP77sEUsy'

# Set up our connection to the API.
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference.
    verbose=True, # Print debug messages.
    engine="stable-diffusion-xl-1024-v1-0", # Set the engine to use for generation.
    # Check out the following link for a list of available engines: https://platform.stability.ai/docs/features/api-parameters#engine
)

# set up image format
image_path = 'img'
img = get_latest_image(image_path)
img = img.resize((768, 512))
img # 統一したimageはimageで出力
timestamp = int(time.time())
save_path = f'save_image/image_{timestamp}.png'

# set up prompt
# year = 2023
# image_style = "pixel"
answers = stability_api.generate(
    prompt="Generate what this photo would have looked like 100 years ago without changing the original premise of this image.",
    # prompt="Create an image in a pixel art style that represents a scene frozen in time in the year 2023. The image should maintain the original content, including the exact positions of objects and the overall composition. The only change should be the transformation of the photo into a pixel art representation, reflecting the distinctive aesthetic of pixelated visuals. The scene is set in 2023, so any visible technology, fashion, or environmental elements should subtly indicate this year, but without altering the fundamental elements of the original photo",
    init_image = img,
    # init_image="/content/img", # Assign our previously generated img as our Initial Image for transformation.
    start_schedule=0.6, # Set the strength of our prompt in relation to our initial image.
    seed=123463447, # If attempting to transform an image that was previously generated with our API,
                    # initial images benefit from having their own distinct seed rather than using the seed of the original image generation.
    steps=50, # Amount of inference steps performed on image generation. Defaults to 30.
    cfg_scale=9.5, # Influences how strongly your generation is guided to match your prompt.
                   # Setting this value higher increases the strength in which it tries to match your prompt.
                   # Defaults to 7.0 if not specified.
    width=786, # Generation width, defaults to 512 if not included.786x512
    height=512, # Generation height, defaults to 512 if not included.
    # style_preset="cinematic",
    sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                 # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                 # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
)

# Set up our warning to print to the console if the adult content classifier is tripped.
# If adult content classifier is not tripped, display generated image.
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img2 = Image.open(io.BytesIO(artifact.binary)) # Set our resulting initial image generation as 'img2' to avoid overwriting our previous 'img' generation.
            #display(img2)
            # img2.show()
            img2.save(save_path)
            