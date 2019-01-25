"""
flask-webpack-js
-------------

Integration of flask with webpack through jinja
"""

from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='flask-webpack-js',
    version='0.1.0',
    url='https://github.com/sullivan-sean/flask-webpack',
    license='BSD',
    author='Sean Sullivan',
    author_email='ssullivan61198@gmail.com',
    description='Use webpack bundles in flask jinja templates',
    long_description=long_description,
    py_modules=['flask_webpack_js'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
