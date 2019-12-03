from setuptools import setup, find_packages
setup(
    name='elf-hunter',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'elf-hunter = elf_hunter:run',
        ],
    },
)
