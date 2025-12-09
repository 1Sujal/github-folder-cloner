from setuptools import setup, find_packages

setup(
    name="github-folder-cloner",
    version="0.1.0",
    description="Clone a specific folder from a GitHub repo without cloning the entire repo",
    author="Sujal Bhattarai",
    author_email="null",
    url="https://github.com/1Sujal/github-folder-cloner",
    packages=find_packages(),
    py_modules=["main"],
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "github-folder-cloner=main:main",
        ],
    },
    python_requires='>=3.8',
)
