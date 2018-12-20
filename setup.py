from setuptools import setup, find_packages

setup(
    name='example',
    version='0.0.0',
    description='Example',
    url='Example',
    author='Me',
    author_email='me@me.me',
    long_description='example',
    license='MIT',
    keywords='',
    packages=find_packages(),
    install_requires=['sphinx', 'sphinx-argparse', 'sphinx-markdown-builder'],
    )
