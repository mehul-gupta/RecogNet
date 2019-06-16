'exec(%matplotlib inline)'
from flask import Flask, render_template, request
from scipy.misc import imsave, imread, imresize
import numpy as np
import keras.models
import re
import base64
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import cv2

import sys
import os
sys.path.append(os.path.abspath("./model"))
from load import *

app = Flask(__name__)
global model, graph
model, graph = init()
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict/', methods=['GET','POST'])
def predict():
    # get data from drawing canvas and save as image
    parseImage(request.get_data())

    # read parsed image back in 8-bit, black and white mode (L)
#    x = imread('output.png', mode='L')
#    x = np.invert(x)
#    x = imresize(x,(28,28))

    new_img=convert_image('tmp/output.png')
    plt.subplot(1, 1, 1)
    plt.axis('off')
    plt.imshow(new_img, cmap=plt.cm.gray_r, interpolation='kaiser')
    npimg=np.array(new_img)
    npimg[npimg>0.1]=1
    npimg[npimg<=0.1]=0
    npimg=npimg.reshape(-1,28,28,1)
    with graph.as_default():
        predicted = model.predict(npimg)
        predicted = np.argmax(predicted,axis = 1)
        print("Predicted: ",predicted)    
        response = np.array_str(predicted)
        return response
    
    # reshape image data for use in neural network
#    x = x.reshape(1,28,28,1)
#    with graph.as_default():
#        out = model.predict(x)
#        print(out)
#        print(np.argmax(out, axis=1))
#        response = np.array_str(np.argmax(out, axis=1))
#        return response 

def imageprepare(argv):
    """
    This function returns the pixel values.
    The input is a png file location.
    """
    im = Image.open(argv).convert("RGB")
    im = im.convert("L")

    width = float(im.size[0])
    height = float(im.size[1])
    new_image = Image.new('L', (28, 28), 255)  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
        if nheight == 0:  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        new_image.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Height becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if nwidth == 0:  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
        new_image.paste(img, (wleft, 4))  # paste resized image on white canvas

    # newImage.save("sample.png

    tv = list(new_image.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    return tva


def remove_transparent(path):
    im = Image.open(path).convert("RGBA")
    width = float(im.size[0])
    height = float(im.size[1])
    canvas = Image.new('RGBA', im.size, (255, 255, 255, 255))  # Empty canvas colour (r,g,b,a)
    canvas.paste(im, mask=im)  # Paste the image onto the canvas, using it's alpha channel as mask
    canvas.thumbnail([width, height], Image.ANTIALIAS)
    canvas.save(path, format="PNG")

def convert_image(image_path):
    remove_transparent(image_path)
    x = [imageprepare(image_path)]  # file path here
    # Now we convert 784 sized 1d array to 24x24 sized 2d array so that we can visualize it
    new_arr = [[0 for d in range(28)] for y in range(28)]
    k = 0
    for i in range(28):
        for j in range(28):
            new_arr[i][j] = x[0][k]
            k = k + 1

    return new_arr

def parseImage(imgData):
    # parse canvas bytes and save as output.png
    imgstr = re.search(b'base64,(.*)', imgData).group(1)
    with open('tmp/output.png','wb') as output:
        output.write(base64.decodebytes(imgstr))

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
