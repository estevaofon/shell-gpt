from setuptools import setup, find_packages

setup(
    name='shell-gpt',
    version='0.1.0',
    url='https://github.com/yourusername/shell-gpt',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple terminal chat with GPT-3.5-turbo',
    packages=find_packages(),    
    install_requires=['openai', 'pygments'],
    entry_points={
        'console_scripts': [
            'shell-gpt = shell_gpt:main',
        ],
    },
)

