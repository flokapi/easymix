from setuptools import setup, find_packages

setup(
    include_package_data=True,
    name='easymix',
    version='0.7',
    description='Simple live and track python audio mixer',
    url='https://github.com/flokapi/easymix',
    author='flokapi',
    author_email='flokapi@pm.me',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    #package_data={"pymikro": ['*.json']},
    install_requires=['pydub', 'pyaudio'],
    license='LGPLv2',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)