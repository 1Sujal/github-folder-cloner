THE GITHUB WAY IS TIME CONSUMING ICL
# GitHub Folder Cloner

A lightweight Python tool that downloads **only a specific folder** from any public GitHub repository — without cloning the entire repo, and without requiring Git or SVN.

---

## 🚀 Features

- Extract a single folder from any GitHub repository
- Works on all operating systems (Windows, macOS, Linux)
- No SVN, no Git required
- Installable via `pip`

---

## 📦 Installation

### Install from GitHub:

```bash
pip install git+https://github.com/1Sujal/github-folder-cloner.git
```
 Or clone and install locally:
```bash
git clone https://github.com/1Sujal/github-folder-cloner.git
cd github-folder-cloner
pip install .
```
🏃 Usage
Basic CLI
```bash
github-folder-cloner <github-folder-url> <output-folder>
```

Example:
```bash
github-folder-cloner https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.hello-world tutorial-hello-world
```


This will download only the tutorial.hello-world folder into tutorial-hello-world/.

🔧 Requirements

Python 3.8+

```bash
requests
``` (installed automatically via pip)
