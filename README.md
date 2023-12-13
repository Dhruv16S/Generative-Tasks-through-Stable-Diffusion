The following repository is an implementation of the diffusers library by hugging face and more particularly the pre trained stable diffusion models. 

# Diffusers Library by Hugging Face

The [diffusers library](https://huggingface.co/docs/diffusers/index) by Hugging Face is a powerful tool for implementing diffusion models which are a class of generative models that leverage the concept of diffusion processes to generate high-quality samples. This repo contains the implementation of the [Text to Image](https://huggingface.co/docs/diffusers/using-diffusers/conditional_image_generation) and [Image to Image](https://huggingface.co/docs/diffusers/using-diffusers/img2img) tasks through stable diffusion models.

`Note:` For all the pretrained models, I have set the value of `safety_checker` to `None`. The documentation does not advice to this, however, I was getting an error `Potential NSFW content was detected in one or more images. A black image will be returned instead. Try again with a different prompt and/or seed.` and changed the variable as per this [issue](https://github.com/huggingface/diffusers/issues/2153)

### Installation

1. Clone this repository

```
git clone https://github.com/Dhruv16S/Generative-Tasks-through-Stable-Diffusion.git
```

2. Install required dependencies through

```
pip install -r requirements.txt
```

3. Create a file called `auth_token.py` and define a variable `token=<INSERT HUGGING FACE TOKEN HERE>`. Specify the user access token in `<>`. To create a user access token follow the instructions [here](https://huggingface.co/docs/hub/security-tokens). Ensure you have a hugging face account before generating your token.

4. Run the application

```
python app.py
```

### Debugging

If `"AssertionError: Torch not compiled with CUDA enabled` is encountered, follow the below steps:

1. Run the following command in the same directory

```
python check_config.py
```
check the torch version and if CUDA is enabled

2. Make sure you have a compatible NVIDIA GPU and have installed the corresponding CUDA toolkit. You can find the CUDA toolkit version compatible with your GPU on the [NVIDIA website](https://developer.nvidia.com/cuda-toolkit)

3. Run the following command

```
pip uninstall torch torchvision -y
```

4. Install PyTorch with CUDA support by following the instructions (here)[https://pytorch.org/get-started/locally/]. The following command worked for me:

```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

5. Re run the flask application
```
python app.py
```

