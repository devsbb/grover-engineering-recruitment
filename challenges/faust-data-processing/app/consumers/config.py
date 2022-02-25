from prettyconf import config

DEBUG = config("DEBUG", default=True, cast=config.boolean)
KAFKA_BROKER_URL = config("KAFKA_BROKER_URL")
KAFKA_CONSUMER_GROUP = config("KAFKA_CONSUMER_GROUP", default="faust-consumers")
KAFKA_BOOTSTRAP_SERVERS = [su.replace("kafka://", "") for su in KAFKA_BROKER_URL.split(";")]
