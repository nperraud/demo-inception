Demo Inception
==============

This small python script simply demonstrates the third version of the inception
network from Google. It captures an image using the webcam of the computer and
predicts the label using the neural network. For the fun, it will also use the
gtts module to say the result.

It is a small demonstration script that needs further cleaning.


Installation
------------

1. Clone the repository
2. Consider creating a pyhton3 virtual environment
3. Install the following python3 packages
   * tensorflow
   * numpy
   * keras
   * matplotlib
   * gtts
   * pygame
   * openCV (cannot be install with pip or conda, need to be installed
     externally, using homebrew for instance)

On mac, if you install opencv using homebrew, you may need to link manually
openCV

Execution
---------

Simply run 
<pre>
python3 main.py
</pre>

The first time, the script will automatically download the inception network,
which will take some time.

Enjoy!
