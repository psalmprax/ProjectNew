from pyspark.sql.types import (
    StructType, StringType, LongType)


data_model_schema = (StructType()
                     .add("id", StringType())
                     .add("first_name", StringType())
                     .add("last_name", StringType())
                     .add("email", StringType())
                     .add("gender", StringType())
                     .add("ip_address", StringType())
                     .add("date", StringType())
                     .add("country", StringType())
                     .add("user", StringType())
                     .add("timestamp_logger", LongType()))
