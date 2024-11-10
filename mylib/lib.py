import os
import requests
import io
import pandas as pd
from pyspark.sql import SparkSession

from pyspark.sql.types import (
     StructType, 
     StructField, 
     IntegerType, 
     StringType, 
)

LOG_FILE = "nutrition_analysis.md"

def log_output(operation, output, query=None):
    """adds to a markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"## {operation}\n\n")
        if query: 
            file.write(f"### Query\n```sql\n{query}\n```\n\n")
        file.write("### Output\n")
        file.write(output)
        file.write("\n\n")

def create_spark_session(app_name="ETL Job"):
    return SparkSession.builder.appName(app_name).getOrCreate()

def end_spark_session(spark):
    spark.stop()

def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/master/nutrition-studies/raw_anonymized_data.csv",
    file_path="data/Nutrition.csv",
    directory="data",
):
    """
    Extract a dataset from a URL and save it locally
    """
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Download the dataset with error handling
    response = requests.get(url)
    response.raise_for_status()
    
    # Load into pandas and select columns
    df = pd.read_csv(io.StringIO(response.text))
    selected_columns = [
        "ID", "cancer", "diabetes", "heart_disease", "EGGSFREQ", 
        "GREENSALADFREQ", "FRIESFREQ", "MILKFREQ", "SODAFREQ", 
        "COFFEEFREQ", "CAKESFREQ"
    ]
    df_subset = df[selected_columns]
    
    # Save the subset
    df_subset.to_csv(file_path, index=False)
    
    return file_path

def load_data(spark, data="data/Nutrition.csv"):
    # Define schema for the pre-filtered columns
    schema = StructType([
        StructField("ID", IntegerType(), True),
        StructField("cancer", StringType(), True),
        StructField("diabetes", StringType(), True),
        StructField("heart_disease", StringType(), True),
        StructField("EGGSFREQ", IntegerType(), True),
        StructField("GREENSALADFREQ", IntegerType(), True),
        StructField("FRIESFREQ", IntegerType(), True),
        StructField("MILKFREQ", IntegerType(), True),
        StructField("SODAFREQ", IntegerType(), True),
        StructField("COFFEEFREQ", IntegerType(), True),
        StructField("CAKESFREQ", IntegerType(), True)
    ])
    
    # Read CSV with schema
    df = spark.read.format("csv") \
        .option("header", "true") \
        .schema(schema) \
        .load(data)
    
    # Check if file doesn't exist or is empty
    if not os.path.exists('nutrition_analysis.md') or os.path.getsize('nutrition_analysis.md') == 0:
        log_output("Load Data (First 10 Rows)", df.limit(10).toPandas().to_markdown())
    return df


def query(spark, df, query_string):
    # Register the DataFrame as a temporary view before querying
    df.createOrReplaceTempView("Nutrition")
    result_df = spark.sql(query_string)
    # Log the query and its results
    log_output("SQL Query Results", result_df.limit(20).toPandas().to_markdown(), query=query_string)
    return result_df


def transform_data(df):
    """Transform the data by adding healthy and unhealthy food totals and health condition flag"""
    
    # Create healthy foods total (eggs, salad, milk, coffee)
    df = df.withColumn('healthy_total', 
        df.EGGSFREQ + df.GREENSALADFREQ + df.MILKFREQ + df.COFFEEFREQ)
    
    # Create unhealthy foods total (fries, soda, cakes)
    df = df.withColumn('unhealthy_total',
        df.FRIESFREQ + df.SODAFREQ + df.CAKESFREQ)
    
    # Create has_health_condition flag
    df = df.withColumn('has_health_condition',
        (df.cancer == "Yes") | 
        (df.diabetes == "Yes") | 
        (df.heart_disease == "Yes"))
    
    # Select only the required columns
    transformed_df = df.select(
        "ID",
        "healthy_total",
        "unhealthy_total",
        "has_health_condition"
    )
    
    log_output("Data Transformation (First 20 Rows)", transformed_df.limit(20).toPandas().to_markdown())

    return transformed_df






