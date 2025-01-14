from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()
setup(
    name = 'testobject',
    packages = ['testobject'],
    version = '0.3.0',
    description = 'Python API wrapper for TestObject',
    author = 'Enrique Gonzalez',
    author_email = 'egonzalezh94@gmail.com',
    license='MIT',
     python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    url = 'https://github.com/enriquegh/testobject-python-api',
    install_requires=['requests', 'pyyaml'],
    long_description=long_description,
    keywords = ['wrapper-api', 'testobject'],
    classifiers = [],
)
