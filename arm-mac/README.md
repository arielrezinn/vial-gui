# Local Development on an Arm-based Mac
After many hours, I'm able to successfully run `fbs run` on my M1 Mac running Ventura 13.1. Here's how!

1. Open a terminal window and navigate to your vial-gui directory
1. Follow the instructions written in [this Github issue](https://github.com/pyenv/pyenv/issues/1768#issuecomment-1105450096) to install python 3.6.15
1. Set your local python version with `pyenv local 3.6.15`
1. Create a virtual environment
   1. `python3 -m venv venv`
   1. `source venv/bin/activate`
1. Install the dependencies that aren't available directly from pip
   1. `pip install arm-mac/renamed-wheels/sip-4.19.8-cp36-cp36m-macosx_13_1_intel.whl`
   1. `pip install arm-mac/renamed-wheels/PyQt5_sip-4.19.18-cp36-cp36m-macosx_13_1_intel.whl`
   1. `pip install arm-mac/renamed-wheels/PyQt5-5.9.2-5.9.3-cp35.cp36.cp37-abi3-macosx_13_1_x86_64.whl`
1. Install the rest of the dependencies 
   1. `pip install -r requirements.txt`

# Resources 
- https://stackoverflow.com/questions/71862398/install-python-3-6-on-mac-m1
- https://github.com/pyenv/pyenv/issues/1768
- https://pypi.org/project/PyQt5-sip/4.19.18/#files
- https://pypi.org/project/sip/4.19.8/#files
- https://pypi.org/project/PyQt5/5.9.2/#files

# Known Issues
The above instructions let you run `fbs run` on your machine, but do **not** let you run `fbs freeze`. In other words, you aren't able to package any of your local changes into a standalone application.