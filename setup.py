from setuptools import setup, find_packages

setup(
    name='davidtea',
    version='1.0.0',
    packages=find_packages(),
    author='Oke Akoro',
    author_email='oke_akoro@hotmail.com',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oakoro/davidtea',
    project_urls={
        "Source": "https://github.com/oakoro/davidtea"  # Added a comma here
    },
    install_requires=[
        # Add your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
