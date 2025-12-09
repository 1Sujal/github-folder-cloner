# GitHub Folder Cloner

A simple tool that clones **only a specific folder** from a GitHub repository — without cloning the whole repo, without SVN, without Git.

## ⭐ Features
- Pure Python (no external tools)
- Works on Windows, macOS, Linux
- Extracts only the selected folder
- Supports any branch

## 🚀 Usage

### Install dependencies
 ```pip install -r requirements.txt```

### Run
```python main.py <github-folder-url> <output-folder>```

### Example
```python main.py https://github.com/GoogleChrome/chrome-extensions-samples/tree/main/functional-samples/tutorial.hello-world tutorial```

The folder will be extracted to `tutorial/`.

