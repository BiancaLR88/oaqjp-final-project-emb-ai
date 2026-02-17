from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='A package to detect emotions in text using Watson NLP',
    author='Amazing Miss B',
    packages=find_packages(),
    install_requires=['requests']
)