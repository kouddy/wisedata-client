import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "wisedata",
    version = "1.0.13",
    author = "WiseData Team <wisedata.help@gmail.com>",
    description = ("AI Assistant for Python Data Analytics"),
    license = "Apache 2.0",
    keywords = "wisedata data-analysis data-science pandas numpy",
    url = "https://www.wisedata.app/",
    long_description=read('README.md'),
)