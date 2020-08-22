import setuptools

with open('README.md','r') as fh:
    long_description = fh.read()


setuptools.setup(
    name="champakraja",
    version="1.0.0",
    author="jeldikk",
    author_email="jeldi.kamal2011@gmail.com",
    description="a small comic inspired from a movie",
    long_description = long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/jeldikk/champakraja",
    packages=['champakraja'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)