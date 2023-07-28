from setuptools import setup, find_packages

setup(
    name='My_Package',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cliente_SUBE = My_Package.My_module:main',
        ],
    },
    install_requires=[],
    author='Alexis Ibarra',
    author_email='alexis.ibarra@accenture.com',
    description='Paquete que modela un Cliente para una página de operacion de SUBE',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
