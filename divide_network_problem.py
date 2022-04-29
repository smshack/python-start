from string import Template
from math import log

t = Template("""
네트워크 $n: $header.$network_adr
서브넷마스크: $subnet
브로드캐스트: $broadcast
IP 주소 범위: $header.$network_adr ~ $header.$broadcast
유효 호스트 IP 주소 범위: $header.$start_adr ~ $header.$end_adr
""")

network_adr = input("Network address? >").split('.')
print(network_adr,'network_adr')
header = '.'.join(network_adr[:3])
print(header,'header')

network_adr = int(network_adr[-1])
print(network_adr,'network_adr')

host = int(input("How many hosts? >"))

divide_by = 2
while divide_by < host:
    divide_by *= 2

subnet = 32 - int(log(divide_by, 2))
broadcast = divide_by - 1

for n in range(1, 256 // divide_by + 1):
    print(t.substitute(
        n=n, header=header,
        network_adr=network_adr,
        subnet=subnet,
        broadcast=broadcast,
        start_adr=network_adr+1,
        end_adr=broadcast-1
    ))
    network_adr += divide_by
    broadcast += divide_by