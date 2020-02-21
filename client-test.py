#!/usr/bin/python3

from ogomclient import OperationsManagerClient

def main():
    api = OperationsManagerClient(url = "https://192.168.34.246",
                             username = "root",
                             password = "default")

    client = api.get_client()

    # a few "GETs" as example...
    print(client.system.webui_session_timeout.get())

    print(client.groups.find(id='groups-2'))

    print(client.ports.sessions.list(parent_id='ports-14'))

    print(client.ports.sessions.find(id='15910', port_id='ports-14'))

    print(client.firewall.services.find('firewall_services-1'))


main()
