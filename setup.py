import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="remaining-lifetime",
    version="0.0.3",
    author="Jon Besga",
    author_email="jonan.bsg@gmail.com",
    description="Remaining lifetime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonbesga/remaining-lifetime",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['remaining-life=remaininglife.__main__:main'],
    },
    package_data={'': ['life_expectancy_country.csv']},
    include_package_data=True,
)