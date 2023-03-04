from netmiko import ConnectHandler

devices_ready = open(r"devices.txt")
devices = devices_ready.read().splitlines()

commands_ready = open(r"commands.txt")
commands = commands_ready.read().splitlines()

for i in devices:
    device = {
        "device_type" : "cisco_xr",
        "ip" : i,
        "username" : "root",
        "password" : "root@123",
        "port" : 22
    }

    connectdevice = ConnectHandler(**device)
    for j in commands:
        fetch = connectdevice.send_command(j,read_timeout=300)
        print(fetch)
    connectdevice.disconnect()
