# 602 virtualenv
 
## Setup .venv (Mac)
Setup your virutalenv venv with something like this... 

```sh
brew install python@3.10 ## to get python, if you do'nt already have it! 
brew install python-tk@3.10 tcl-tk 
brew link --overwrite python-tk@3.10
# create your venv with python3.10, like this.
/opt/homebrew/Cellar/python\@3.10/3.10.13_2/bin/python3.10 -m venv .venv
#activate and further build your virtual environment 
source ./.venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
```

## Test the Tk Gui
```shell
## cd project-directory
source ./.venv/bin/activate
python test_tkinter.py
```

## Set your PYTHONPATH
In your .venv/bin/activate, your python class path must be set to include the .venv directory, plus the ./src directory, like this, but with your computer paths. 

`export PYTHONPATH=/Users/afraser/Documents/src/dreamteam/.venv/lib/python3.10/site-packages:/Users/afraser/Documents/src/dreamteam/src`


## Test an nltk plot using iPython
```shell
source ./.venv/bin/activate
ipython
```

```python
import matplotlib.pyplot as plt
import nltk
from nltk.book import text4
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])
plt.show()
```
