#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interfaccia da selezionare per il cambio MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Nuovo MAC address nel formato 00:00:00:00:00:00")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Specifica una interfaccia, usa --help per maggiori informazioni")
    elif not options.new_mac:
        parser.error("[-] Specifica un mac address, usa --help per maggiori informazioni")
    return options


def change_mac(interface, new_mac):
    print("[+] Cambio MAC address per l'interfaccia " + interface)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
