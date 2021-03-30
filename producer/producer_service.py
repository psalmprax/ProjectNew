
import os
import time
from pathlib import Path
from json import dumps

from confluent_kafka import Producer

from utils import (
    set_logger, config_reader, acked)
from producerAPI import Publisher


SOURCE_URL = "https://storage.googleapis.com/datascience-public/data-eng-challenge/MOCK_DATA.json"
LOGGER = set_logger("producer_logger")
PARENT_PATH = os.fspath(Path(__file__).parents[1])
CONFIG_PATH = os.path.join(
    PARENT_PATH,
    "configurations",
    "settings.ini")
KAFKA_CONFIG_DICT = config_reader(
    CONFIG_PATH, "kafka")
TOPIC = config_reader(
    CONFIG_PATH, "app.settings")["topic_raw"]


def produce_list_of_dict_into_kafka(list_of_dict):
    publisher = Producer(KAFKA_CONFIG_DICT)
    for line in list_of_dict:
        coin_name = line["id"]
        try:
            print(line)
            publisher.produce(
                topic=TOPIC,
                value=dumps(line).encode("utf-8"),
                callback=acked)
            # time.sleep(5)
            publisher.poll(1)

        except Exception as e:
            LOGGER.info(
                f"There is a problem with the {coin_name}\n"
                f"The problem is: {e}!")


if __name__ == "__main__":
    producer = Publisher()
    
    while True:
        dataset, status = producer.get_json_api(SOURCE_URL)
        data_with_model = producer.get_all_data_with_model(dataset)
        produce_list_of_dict_into_kafka(data_with_model)
        LOGGER.info(f"Produced into Kafka topic: {TOPIC}.")
        LOGGER.info(f"Waiting for the next round...")
        time.sleep(15)


