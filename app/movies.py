#!/usr/bin/env python
# coding: utf-8
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
import json
with open("config.json","r") as config_file:
    config=json.load(config_file)# load as a python dictionary
spark = SparkSession.builder.appName(config.get("app_name")).getOrCreate()  
raw_df = (
    spark.read.format("csv")
    .option("header", "true")
    .load(f"../{config.get('source_data_path')}/movies.csv")
)

transformed_df = raw_df.select(
    col("movieId"),
    expr("substring(title, 1, length(title)-6)").alias("title"),
    col("title").substr(-5, 4).alias("year"),
)

transformed_df.write.mode("overwrite").parquet(f"../{config.get('source_data_path')}/movies")




