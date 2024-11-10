from setuptools import setup, find_packages

setup(
    name='package_example',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'PyJWT',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my_library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)