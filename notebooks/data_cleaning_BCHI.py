# %%

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import sklearn
from dotenv import find_dotenv, load_dotenv
from IPython.core.interactiveshell import InteractiveShell

# Setting styles
InteractiveShell.ast_node_interactivity = "all"
sns.set(style="whitegrid", color_codes=True, rc={"figure.figsize": (12.7, 9.27)})

# %% load data

df = pd.read_csv(os.path.join("data", "raw", "BCHI-dataset_2019-03-04.csv"))

# %% data check

df.head()
df.dtypes
df.isna().sum()

# %% dropping empty values

# when we pivot the data these values will "come back"
# as nulls anyway
df.isna().sum()
df.dropna(subset=["Value"], inplace=True)

# %% dropping unnecessary columns

columns_to_drop = [
    "Indicator Category",
    "Source",
    "Methods",
    "BCHC Requested Methodology",
    "90% Confidence Level - Low",
    "90% Confidence Level - High",
    "95% Confidence Level - Low",
    "95% Confidence Level - High",
]

df.drop(columns=columns_to_drop, inplace=True)

# %% Check duplicates

df.duplicated().sum()
df.loc[df.duplicated(), :]
# No duplicates

# %% Duplicate check for only future temporary index columns

df.drop(columns="Value").duplicated().sum()
df.loc[df.drop(columns="Value").duplicated(), :]

# There are 85 cases where there is multiple different values for
# the same indicator. There is not really much that can be done
# here without dwellwing really deep in to the methods. We try
# to avoid it here so we just drop the duplicates

df.drop_duplicates(
    subset=["Indicator", "Year", "Sex", "Race/Ethnicity", "Place", "Notes"],
    inplace=True,
)

# %% Checking the notes and seeing if some the values should be dropped

df.Notes.value_counts()

# there seems to lots notes where there is mention that the
# value is calculated with range of years. Lets see if some of these should be dropped

# %% dropping duplicates

# Being bit rough with the data now and just dropping all duplicates regardless
# of notes

df.drop(columns="Notes", inplace=True)
# this just keeps one of the multiple options for the same indicator if
# multiple values present
df.drop_duplicates(
    subset=["Place", "Year", "Sex", "Race/Ethnicity", "Indicator"], inplace=True
)

# %%

df = (
    df.set_index(["Place", "Year", "Sex", "Race/Ethnicity", "Indicator"])["Value"]
    .unstack()
    .reset_index()
)
df.columns = df.columns.tolist()

# %%

df.shape
df.head()
df.dtypes
df.isna().sum()

