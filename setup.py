from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README

setup(
    name="quidax-python",
    version="1.2",
    description='A python library to consume Quidax API',
    keywords='quidax python library',
    license="MIT",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
    author_email="oye@appstate.co",
)