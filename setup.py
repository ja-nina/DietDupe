from setuptools import setup, find_packages

setup(
    name='Diet-Dupe',
    version='0.1',
    packages=find_packages(),
    description='Supsitution recommender for dietary restrictions',
    author='PAN',
    author_email='ninazukowska1@gmail.com',
    url='https://github.com/ja-nina/DietDupe',
    install_requires=[
        'numpy==1.25.2',
        'pandas==1.5.2',
        'transformers==4.20.1',
        'torch==2.0.0'
    ],
)