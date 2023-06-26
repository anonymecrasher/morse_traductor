import time
import udp_api
from yaspin import yaspin
import click


@click.command()
@click.option("--pseudo", default="guest", help="The name that peers will see")
@click.option("--port", default=2236, help="Port to communicate with peers")
def main(pseudo: str, port: int):



@yaspin(text="Waiting for a peer...")
def scan():
    time.sleep(5)
    print("OOF")


if __name__ == "__main__":
    pass


