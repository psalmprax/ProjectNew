from pyspark.sql.functions import (
    from_json, col, window, avg, desc, max, min, count, countDistinct)

from spark_base import Source
from schema.data_models import data_model_schema


def connect_to_kafka_stream(topic_name, spark_session):
    return (spark_session
            .readStream
            .format("kafka")
            .option("kafka.bootstrap.servers", "http://kafka:29092")
            .option("subscribe", topic_name)
            .option("startingOffsets", "earliest")
            .load())


def calculate_simple_moving_total(dataframe):
    w = window(
        timeColumn="date_time",
        windowDuration="60 seconds",
        slideDuration="20 seconds")
    # Milliseconds to UTC
    return (df.selectExpr("CAST(value AS STRING) AS json")
            .select(from_json(col("json"), data_model_schema).alias("data"))
            .select("data.*", (col("data.timestamp_logger") / 1000)
                    .cast("timestamp").alias("date_time"))
            .withWatermark("date_time", "20 seconds")
            .groupBy(col("country"), w)
            .agg(count("id"))
            .select("country", "window", col("count(id)").alias("total"))
            )


def calculate_simple_current_users(dataframe):
    w = window(
        timeColumn="date_time",
        windowDuration="60 seconds",
        slideDuration="20 seconds")
    # Milliseconds to UTC
    return (df.selectExpr("CAST(value AS STRING) AS json")
            .select(from_json(col("json"), data_model_schema).alias("data"))
            .select("data.*", (col("data.timestamp_logger") / 1000)
                    .cast("timestamp").alias("date_time"))
            .withWatermark("date_time", "20 seconds")
            .groupBy(col("country"), w)
            .agg(count("id"))
            .select(col("count(id)").alias("total_users"))
            )


if __name__ == "__main__":
    s = Source()
    s.sc.setLogLevel("ERROR")
    df = connect_to_kafka_stream(
        topic_name="data", spark_session=s.spark)
    total_values = calculate_simple_moving_total(df)
    total_user_values = calculate_simple_current_users(df)

    query = (total_values
             .writeStream
             .option("truncate", "false")
             .outputMode("append")
             .format("console")
             .start()
             )

    query_user = (total_user_values
                  .writeStream
                  .option("truncate", "false")
                  .outputMode("append")
                  .format("console")
                  .start()
                  )

    query.awaitTermination()
    query_user.awaitTermination()
