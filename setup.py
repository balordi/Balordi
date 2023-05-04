import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='bandiere',
    version="0.0.1dev",
    packages=['bandiere'],
    package_dir={'bandiere': 'src/bandiere'},
    package_data={'bandiere': ['data/*.csv']},
    author="balordi LLC",
    license="MIT",
    install_requires=install_requires,
    include_package_data=True
)