from setuptools import setup, find_packages

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
# NAME = "groq-llm-api"
# VERSION = "0.5.0"
# PYTHON_REQUIRES = ">=3.7"
# REQUIRES = [
#     "protobuf >=3.5.0, < 4.0dev",
#     "grpcio >= 1.42.0",
#     "google-api-python-client >= 2.53.0"
# ]

setup(
    # name=NAME,
    # version=VERSION,
    # description="Groq API Python",
    # author="Groq",
    # author_email="",
    # url="",
    # keywords=["Groq API"],
    # install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True
    # python_requires=PYTHON_REQUIRES,
    # long_description_content_type='text/markdown',
    # long_description="""\
    # The Groq Python API.
    # """,  # noqa: E501
)