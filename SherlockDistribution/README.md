# SherlockDistribution package

This is a simple package to be able to initialize and use Gaussian and Binomial Distributions.

This package also defines magic methods to enable the user to add two or more distributions.

# Future Updates will include- 
Working on addition of binomial distributions with unequal probabilities.

# Files

* `setup.py`
It installs the Python Package to the Python Installation directory, it is executed by the Python Package Manager.

* `Generaldistribution.py`
It defines a generic distribution parent class and a read_data_file() to read data.

* `Gaussiandistribution.py`
It defines the Gaussian child class and functions such as calculate_mean(), calculate_stdev(), plot_histogram(), pdf(), plot_histogram_pdf() which are used to calculate the mean, standard deviation, plot histogram, calculate the probability distribution function, and plot the histogram of the probability distribution function of the specified Gaussian distribution respectively.

It also contains magic methods such as `__add__()` and `__repr__()` which are used to overwrite the add and represent functions of Python to be able to support the Gaussian class. 

* `Binomialdistrbution.py`
It defines the Binomial child class and functions as calculate_mean(), calculate_stdev(), replace_stats_with_data(), plot_bar(), pdf(), plot_bar_pdf() which are used to calculate the mean, standard deviation, plot bar graph, calculate the probability distribution function, and plot the bar graph of the probability distribution function of the specified Binomial distribution respectively.

It also contains magic methods such as `__add__()` and `__repr__()` which are used to overwrite the add and represent functions of Python to be able to support the Binomial class.

Currently it can only add the Binomial distribution objects with same probability, but the addition of Binomial distribution objects with unequal probabilities will be added in future updates. 

* `__init__.py`
It contains the initialization of the Python package and is used to classify this folder and collection of python scripts as a Python Package.

* `license.txt`
It contains the open source license of this Python package.

# Installation
Use the command:

```
pip install SherlockDistribution
```