from pyspark.sql import SparkSession
import pyspark.sql.functions as F
import requests

def main():
    spark = SparkSession.builder.appName("DataRequest").getOrCreate()
    
    response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=256da2d742d5a5979790e6833447e4b4').json()
    df = spark.createDataFrame(response['results'])
    df_movies = df.select('title', 'release_date', 'overview', 'vote_average')

    # Define GMT-3 timezone
    gmt_minus_3 = "America/Sao_Paulo"  # Brazil time zone

    # Add column with current timestamp converted to GMT-3
    df_movies = df_movies.withColumn("execution_timestamp", F.from_utc_timestamp(F.current_timestamp(), gmt_minus_3))


    df_movies.write.mode("append").parquet("/home/jupyter/app/data/movies.parquet")
    spark.stop()

if __name__ == "__main__":
    main()