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
        'transformers==4.25.1',
        'torch==2.1.0',
        'datasets==2.15.0',
        'safetensors==0.4.0'
    ],
)