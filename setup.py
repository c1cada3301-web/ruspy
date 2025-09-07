from setuptools import setup, find_packages

setup(
    name='ruspy',
    version='0.1.0',
    description='Транспилятор "русский Python" — пишите код на русском, запускайте на Python!',
    author='Саша Трунов',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ruspy = ruspy.cli:main',
        ],
    },
    python_requires='>=3.7',
)