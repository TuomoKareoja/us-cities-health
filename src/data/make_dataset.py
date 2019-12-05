# -*- coding: utf-8 -*-
import logging
import os
from pathlib import Path

import pandas as pd
from dotenv import find_dotenv, load_dotenv


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("Making final data set from raw data")

    logger.info("Loading data in")
    df = pd.read_csv(os.path.join("data", "raw", "BCHI-dataset_2019-03-04.csv"))

    logger.info("Dropping unneccessary columns, missing and duplicates")

    df.dropna(subset=["Value"], inplace=True)

    columns_to_drop = [
        "Indicator Category",
        "Source",
        "Methods",
        "Notes",
        "BCHC Requested Methodology",
        "90% Confidence Level - Low",
        "90% Confidence Level - High",
        "95% Confidence Level - Low",
        "95% Confidence Level - High",
    ]

    df.drop(columns=columns_to_drop, inplace=True)

    df.drop_duplicates(
        subset=["Indicator", "Year", "Sex", "Race/Ethnicity", "Place"], inplace=True
    )

    logger.info("Unmelting the data")
    df = (
        df.set_index(["Place", "Year", "Sex", "Race/Ethnicity", "Indicator"])["Value"]
        .unstack()
        .reset_index()
    )

    df.columns = df.columns.tolist()

    logger.info("Saving to data/processed/")
    df.to_csv(os.path.join("data", "processed", "bhci.csv"), index=False)


if __name__ == "__main__":
    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
