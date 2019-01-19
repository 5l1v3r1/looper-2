with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="looper",
    version="0.1",
    author="Akere Mukhtar Abiodun",
    author_email="akeremukhtar10@gmail.com",
    description= "An email scrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url= "https://github.com/sirrobot01/Looper"
    packages=setuptools.find_packages(),
    scripts = ["looper"]
)