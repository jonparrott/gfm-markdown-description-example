from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    author='Jon Parrott',
    author_email='me@thea.codes',
    description='A PyPI package with a Github-Flavored Markdown README',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    name='gfm-markdown-description-example',
    setup_requires=['setuptools>=38.6.0'],
    url='http://github.com/jonparrott/gfm-markdown-description-example',
    version='0.0.2',
)
