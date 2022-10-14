import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(name="packaging_demo",
                 version="0.0.1",
                 author="Doug",
                 author_email="dbergman@sorenson.com",
                 packages=["word_counter"],
                 description="A package to practice packaging itself",
                 long_description=description,
                 license='MIT',
                 url='git@github.com:dbergman-sorenson/hello_worlds.git',
                 requires=[])
