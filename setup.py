import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="requestspwn",
    version="1.0.0",
    author="Pietro Ferretti",
    author_email="me@pietroferretti.com",
    description="Drop-in replacement for the requests library with random user agents as default.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pietroferretti/requestspwn",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={"requestspwn": ["data/*"]},
    package_dir={"requestspwn": "requestspwn"},
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="ctf http",
    project_urls={
        "Source": "https://github.com/pietroferretti/requestspwn"
    },
)
