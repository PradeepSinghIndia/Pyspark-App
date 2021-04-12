#!/usr/bin/env python
# coding: utf-8
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
# create spark context or get allready created
spark = SparkSession.builder.appName("Movies").getOrCreate()
#read csv file and create a dataframe
raw_df = (
    spark.read.format("csv")
    .option("header", "true")
    .load("../data/ml-latest-small/movies.csv")
)
# select movies columns and manipulate it
transformed_df = raw_df.select(
    col("movieId"),
    expr("substring(title, 1, length(title)-6)").alias("title"),
    col("title").substr(-5, 4).alias("year"),
)
# write data in parquet format
transformed_df.write.mode("overwrite").parquet("../data/output/movies")





