# Data Manipulation and Analysis in Python using `pandas`

## NGCM Summer Academy 2017

This tutorial will introduce the use of Python for statistical data analysis, using data stored as pandas DataFrame objects. Much of the work involved in analyzing data resides in importing, cleaning and transforming data in preparation for analysis. Therefore, the first half of the course is comprised of a 2-part overview of basic and intermediate pandas usage that will show how to effectively manipulate datasets in memory. This includes tasks like indexing, alignment, join/merge methods, date/time types, and handling of missing data. Next, we will cover plotting and visualization using pandas and Seaborn, focusing on creating effective visual representations of your data, while avoiding common pitfalls. Finally, participants will be introduced to methods for statistical data modeling using some of the advanced functions in Numpy, Scipy and pandas. This will include fitting statistical models using linear and non-linear models, bootstrapping methods, and imputation of missing data. Each section of the tutorial will involve hands-on manipulation and analysis of sample datasets, to be provided to attendees in advance.

## Instructors

Christopher Fonnesbeck (Vanderbilt University) Skipper Seabold (Civis Analytics)

## Outline

### Monday, June 26

**09:30 - 10:45**

*Intro to NumPy and pandas (Skipper Seabold)*

- NumPy arrays and indexing
- Multidimensional arrays
- Array methods and functions
- Series and DataFrame objects
- Reading and writing files
- Setting options
- Categorical data

**11:00 - 13:15**

*Intermediate pandas (Chris Fonnesbeck)*

- Indexing, data selection and subsetting
- `where` and `query`
- Hierarchical indexing
- Sorting and ranking
- Missing data
- Data summarization

**13:15 - 14:15 Lunch**

**14:15 - 16:00**

*Data Manipulation with pandas (Skipper Seabold)*

- Date/time types
- Merging and joining DataFrame objects
- Concatenation
- Text data operations

**16:15 - 17:30**

*pandas Best Practices (Chris Fonnesbeck)*

- Data aggregation and GroupBy operations
- Reshaping DataFrame objects
- Pivoting
- Data transformation with `assign`
- Method chaining
- `pipe`

### Tuesday, June 27

**09:30 - 10:45**

*High-level Plotting with pandas and Seaborn (Chris Fonnesbeck)*

- Basic plotting with pandas
- Controlling figure aesthetics
- Choosing color palettes
- Visualizing the distribution of a dataset
- Visualizing linear relationships
- Plotting with categorical data
- Plotting on data-aware grids

**11:00 - 13:15**

*Advanced Plotting with Matplotlib and Bokeh (Skipper Seabold)*

- Creating low-level plots with Matplotlib
- Customizing plot attributes
- Building interactive visualizations with Bokeh

**13:15 - 14:15 Lunch**

**14:15 - 16:00**

*Data Analysis with pandas (Chris Fonnesbeck)*

- Statistical operations in pandas
- Fitting regression models
- Bootstrapping
- Working with missing data
- Data analysis with Scikit-learn

**16:15 - 17:30**

*Parallel Computing with Dask (Skipper Seabold)*

- Dask data structures
- Out-of-core/memory workflows: xray


## Prerequisites

This is an intermediate-level computing course, so some previous experience with Python is required. Some undergraduate-level statistics is also recommended.

## Software Requirements

Python 3.5. We recommend installing the free Anaconda distribution of Python, available from Continuum Analytics.

The following packages should be installed on your system:

- jupyter
- ipython>=4.0
- numpy>=1.10
- pandas>=0.18
- scipy
- matplotlib
- scikit-learn
- seaborn
- patsy
- numexpr
- bottleneck
- xlrd
- jinja2
- tornado
- pyzmq
- jsonschema
- mpld3
- dask

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
    
If you are not using the Anaconda Python distribution, you will need to manually install the packages listed in `environment.yml` using `pip`.

Which you probably don't want to do.

So install Anaconda.

To use the environment, you may type:

    source activate ngcm
