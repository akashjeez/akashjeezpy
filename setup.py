from setuptools import setup

with open("README.md", 'r') as fh:
	long_description = fh.read()

setup(
    name = 'akashjeezpy',
    version = '0.0.2',
    author = 'akashjeez',
    author_email = 'akashit63@gmail.com',
    url = 'https://github.com/akashjeez/akashjeezpy',
    description = 'A Python Package to Deliver a Lot of Useful Services!',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Programming Language :: Python :: 3", 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.4',
    install_requires = ['requests'],
    py_modules = ['akashjeezpy'],
    package_dir = {'': 'src'}
)
