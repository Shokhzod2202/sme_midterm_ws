import click
import subprocess

@click.command()
@click.option('--fleet-size', type=int, help='Specify the fleet size', required=True)
def allocate_and_route(fleet_size):
    subprocess.run(["python3", "fleet_management_client_cli.py", f"--fleet_size={fleet_size}"])

if __name__ == '__main__':
    allocate_and_route()
