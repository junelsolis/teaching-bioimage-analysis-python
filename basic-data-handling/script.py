import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats

# Book 1
# How to read a CSV file into a data table


# Simple math
a = 3
b = 5

print(a + b)
print(10 / 2)
print(type(10 / 2))
print(int(10 / 2))
print(type(int(10 / 2)))
print(type(str(10 / 2)))

# modulo operator
print(10 % 2)
print(10 % 3)

# strings
str_1 = "I am "
str_2 = "having fun"

print(str_1 + str_2)
print(f"{str_1} able to do basic match, and I am {str_2}.")

# reading CSV's into Pandas dataframes
df1 = pd.read_csv("data/Results_01.csv")
df1.head()
df1.describe()
type(df1)

# getting basic statistics
df1["Area"]
df1["Area"].describe()

df1.columns = (
    "",
    "label",
    "area",
    "perimeter",
    "circularity",
    "ar",
    "roundness",
    "solidity",
)
df1.describe()

# Book 2
# How to do simple plots with Pandas
df1.hist(column="Area")


# Book 3
# How to concatenate data frames

# Add a column to descrite the "student" who made the analysis
df1["Student"] = "01"
df1.to_string()

# Read a second dataset and add an extra "student"
df2 = pd.read_csv("data/Results_02.csv")
df2["Student"] = "02"
df2.head()

# Let's see if there are differences in the datasets
print(f"Area mean for student 1 is: {df1['Area'].mean():.3f}.")
print(f"Area mean for student 2 is: {df2['Area'].mean():.3f}.")

# Instead of keeping track of different data framese, it is easier to put these tables together. This is called concatenation
df = pd.concat([df1, df2])
df.head()

# Let us do a basic boxplot to see if the results of both studnets are significanlty different from one another.
df.boxplot(column="Area", by="Student")

# Saving Pandas data frames into new CSV files
df.to_csv("data/Results_total.csv")

# Book 4
# Elaborate plots using seaborn sns
sns.violinplot(x="Student", y="Area", data=df)

# Programming cases
myVariableName = None  # camelCase
my_variable_name = None  # snake_case
# my-variable-name # kebab-case
MyVariableName = None  # PascalCase
MY_VARIABLE_NAME = None  # UPPER_CASE_SNAKE_CASE

# Book 5

# For clarity let us get out the data of interest from the
# data table by using the 'query' method of the dataframe.
area_s1 = df.query("Student == '01'")["Area"]
area_s2 = df.query("Student == '02'")["Area"]

# Before using a t-test, one must check for independence, normality, and homogeneity.

# Homogeneity
stats.levene(area_s1, area_s2)

# Shapiro-Wilk (SW) test for normality
# Checks whether the datasets follow a Gaussian distribution
# If p-value < 0.05, then reject the null hypothesis that data is drawn from a normal distribution
stats.shapiro(area_s1)
stats.shapiro(area_s2)

# The actual t-test
stats.ttest_ind(area_s1, area_s2)


# Book 6
pivot_table = pd.pivot_table(
    data=df, index=["Student"], values="AR", aggfunc=["sum", "mean"]
)
pivot_table.head()

# Book 7
# Plotting mean speed over time for a movie.
#
path = "data/TrackMate-edgeTable.csv"
df = pd.read_csv(path)
df = df.drop([0, 1, 2])

df.head()

df = df.drop(labels="LABEL", axis=1)
df = df.apply(pd.to_numeric)
df.head()

# We want to compute the mean of the SPEED values, but averaged
# over all the cells in a given time-point. The time-piont is
# indexed in the table by the feature EDGE_TIME.

# So we want to group all values based on EDGE_TIME, and take the
# mean over all the SPEED values for rows that have a common EDGE_TIME value.

# In Pandas this is done using the 'groupby' method.

# Make a new table where we group everything by 'EDGE_TIME'
# and wilthin a group, compute the mean of 'SPEED'
speed_df = df.groupby("EDGE_TIME")[["SPEED"]].mean()
speed_df.head()
speed_df

# Plot it
speed_df["SPEED"].plot(x="time (min)", y="cell speed (pixel/min")

# use rolling median to filter the data
speed_df["FILTERED_SPEED"] = speed_df["SPEED"].rolling(5, center=True).median()

# Plot the filtered speed
speed_df["FILTERED_SPEED"].plot(x="time (min)", y="cell speed (pixel/min")
