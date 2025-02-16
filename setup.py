from setuptools import setup, find_packages

setup(
    name="trove-ai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
        "python-dotenv"
    ],
    author="Your Name",
    description="A modular AI agent framework for intelligent automation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/trove",
    license="MIT",
)
