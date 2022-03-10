import logging

from faust.app import App

from consumers import config


logger = logging.getLogger(__name__)

app = App(
    config.KAFKA_CONSUMER_GROUP,
    broker=config.KAFKA_BROKER_URL,
    debug=config.DEBUG,
)

users_topic = app.topic('users')

# TODO add your agent/consumer here
