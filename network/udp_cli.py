import time
import udp_api
import typer
from yaspin import yaspin
from inquirer import Text, List

app = typer.Typer()


def main(pseudo: str, port: int):
    udp = udp_api.UDPClient(pseudo, port)
    choice = List(name="choice", message="What do you want to do ?", choices=["scan", "wait", "send"], default="scan")
    if choice == "scan":
        print("Good choice")


@yaspin(text="Waiting for a peer...")
def scan():
    time.sleep(5)
    print("OOF")


if __name__ == "__main__":
    typer.run(main)


