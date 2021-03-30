# Spark Structured Streaming Project 

A Python task for analysing real-time data ingestion using Kafka and Spark Structured Streaming.

To run the producer and kafka services:
`install docker and docker-compose on the server`
and 
`docker-compose up -d --build`

To run the consumer from spark-master:

`docker exec spark-master bash scripts/start_consumer.sh`

## Producer

* API data: 

* Request: From Publisher Class.

```
{
"id": data.get("id"),
"first_name": data.get("first_name"),
"last_name": data.get("last_name"),
"email": data.get("email"),
"gender": data.get("gender"),
"ip_address": data.get("ip_address"),
"date": data.get("date"),
"country": data.get("country"),
"timestamp_logger": current_milli_time()
}
```

* Produces into Kafka topic: `data`

## Consumer

* Reads from `data`

* Uses Spark Structured Streaming

* Calculates moving total by countries and users (with window, slide and watermark)

* Sinking: Console

## Additional Services

* JMX (Java Management Extensions) Exporter for Prometheus: For Prometheus to consume Java based metrics

* Prometheus: Scraping and storing metrics in a time series db (this is set for Kafka topic monitoring)



