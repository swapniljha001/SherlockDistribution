from setuptools import setup, find_packages
setup(
    name="SherlockDistribution",
    version="1.0",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["docutils>=0.3"],

    # metadata to display on PyPI
    author="Swapnil Jha",
    author_email="swapniljha001@gmail.com",
    description="Gaussian and Binomial distributions",
    long_description="This is a simple package to be able to initialize and use Gaussian and Binomial Distributions. \
    This package also defines magic methods to enable the user to add two or more distributions. \
    \
    Working on addition of binomial distributions with unequal probabilities.",
    
    project_urls={
        "Author LinkedIn": "https://www.linkedin.com/in/swapniljha001",
    },
  zip_safe=False)