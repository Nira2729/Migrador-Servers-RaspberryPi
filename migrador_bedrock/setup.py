from setuptools import setup, find_packages

setup(
    name='migrador-bedrock',
    version='0.1.0',
    author='Hendricks',
    description='Herramienta modular para migrar mundos Bedrock a servidores dedicados en Raspberry Pi',
    packages=find_packages(),
    install_requires=[
        'click',
        'psutil'
    ],
    entry_points={
        'console_scripts': [
            'migrador-bedrock = migrador.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)