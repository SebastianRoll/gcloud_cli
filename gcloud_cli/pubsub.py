# Imports the Google Cloud client library
from google.cloud import pubsub

def create_topic(client, topic_name):
    # Instantiates a client
    pubsub_client = pubsub.Client(client)

    # Prepares the new topic
    topic = pubsub_client.topic(topic_name)
    topic.create()
    """subscription = topic.subscription("thing-search-local")
    subscription.create(pubsub_client)
    # The name for the new topic
    topic_name = 'thingstate-local'
    # Prepares the new topic
    topic = pubsub_client.topic(topic_name)
    topic.create()
    subscription = topic.subscription("thing-search-state-dev-local")
    subscription.create(pubsub_client)"""
    #topic.create()



    print('Topic {} created.'.format(topic.name))
