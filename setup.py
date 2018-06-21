from setuptools import setup, find_packages


setup(
    name='gremlinc',
    version='0.2',
    description='Handle gremlin characters (zero width / invisible).',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='zero width characters gremlins',
    url='https://github.com/marinko-peso/gremlinc',
    author='Marinko Peso',
    author_email='marinko.peso@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
