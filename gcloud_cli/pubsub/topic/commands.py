import click
from google.cloud import pubsub as ps


@click.group()
@click.pass_context
def topics(ctx):
    """Console script for gcloud_cli."""
    pass


@topics.command()
@click.pass_context
def list(ctx):
    """
    List topics.
    """
    client = ps.Client(ctx.obj['PROJECT'])
    for t in client.list_topics():
        click.echo(t.name)


@topics.command()
@click.argument('name')
@click.pass_context
def create(ctx, name):
    """
    Create new topic.
    """
    # Instantiates a project
    pubsub_client = ps.Client(ctx.obj['PROJECT'])

    # Prepares the new topic
    topic = pubsub_client.topic(name)
    topic.create()
    click.echo('Topic {} created.'.format(topic.name))



@topics.command()
@click.argument('name')
@click.pass_context
def delete(ctx, name):
    """
    Delete topic.
    """
    client = ps.Client(ctx.obj['PROJECT'])
    topic = client.topic(name)
    assert topic.exists(), 'Topic {} does not exist'.format(name)       # API request
    topic.delete()
    assert not topic.exists(), 'Topic {} was not deleted!'.format(name)   # API request
    click.echo('Topic {} deleted'.format(name))
