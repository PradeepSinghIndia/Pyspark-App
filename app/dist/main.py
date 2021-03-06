#!/usr/bin/env python
# coding: utf-8
import json
import importlib
import argparse
from pyspark.sql import SparkSession


def _parse_arguments():
    """ Parse arguments provided by spark-submit command"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--job", required=True)
    return parser.parse_args()


def main():
    """ Main function excecuted by spark-submit command"""
    args = _parse_arguments()

    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    spark = SparkSession.builder.appName(config.get("app_name")).getOrCreate()
    if args.job=="test_movies":
        job_module = importlib.import_module(f"tests.{args.job}")
        job_module.TestMoviesJob().test_transform_data(spark)
        job_module.TestMoviesJob().test_run_job(spark, mocker)	    
    else:
        job_module = importlib.import_module(f"jobs.{args.job}")
        job_module.run_job(spark, config) 
           
	    

if __name__ == "__main__":
    main()