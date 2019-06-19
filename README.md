# Recognizes Handwritten digits:sunglasses: 
A software which predicts any handwritten English numeral drawn on the HTML canvas.

    Open-sourced on: 10-04-2019
Feel free to fork the repo and make any pull requests. 

A working demo of the project is hosted on https://recog-digits-api.herokuapp.com/

_______________________________________________________________________________________________________________________________________

## About the project:

The classifier is a 5 layer Sequential Convolutional Neural Network model trained on the MNIST dataset. I choosed to build it with keras API (Tensorflow backend) which is very intuitive. The model achieved an accuracy of 99.7% in the [Kaggle digit recognizer](https://www.kaggle.com/c/digit-recognizer) when trained on a single CPU (i5 2500k) with Nvidia GeForce 940MX capability.
_______________________________________________________________________________________________________________________________________

## How to deploy the model :question:
* Activate the virtual environment - <br/><br/>
Linux:  ```Source <virtualenv-name>\bin\activate```<br/>
Windows: ```<virtualenv-name>\Scripts\activate```

* Clone the repository - 
```bash
cd 
git clone https://github.com/mehul-gupta/RecogMyDigits
cd RecogMyDigits
```
* Install the required libraries by `pip install -r requirements.txt`

**Now, we are ready to launch and deploy our flask application.**

Run `python3 app.py` to launch the app. Now, open your browser and go to `localhost:5000`. TaDaaa!! Our app is running...
Draw any digit on the canvas and click on 'Predict'.

_______________________________________________________________________________________________________________________________________

## Re-training the classifier
Open the `Digit recognition.ipynb` notebook and follow the instructions to create your own classifier. When done, run the save_model() cell. The model will get saved to `digits_deeplearn.h5` file 

A demo of the project is shown below :smiley:<br/><br/>

 ![](https://github.com/mehul-gupta/RecogMyDigits/blob/master/DemoProj.gif) <br /><br />

For information on how the model works, please refer to:
* https://machinelearningmastery.com/handwritten-digit-recognition-using-convolutional-neural-networks-python-keras/
and 
* https://towardsdatascience.com/a-simple-2d-cnn-for-mnist-digit-recognition-a998dbc1e79a
