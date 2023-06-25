import time
import udp_api
import typer
from yaspin import yaspin
import inquirer

app = typer.Typer()


def main(pseudo: str, port: int):
    udp= udp_api.UDPClient(pseudo, port)


@yaspin(text="Waiting for a peer...")
def scan():
    time.sleep(5)
    print("OOF")


if __name__ == "__main__":
    typer.run(main)


