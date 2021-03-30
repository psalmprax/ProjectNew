#!/bin/bash

spark/bin/spark-submit \
	--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.2.2 \
<<<<<<< HEAD
	./scripts/consumer/moving_average.py
=======
	./scripts/consumer/moving_total.py
>>>>>>> fc11ffd78bbf228242c3706ac834c799f83ca9a7

# spark/bin/spark-submit \
#	--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.0 \
#        --jars local:///root/sources/jars/kafka-clients-0.10.0.1.jar \
#        --driver-class-path local:///root/sources/jars/kafka-clients-0.10.0.1.jar \
<<<<<<< HEAD
#	./scripts/consumer/moving_average.py
=======
#	./scripts/consumer/moving_total.py
>>>>>>> fc11ffd78bbf228242c3706ac834c799f83ca9a7

