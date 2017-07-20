import click
from google.cloud import pubsub as ps


@click.group()
@click.pass_context
def subscriptions(ctx):
    """Console script for gcloud_cli."""
    pass


@subscriptions.command()
@click.option('--topic', default=None)
@click.pass_context
def list(ctx, topic):
    """
    List subscriptions.
    """
    client = ps.Client(ctx.obj['PROJECT'])
    subscriptions = client.topic(topic).list_subscriptions() if topic else client.list_subscriptions()
    for s in subscriptions:
        click.echo(s.name)


@subscriptions.command()
@click.argument('name')
@click.option('--topic', prompt=True)
@click.pass_context
def create(ctx, topic, name):
    """
    Create new subscription.
    """
    client = ps.Client(ctx.obj['PROJECT'])
    t = client.topic(topic)
    subscription = t.subscription(name)
    subscription.create(client)
    click.echo('Subscription {} created.'.format(subscription.name))


@subscriptions.command()
@click.argument('name')
@click.option('--topic', default=None)
@click.pass_context
def delete(ctx, topic, name):
    """
    Delete subscription.
    """
    client = ps.Client(ctx.obj['PROJECT'])
    subscriptions = client.topic(topic).list_subscriptions() if topic else client.list_subscriptions()
    for s in subscriptions:
        if s.name == name:
            s.delete()  # API request
            click.echo('Subscription {} deleted'.format(s.name))

