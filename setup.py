import setuptools

setuptools.setup(
    name='itunes',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
