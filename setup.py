import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "datawise",
    version = "0.0.6",
    author = "DataWise Team",
    description = ("DataWise"),
    license = "Apache 2.0",
    keywords = "datawise data-analysis data-science pandas numpy",
    url = "https://pypi.org/project/datawise/",
    long_description=read('README.md'),
)