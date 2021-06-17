from setuptools import setup, find_packages
from glob import glob

setup(
    name = 'vipcolors',
    packages = find_packages(),
    include_package_data=True,
    version = '21.06.15.0',
    license = 'GNU GPLv3',
    platforms = 'any',
    description = 'A collection of color schemes with interpolation resources',
    author = 'Julio Trevisan',
    author_email = 'juliotrevisan@gmail.com',
    url = 'http://github.com/trevisanj/vipcolors',
    keywords= [],
    install_requires = ["pygame"],
    python_requires = '>=3',
    scripts = glob('vipcolors/scripts/*.py')
)
