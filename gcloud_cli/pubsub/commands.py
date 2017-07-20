import click
from google.cloud import pubsub as ps
from .topic.commands import topics
from .subscription.commands import subscriptions


@click.group()
@click.option('--project', default='default_project', help='Google Cloud project name')
@click.pass_context
def pubsub(ctx, project):
    """
    Pubsub commands.
    """
    ctx.obj['PROJECT'] = project
    pass

pubsub.add_command(topics)
pubsub.add_command(subscriptions)
