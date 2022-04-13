import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitsecrets-JustinGuese",
    version="0.0.1",
    author="Justin Guese",
    author_email="guese.justin@gmail.com",
    description="A package to safely encrypt files and secrets in a Github repository using a password.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JustinGuese/pip-gitsecrets/",
    project_urls={
        "Bug Tracker": "https://github.com/JustinGuese/pip-gitsecrets/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires = ["cryptography"],
)