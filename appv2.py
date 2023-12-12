import torch
from diffusers import StableDiffusionPipeline
from auth_token import token

# stabilityai/stable-diffusion-xl-base-1.0
# CompVis/stable-diffusion-v1-4
# runwayml/stable-diffusion-v1-5
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", safety_checker=None, auth_token=token)
pipe = pipe.to("cuda")
# pipe.enable_sequential_cpu_offload()
prompt = "a formula one race on a star wars planet, 8k, high res"
image = pipe(prompt, guidance_scale=7.0).images[0]
image.save("gen.png")