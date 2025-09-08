import pandas as pd

# OPTION 1
# Load csv from the computer
iris_df = pd.read_csv("iris.csv")    # returns pandas.DataFrame

# OPTION 2
# Load csv from the internet
malaria_df = pd.read_csv("https://people.sc.fsu.edu/~jburkardt/datasets/iswr/malaria.csv")
iris_df = pd.read_csv("https://raw.githubusercontent.com/hogeschool/CMIBOD021T-2526/refs/heads/main/data/datasets/iris.csv")

# OPTION 3
# Load Dataset from a python library: seaborn, statsmodels, scikit-learn
# I think best option is statsmodels because output can be easily converted into a DataFrame and it contains documentation

# library       method                  returns                 containsDocumentation?
# seaborn       load_dataset()          pandas.DataFrame        NO
# statsmodels   get_rdataset()          statsmodels.Dataset     YES
# scikit-learn  load_*() or fetch_*()   Bunch                   YES

########### SEABORN
import seaborn as sns
iris_df1 = sns.load_dataset("iris")   # returns pandas.Dataframe directly but misses documentation

########### STATSMODELS
# statsmodels dataset easily convertible to dataframes and contain documentation. 
# Easy access to R datasets through get_rdataset()
import statsmodels.api as sm

# Example: Load a sample dataset
iris_ds = sm.datasets.get_rdataset("iris") # returns statsmodels Dataset type which contains metadata
iris_doc = iris_ds.__doc__                 # returns string with documentation
iris_df2 = iris_ds.data                    # returns Pandas DataFrame

########### SCIKIT-LEARN
# Not as straightforward to convert to dataframe.
from sklearn.datasets import load_iris
iris_bunch = load_iris()            # returns object of type Bunch
iris_doc = load_iris().DESCR        # returns string

# Convert Bunch to Pandas.DataFrame
iris_df3 = pd.DataFrame(data=iris_bunch.data, columns=iris_bunch.feature_names)