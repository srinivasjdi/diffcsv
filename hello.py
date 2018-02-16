import click
"""
@click.group()
def cli():
	click.echo("hello group !")
"""

@click.command()
@click.option('--count',default=1,help="number of times to print greetings")
@click.argument('name')
def cli(name,count):
	for i in range(count):
		click.echo("hello  %s!"%name)

"""
@cli.command()
def two():
	click.echo("hello two !")
"""