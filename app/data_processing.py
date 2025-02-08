from pyspark.sql import SparkSession
import pyspark.sql.functions as F

def main():
    spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()
    
    df_movies = spark.read.parquet("/home/jupyter/app/data/movies.parquet")

    df_movies = df_movies.withColumn("release_year", F.year(F.col("release_date")))\
                        .withColumn("Status", F.lit('Processed Data'))
    # Define GMT-3 timezone
    gmt_minus_3 = "America/Sao_Paulo"  # Brazil time zone

    # Add column with current timestamp converted to GMT-3
    df_movies = df_movies.withColumn("execution_timestamp", F.from_utc_timestamp(F.current_timestamp(), gmt_minus_3))


    df_movies.write.mode("overwrite").parquet("/home/jupyter/app/data/movies_processed.parquet")
    spark.stop()

if __name__ == "__main__":
    main()