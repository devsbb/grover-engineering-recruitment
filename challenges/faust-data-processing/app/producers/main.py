import asyncio
import datetime
import json
import logging
from random import randint
import time
import uuid

from aiokafka import AIOKafkaProducer
import faker
from prettyconf import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

KAFKA_BOOTSTRAP_SERVERS = config("KAFKA_BOOTSTRAP_SERVERS", default="localhost:9092")
TOPIC_NAME = "users"


def prepare_message(event):
    return json.dumps(event, default=str).encode()


async def send_many(topic_name, servers, data):
    producer = AIOKafkaProducer(bootstrap_servers=servers)
    await producer.start()

    senders = [
        sender(topic_name, prepare_message(event), producer)
        for event in data
    ]
    logger.info("Preparation completed")

    try:
        await asyncio.gather(*senders)
    finally:
        await producer.stop()


async def sender(topic_name, payload, producer):
    try:
        await producer.send_and_wait(topic_name, value=payload)
        logger.info(f"Message sent to {topic_name}")
        logger.debug(payload)
    except Exception as error:
        logger.error(error)


def get_samples(size: int) -> list:
    def _get_sample():
        base = {'user_id': str(uuid.uuid4()),
                'created_at': datetime.datetime.utcnow()
                }
        return {**base, **faker.Faker().profile()}

    return [_get_sample() for _ in range(size)]


if __name__ == "__main__":
    while True:
        sample_data = get_samples(randint(5, 50))
        asyncio.run(send_many(TOPIC_NAME, KAFKA_BOOTSTRAP_SERVERS, sample_data))
        time.sleep(randint(10, 60))
