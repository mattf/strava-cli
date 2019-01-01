import click

from commands import login, logout, get_activities, get_activity, get_profile, get_stats, set_config


@click.group()
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(get_activities)
cli.add_command(get_activity)
cli.add_command(get_profile)
cli.add_command(get_stats)
cli.add_command(set_config)

if __name__ == '__main__':
    cli()
