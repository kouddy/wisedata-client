import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "datawise",
    version = "0.0.20",
    author = "DataWise Team",
    description = ("AI Assistant for Python Data Analytics"),
    license = "Apache 2.0",
    keywords = "datawise data-analysis data-science pandas numpy",
    url = "https://pypi.org/project/datawise/",
    long_description=read('README.md'),
)