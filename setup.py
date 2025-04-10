from setuptools import setup, find_packages

setup(
    name="lunarscan",
    version="0.1.0",
    author="Lunar Team",
    author_email="64bit-lunarteam@gmail.com",
    description="A simple network port scanning and geolocation tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/64bit-lunarteam/LunarScan",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["requests"],
)
