"""
Flask-Webpack
-------------

Integration of flask with webpack through jinja
"""
from setuptools import setup

setup(
    name='Flask-Webpack',
    version='1.0',
    url='http://example.com/flask-webpack/',
    license='BSD',
    author='Sean Sullivan',
    author_email='ssullivan61198@gmail.com',
    description='Use webpack bundles in flask jinja templates',
    long_description=__doc__,
    py_modules=['flask_webpack'],
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
