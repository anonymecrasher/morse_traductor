import time
import udp_api
from yaspin import yaspin
import click


@click.command()
@click.option("--pseudo", prompt="Your name", help="The name that peers will see")
@click.option("--port", default=2236, help="Port to communicate with peers")
@click.option("--receiver", default="on", help="[on] you are reachable \n [off] you are unreachable")
@click.option("--discoverable", default="on", help="[on]  You respond to ping\n [off] you don't respond")
def main(pseudo: str, port: int):



@yaspin(text="Waiting for a peer...")
def scan():
    time.sleep(5)
    print("OOF")


if __name__ == "__main__":
    main()


