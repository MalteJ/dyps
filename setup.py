from setuptools import setup

setup(
    name="dyps",
    version="0.0.1",
    description="repository dependency manager",
    author="Malte Janduda",
    author_email="mail@janduda.net",
    url="https://github.com/MalteJ/dyps/",
    depends=["yaml"],
    scripts = [
        'src/dyps'
    ]
)
