# Pyspark-App
this is simple app just read the csv file transformded it and write it in parquet format created with the help of Pydata talks.
This application uses MovieLens data set as a source data. This data can be downloaded here https://grouplens.org/datasets/movielens/ or using get_data.ipynb notebook included in this repository.
App development steps:
v1.0 - Initial version: how to structure pyspark application
In project folder:
                  App:
                    -	Movies.py
                    -	Movie_genres.py
                  Data:
                         -input:
                                  - movies.csv
                          -ouput:
                                  - movies : parquetsformat data
                                  - movies_genres: : parquetsformat data
Spark-submit: is a part of spark distribution used to launch our pyspark application on cluster. It take care of settings and distribution the code for us.

Command: 1. Spark-submit app/movies.py 
         2. Spark-submit app/movie_genres.py
         
v2.0 - second version: how to structure pyspark application
In project folder:
                  App:
                    -	Movies.py
                    -	Movie_genres.py
                    -	Config.json
                 Data:
                         -input:
                                  - movies.csv
                          -ouput:
                                  - movies : parquetsformat data
                                  - movies_genres: : parquetsformat data
 Config.json: we will separate input and output path of data and app name and keep in json file
{
	  "app_name": "MoviesETL",
	  "source_data_path": "data/ml-latest-small",
	  "output_data_path": "data/output"
	}

Spark-submit: is a part of spark distribution used to launch our pyspark application on cluster. It take care of settings and distribution the code for us.
Command: 
 (sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app> spark-submit --files config.json movies.py            
 (sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>  spark-submit --files config.json movie_genres.py
 
v3.0 – 3rd version: how to structure pyspark application
In project folder:
                  App:
                         -Makefile:
                         -jobs:
                                  __init__.py
                                   Movies.py
                                   Movie_genres.py  
                         -jobs.zip
                        - Config.json
                         -main.py
                        -dist:
                               Jobs.zip
                               Main.py
                              Config.json
                 Data:
                         -input:
                                  - movies.csv
                          -ouput:
                                  - movies : parquetsformat data
                                  - movies_genres: : parquetsformat data
 Config.json: we will separate input and output path of data and app name and keep in json file
{
	  "app_name": "MoviesETL",
	  "source_data_path": "data/ml-latest-small",
	  "output_data_path": "data/output"
	}

Spark-submit: is a part of spark distribution used to launch our pyspark application on cluster. It take care of settings and distribution the code for us.
to run the jobs on cluster we need to run main.py file and specify job name as a job argument and we have -–py-files jobs.zip to add jobs to cluster
our application may contain multiple jobs so we are going to create one entry point main which will run our  multiple jobs so that in future we can add multiple jobs as many as required by application

Command: 
(sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>spark-submit --py-files jobs.zip --files config.json main.py --job movies
 (sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>spark-submit --py-files jobs.zip --files config.json main.py --job movie_genres
 
v4.0 – 4th version: how to structure pyspark application
now we are going to separate data file logic and domain logic.
We create UDF user define functions that work on column label in dataframe
Create a udf.py file.
In project folder:
                  App:
                         -Makefile:
                         -jobs:
                                  __init__.py
                                   Movies.py
                                   Movie_genres.py
                        -jobs.zip
                        - Config.json
                        -main.py
                        -dist:
                               Jobs.zip
                               Main.py
                              Config.json
                       Shared.zip
                      -shared:
                                __init__.py
                                  udf.py
                 Data:
                         -input:
                                  - movies.csv
                          -ouput:
                                  - movies : parquetsformat data
                                  - movies_genres: : parquetsformat data
 Config.json: we will separate input and output path of data and app name and keep in json file
{
	  "app_name": "MoviesETL",
	  "source_data_path": "data/ml-latest-small",
	  "output_data_path": "data/output"
	}

Spark-submit: is a part of spark distribution used to launch our pyspark application on cluster. It take care of settings and distribution the code for us.
to run the jobs on cluster we need to run main.py file and specify job name as a job argument and we have -–py-files jobs.zip ,shared.zip to add jobs to cluster
our application may contain multiple jobs so we are going to create one entry point main which will run our  multiple jobs so that in future we can add multiple jobs as many as required by application

Command: 
(sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>spark-submit --py-files jobs.zip,shared.zip --files config.json main.py --job movies
 (sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>spark-submit --py-files jobs.zip,shared.zip --files config.json main.py --job movie_genres

v5.0 – 5th version: how to structure pyspark application
now we are going to add third party dependency in libs folder inside dist folder
and add app/libs.zip
Command: 
(sparkenv) C:\Users\ARYAN\Desktop\SparkApplication\sparkapp\app>spark-submit --py-files jobs.zip,shared.zip,libs.zip --files config.json main.py --job movies
And finally add tests: 
                                Test_movies.py
                                 Test_udf.py
