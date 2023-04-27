import setuptools

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='bandiere',
    version="0.0.1dev",
    #packages=['may_browse'],
    author="balordi LLC",
    license="MIT",
    install_requires=install_requires,
)