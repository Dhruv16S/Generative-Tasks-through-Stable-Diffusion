from flask import Flask, render_template, request
from diffusers import StableDiffusionPipeline
from auth_token import token

app = Flask(__name__)

# Kept safety_checker as None to avoid error of "NSFW content"
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", safety_checker=None, auth_token=token).to("cuda")

@app.route('/')
def home():
    return render_template('index.html', image_path="None")

@app.route('/generate', methods=['POST'])
def generate():
    task = request.form['task']
    prompt = request.form['prompt']

    if task == 'text2image':
        image = pipe(prompt, guidance_scale=8.0, height=560, width=480).images[0]
    elif task == 'image2image':
        pass
    else:
        return "Invalid task selected"
    
    image_path = "./static/gen.png"
    image.save(image_path)
    return render_template('index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
