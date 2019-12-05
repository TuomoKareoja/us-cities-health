# %%

import os

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import pandas as pd
import seaborn as sns
from dotenv import find_dotenv, load_dotenv
from IPython.core.interactiveshell import InteractiveShell

# Setting styles
InteractiveShell.ast_node_interactivity = "all"
sns.set(style="whitegrid", color_codes=True, rc={"figure.figsize": (12.7, 9.27)})

# %% load data

df = pd.read_csv(os.path.join("data", "processed", "bhci.csv"))

# %%

df.head()

# %%

df.isna().sum()

# %%

df_all_eth_sex = df[(df["Race/Ethnicity"] == "All") & (df["Sex"] == "Both")].copy()
df_all_eth_sex.drop(columns=["Race/Ethnicity", "Sex"], inplace=True)

# %%

df_all_eth_sex.isna().sum()

# %%

indicators = [
    "AIDS Diagnoses Rate (Per 100,000 people)",
    "All Types of Cancer Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "All-Cause Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Asthma Emergency Department Visit Rate (Age-Adjusted; Per 10,000)",
    "Bike Score",
    "Chlamydia Rate (Per 100,000 People)",
    "Congenital Syphilis Rate (Per 100,000 Live Births)",
    "Diabetes Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Female Breast Cancer Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Firearm-Related Emergency Department Visit Rate (Age-Adjusted; Per 10,000 people)",
    "Firearm-Related Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Gonorrhea Rate (Per 100,000 People)",
    "HIV Diagnoses Rate (Per 100,000 people)",
    "HIV-Related Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Heart Disease Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Homicide Rate (Age-Adjusted; Per 100,000 people)",
    "Infant Mortality Rate (Per 1,000 live births)",
    "Life Expectancy at Birth (Years)",
    "Lung Cancer Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Median Household Income (Dollars)",
    "Motor Vehicle Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Opioid-Related Unintentional Drug Overdose Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Percent Foreign Born",
    "Percent Living Below 200% Poverty Level",
    "Percent Unemployed",
    "Percent Who Only Speak English at Home",
    "Percent Who Speak Spanish at Home",
    "Percent of 3 and 4 Year Olds Currently Enrolled in Preschool",
    "Percent of Adults 65 and Over Who Received Pneumonia Vaccine",
    "Percent of Adults Who Are Obese",
    "Percent of Adults Who Binge Drank",
    "Percent of Adults Who Currently Smoke",
    "Percent of Adults Who Meet CDC-Recommended Physical Activity Levels",
    "Percent of Adults Who Received Seasonal Flu Shot",
    "Percent of Children (Tested) Under Age 6 with Elevated Blood Lead Levels",
    "Percent of Children Living in Poverty",
    "Percent of Children Who Received Seasonal Flu Shot",
    "Percent of High School Graduates (Over Age 18)",
    "Percent of High School Students Who Are Obese",
    "Percent of High School Students Who Binge Drank",
    "Percent of High School Students Who Currently Smoke",
    "Percent of High School Students Who Meet CDC-Recommended Physical Activity Levels",
    "Percent of Households Whose Housing Costs Exceed 35% of Income",
    "Percent of Low Birth Weight Babies Born",
    "Percent of Mothers Under Age 20",
    "Percent of Population 65 and Over",
    "Percent of Population Under 18",
    "Percent of Population Uninsured",
    "Percent of Population with a Disability",
    "Persons Living with HIV/AIDS Rate (Per 100,000 people)",
    "Pneumonia and Influenza Mortality Rate (Age-Adjusted; Per 100,000 people)",
    "Primary and Secondary Syphilis Rate (Per 100,000 People)",
    "Race/Ethnicity (Percent)",
    "Rate of Laboratory Confirmed Infections Caused by Salmonella (Per 100,000 people)",
    "Rate of Laboratory Confirmed Infections Caused by Shiga Toxin-Producing E-Coli (Per 100,000 people)",
    "Sex (Percent)",
    "Suicide Rate (Age-Adjusted; Per 100,000 people)",
    "Total Population (People)",
    "Transit Score",
    "Tuberculosis Incidence Rate (Per 100,000 people)",
    "Walkability",
]


# %% initial exploration

for indicator in indicators:
    sns.lineplot(x="Year", y=indicator, hue="Place", data=df_all_eth_sex)
    plt.title(indicator)
    plt.show()

# %% Opioids

fig = px.line(
    df_all_eth_sex,
    x="Year",
    y="Opioid-Related Unintentional Drug Overdose Mortality Rate (Age-Adjusted; Per 100,000 people)",
    color="Place",
)
fig.show()

# %%
