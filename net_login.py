from netmiko import ConnectHandler

device = ConnectHandler(device_type='ubiquiti_edge', ip ='204.191.123.84', username ='CBMUBNT', password ='CBMCBM@dm1N')
output  = device.send_command("show version")
print(output)
device.disconnect()
