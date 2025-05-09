# Welcome!

### Python setup

Recommended to install "Anaconda"

- Open-source distribution of Python and R programming languages for scientific computing
- Simplifies package management and deployment
- Easy management of environemts

Installing conda

1. Get the distribution from https://www.anaconda.com/download#downloads
2. Install it, remember the path, on Windows, e.g. `C:\opt\anaconda3`

Creating an environment (in Windows)

1. Open a command prompt
2. `cd C:\opt\anaconda3`
3. `condabin\conda create -n ml3 python=3.11`
4. `condabin\conda activate ml3`

5. `python --version`

### Opening the course notebooks

1. From start menu, open a new shell via "Anaconda" > "Anaconda Prompt"
2. `cd` into the base directory for this course, e.g. `C:\Users\Michael\Desktop\hslu\cas\ml3\01-py-refresher`
3. `conda activate ml3`
4. `pip install -r requirements.txt`
5. Type `jupyter notebook` and wait for browser to open http://localhost:8888

Alternatively use your editor of choice (recommended). Free options:

- [Visual Studio Code](https://code.visualstudio.com/download)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Spyder](https://www.spyder-ide.org/)
