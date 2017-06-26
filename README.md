# Data Manipulation and Analysis in Python using `pandas`

## NGCM Summer Academy 2017

This tutorial will introduce the use of Python for statistical data analysis, using data stored as pandas DataFrame objects. Much of the work involved in analyzing data resides in importing, cleaning and transforming data in preparation for analysis. Therefore, the first half of the course is comprised of a 2-part overview of basic and intermediate pandas usage that will show how to effectively manipulate datasets in memory. This includes tasks like indexing, alignment, join/merge methods, date/time types, and handling of missing data. Next, we will cover plotting and visualization using pandas and Seaborn, focusing on creating effective visual representations of your data, while avoiding common pitfalls. Finally, participants will be introduced to methods for statistical data modeling using some of the advanced functions in Numpy, Scipy and pandas. This will include fitting statistical models using linear and non-linear models, bootstrapping methods, and imputation of missing data. Each section of the tutorial will involve hands-on manipulation and analysis of sample datasets, to be provided to attendees in advance.

## Instructors

Christopher Fonnesbeck (Vanderbilt University)  
Skipper Seabold (Civis Analytics)

## Outline

### Introduction to NumPy and Pandas (SS)
- Introduction to NumPy
- Import Convention
- NumPy Arrays and Indexing
- Exercise: Random numbers
- Index Arrays
- Multidimensional Arrays
- Array Operations, Methods, and Functions
- Introduction to Pandas
- Pandas Series
- Pandas DataFrames
- Reading and Writing Files
### Indexing, Selection and Operations (CF)
- Indexing and Selection
- Indexing with where
- Selection with query
- Operations
- Sorting and Ranking
- Hierarchical indexing
- Missing data
- Data summarization
- Writing Data to Files
### Data Manipulation with Pandas (SS)
- Categorical Types
- Date and Time Types
- Merging and Joining DataFrames
- Concatenation
- Text Data Manipulation
### Pandas Best Practices (CF)
- Reshaping DataFrame objects
- Method chaining
- Pivoting
- Data transformation
- Categorical Variables
- Data aggregation and GroupBy operations
### High-level Plotting with Pandas and Seaborn (SS)
- Bar plots
- Histograms
- Boxplots
- Scatterplots
- Introduction to Seaborn
- Customizing Seaborn Figure Aesthetics
- Plotting Small Multiples on Data-aware Grids
### Performance Pandas (CF)
- cython
- numba
- eval with numexp
- sparse data structures
### Dask (SS)
- Introduction
- Dask Array
- Performance vs. NumPy
- Linear Algebra
- Dask Bag
- Dask DataFrame
- DataFrame API
- Aside on Storage Formats: Thinking about Computers
- Dask Resources


## Prerequisites

This is an intermediate-level computing course, so some previous experience with Python is required. Some undergraduate-level statistics is also recommended.

## Software Requirements

Python 3.6. We recommend installing the free Anaconda distribution of Python, available from Continuum Analytics.

The following packages should be installed on your system:

- cython
- dask
- ipython
- ipywidgets
- jupyter
- line_profiler
- matplotlib
- notebook
- numba 
- numexpr
- numpy
- pandas
- pip
- pprofile
- pyzmq
- scipy
- seaborn
- snakeviz
- sympy

If you have installed Anaconda, these should already be available to you.

## Getting this repository

    git clone https://github.com/fonnesbeck/ngcm_pandas_2017.git

If you are not familiar with Git and GitHub, you can simply download the zip file of the repository at the top of the main repository page.

Then, move to the directory created by the clone/zip file:

    cd ngcm_pandas_2017

and install everything using `conda`:

    conda config --add channels conda-forge
    conda env create -f environment.yml

This will create an **environment** called `ngcm` that includes the packages required for the course.    
​    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Anaconda.

To use the environment, you may type:

    source activate ngcm
