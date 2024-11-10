import os
from mylib.lib import (
    extract,
    load_data,
    transform_data,
    query,
    create_spark_session,
    end_spark_session,
)


def main():
    # delete nutrition_analysis.md if it exists
    if os.path.exists("nutrition_analysis.md"):
        os.remove("nutrition_analysis.md")
    # define queries
    my_query = """SELECT 
        ID, 
        SODAFREQ, 
        EGGSFREQ, 
        FRIESFREQ 
    FROM Nutrition 
    WHERE SODAFREQ > 3 
    ORDER BY SODAFREQ DESC 
    LIMIT 5"""

    my_query_2 = """SELECT 
        AVG(EGGSFREQ) as avg_eggs,
        AVG(GREENSALADFREQ) as avg_salad,
        AVG(FRIESFREQ) as avg_fries,
        AVG(MILKFREQ) as avg_milk,
        AVG(SODAFREQ) as avg_soda,
        AVG(COFFEEFREQ) as avg_coffee,
        AVG(CAKESFREQ) as avg_cakes
    FROM Nutrition"""
    # extract data
    extract()
    # start spark session
    spark = create_spark_session()
    # load data into dataframe
    df = load_data(spark)
    # Register the DataFrame as a temporary view
    df.createOrReplaceTempView("Nutrition")
    # query
    query(spark, df, my_query)
    query(spark, df, my_query_2)
    # transform
    transform_data(df)
    # end spark session
    end_spark_session(spark)


if __name__ == "__main__":
    main()
