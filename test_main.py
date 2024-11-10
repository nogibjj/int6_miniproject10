import os
import pytest
from mylib.lib import (
    extract,
    load_data,
    query,
    transform_data,
    create_spark_session,
    end_spark_session,
)


@pytest.fixture(scope="module")
def spark():
    spark = create_spark_session()
    yield spark
    end_spark_session(spark)


def test_extract():
    file_path = extract()
    assert os.path.exists(file_path) is True


def test_load_data(spark):
    df = load_data(spark)
    assert df is not None


def test_query(spark):
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
    df = load_data(spark)
    result = query(spark, df, my_query)
    result2 = query(spark, df, my_query_2)
    assert result is not None
    assert result2 is not None


def test_transform(spark):
    df = load_data(spark)
    result = transform_data(df)
    assert result is not None


if __name__ == "__main__":
    test_extract()
    test_load_data(spark)
    test_query(spark)
    test_transform(spark)
