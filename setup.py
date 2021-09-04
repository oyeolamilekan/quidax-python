from setuptools import setup, find_packages

setup(
    name="quidax-python",
    version="1.0",
    description='A python library to consume Quidax API',
    keywords='quidax python library',
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
    packages=find_packages()
)