from setuptools import setup, find_packages

setup(
    name="markdown_table",
    version="1.0.0",
    author="Kitsumetri",
    author_email="no_email@example.com",
    description="A library for generating Markdown tables.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Kitsumetri/md_table_generator",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
