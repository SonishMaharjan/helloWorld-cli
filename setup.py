from setuptools import setup

setup(
    #name shuould be same as 'console_scripts': ['helloworld---<
    name = 'helloworld',
    version = '0.1.0',
    packages = ['helloworld'],
    entry_points={
        'console_scripts': ['helloworld=helloworld.__main__:main'],
    }
)




