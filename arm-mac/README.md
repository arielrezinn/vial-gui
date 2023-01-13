# Local Development on an Arm-based Mac
After many hours, I'm able to successfully run `fbs run` and `fbs freeze` on my M1 Mac running Ventura 13.1. Here's how!

1. Open a terminal window and navigate to your vial-gui directory
1. Install Python 3.6.15 (Credit goes to [this Github issue](https://github.com/pyenv/pyenv/issues/1768#issuecomment-1105450096) and [this Stack Overflow post](https://stackoverflow.com/questions/68583709/pyinstaller-oserror-python-library-not-found))
   ```
   # Install Rosetta
   /usr/sbin/softwareupdate --install-rosetta --agree-to-license

   # Install x86_64 brew
   arch -x86_64 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

   # Set up x86_64 homebrew and pyenv and temporarily set aliases
   alias brew86="arch -x86_64 /usr/local/bin/brew"
   alias pyenv86="arch -x86_64 pyenv"

   # Install required packages and flags for building this particular python version through emulation
   brew86 install pyenv gcc libffi gettext
   export CPPFLAGS="-I$(brew86 --prefix libffi)/include -I$(brew86 --prefix openssl)/include -I$(brew86 --prefix readline)/lib"
   export CFLAGS="-I$(brew86 --prefix openssl)/include -I$(brew86 --prefix bzip2)/include -I$(brew86 --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include -Wno-implicit-function-declaration" 
   export LDFLAGS="-L$(brew86 --prefix openssl)/lib -L$(brew86 --prefix readline)/lib -L$(brew86 --prefix zlib)/lib -L$(brew86 --prefix bzip2)/lib -L$(brew86 --prefix gettext)/lib -L$(brew86 --prefix libffi)/lib"

   # Providing an incorrect openssl version forces a proper openssl version to be downloaded and linked during the build
   export PYTHON_BUILD_HOMEBREW_OPENSSL_FORMULA=openssl@1.0

   # Build CPython with Framework support on OS X, not doing this results in an error similar to: "OSError: Python library not found: .Python, Python, libpython3.6m.dylib, libpython3.6.dylib". However, exporting this [can cause issues building some distros](https://github.com/pyenv/pyenv/wiki#how-to-build-cpython-with-framework-support-on-os-x), so do it at your own risk.
   export PYTHON_CONFIGURE_OPTS="--enable-framework"

   # Install Python 3.6
   pyenv86 install --patch 3.6.15 <<(curl -sSL https://raw.githubusercontent.com/pyenv/pyenv/master/plugins/python-build/share/python-build/patches/3.6.15/Python-3.6.15/0008-bpo-45405-Prevent-internal-configure-error-when-runn.patch\?full_index\=1)

   # Note: the build will (hopefully) succeed and give the following warning: "WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?" This doesn't have any ill-effect for our purposes, and can be ignored.
   ```
1. Set your local python version with `pyenv local 3.6.15`
1. Create a virtual environment
   1. `arch -x86_64 python3 -m venv venv`
   1. `source venv/bin/activate`
1. Install the dependencies that aren't available directly from pip
   1. `pip install arm-mac/renamed-wheels/sip-4.19.8-cp36-cp36m-macosx_13_1_intel.whl`
   1. `pip install arm-mac/renamed-wheels/PyQt5_sip-4.19.18-cp36-cp36m-macosx_13_1_intel.whl`
   1. `pip install arm-mac/renamed-wheels/PyQt5-5.9.2-5.9.3-cp35.cp36.cp37-abi3-macosx_13_1_x86_64.whl`
1. Install the rest of the dependencies 
   1. `pip install -r requirements.txt`
1. Check if you can successfully run `fbs run`
   1. If you can, proceed to the next step
   1. If you can't, something went wrong. I wish you the best while troubleshooting :)
1. Apply a patch that lets Pyinstaller find dynamically linked libs. This is the step that enables `fbs freeze`. Credit for the patch goes to [this Github issue](https://github.com/pyinstaller/pyinstaller/issues/5107)
   1. Copy the contents of `/vial-gui/arm-mac/venv-lib-Pyinstaller-depend/bindepend.py` to `/vial-gui/venv/lib/python3.6/site-packages/PyInstaller/depend/bindepend.py`
1. Check if you can successfully run `fbs freeze`
   1. If you can, congratulations!
   1. If you can't, something went wrong. I wish you the best while troubleshooting :)
# Resources 
- https://stackoverflow.com/questions/71862398/install-python-3-6-on-mac-m1
- https://github.com/pyenv/pyenv/issues/1768
- https://pypi.org/project/PyQt5-sip/4.19.18/#files
- https://pypi.org/project/sip/4.19.8/#files
- https://pypi.org/project/PyQt5/5.9.2/#files
- https://github.com/mherrmann/fbs/issues/282
- https://github.com/pyinstaller/pyinstaller/issues/5107
