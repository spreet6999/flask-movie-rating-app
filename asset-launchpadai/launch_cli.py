import click
from index import main
from app import app_port, app_prefix
import requests
import subprocess


@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--local', is_flag=True, help="Only run locally and do not forward the port")
@click.argument('action')
def cli(verbose, action, local):
    """This is to start or stop a launch_AI app. You must indicate start or stop"""
    if verbose:
        click.echo("We are in the verbose mode.")

    if action.lower() == 'start':
        if local:
            main()
        else:
            p = subprocess.run("./run.sh")
            print(p)
            main()
        if verbose:
            click.echo("start the app")
    elif action.lower() == "stop":
        # print("http://localhost:" + str(app_port) + "/shutdown/")
        c = requests.get("http://localhost:" + str(app_port) + app_prefix + "shutdown")
        if verbose:
            print(c)
            click.echo('stop the app')
    else:
        click.echo('you must provide a valid argument')
