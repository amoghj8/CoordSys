from setuptools import setup

setup(
    # The name of our pip package
    name='Coordconv',
    # The Python packages in this project
    packages=[
        # This is the `Coordsys` folder that contains __init__.py and cli.py
        'Coordsys',
    ],
    version="1.0.0",
    entry_points={
        'console_scripts': [
            #This line to maps main()` method in cli.py
            # to a shell command `coordsys`
            'coordsys = Coordsys.cli:main',
        ],
    },
	
    description='Python command line client for conversion between coordinates',
    url='https://github.com/amoghj8/CoordSys',
    author='Amogh A Joshi',
    author_email='amoghj8@gmail.com',
    scripts=['Coordsys/cli.py'],
    license='MIT',
    keywords='coordinates cli physics numpy cartesian spherical cylindrical'
)
