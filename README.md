# Demo Inception


This small python script simply demonstrates the third version of the inception
network from Google. It captures an image using the webcam of the computer and
predicts the label using the neural network. For the fun, it will also use the
gtts module to say the result.

It is a small demonstration script that needs further cleaning.

### Requirements


Make sure you have openCV (it cannot be installed with pip or conda, need to 
be installed externally, using homebrew for instance)

On mac, if you install opencv using homebrew and virtual environment, you may 
need to manually link openCV


### Installation

1. Clone the repository
   ```
   git clone https://github.com/nperraud/demo-inception.git
   ```

2. Consider creating a pyhton3 virtual environment. Make sure openCV is
   accessible from it. To test you can simply use
   ```
   python
   import cv2
   print(cv2.__version__)
   ```
   
3. Install the following python3 packages
   ```
   pip install -r requirements.txt
   ```

### Execution

Simply run 
```
python main.py
```

For the script to work properly, it needs to capture your keyboard input. If
your inputs are not captured, click on the current window/figure.

The first time, the script will automatically download the inception network,
which will take some time.

Enjoy!
