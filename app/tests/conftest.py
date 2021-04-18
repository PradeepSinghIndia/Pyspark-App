import pytest
from pyspark.sql import SparkSession
@pytest.fixture(scope='module')
def spark_session():
   spark=SparkSession.builder.appName("Test").getOrCreate()
   return spark
   
    

   