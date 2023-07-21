import time
import udp_api
from yaspin import yaspin
import click
import threading
import inquirer


@click.command()
@click.option("--pseudo", prompt="Your name", help="The name that peers will see")
@click.option("--port", default=2236, help="Port to communicate with peers")
@click.option("--reachable", default="on", help="[on] you are reachable \n [off] you are unreachable")
@click.option("--discoverable", default="on",
              help="[on]  You respond to ping\n [off] you don't respond \n (--reachable must be [on])")
def main(pseudo: str, port: int, reachable: str, discoverable: str):
    assert pseudo != ""
    assert port != ""
    assert reachable != ""
    assert discoverable != ""

    client = udp_api.UDPClient(pseudo, port, reachable, discoverable)
    if reachable == "on":
        receiver = threading.Thread(target=client.receiver)
        print(f"✅ Your IP address is {client.client_ip[0]} \n You are listening on {port}")
    choice = inquirer.list_input("What do you want to do ?", choices=["Scan network", "Send message to a peer", "Send message to an unknown ip", "Ping an IP", "Wait for some messages"])

    match choice:
        case "Scan network":
            with yaspin(text="Waiting for a peer", color="yellow"):
                client.scanner()
        case "Send message to a peer":
            pass
        case "Send message to an unknown ip":
            pass
        case "Ping an IP":
            pass
        case  "Wait for some messages":
            pass

    time.sleep(5)
    print("HEY")




if __name__ == "__main__" :
    main()