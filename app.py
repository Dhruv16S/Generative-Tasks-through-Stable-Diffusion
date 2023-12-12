from flask import Flask, request, render_template
from PIL import Image, ImageTk
from auth_token import token
from torch import autocast
from diffusers import StableDiffusionPipeline

app = Flask(__name__)

model_id = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16, use_auth_token=token)
pipe.to(device)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['prompt']

    with autocast(device):
        image = pipe(text, guidance_scale=8.5)["sample"][0]

    image.save('static/generatedimage.png')

    return 'static/generatedimage.png'

if __name__ == '__main__':
    app.run(debug=True)
