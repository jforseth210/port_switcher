import miniupnpc
from sensitivedata import SERVER_NAMES, PORTS
u = miniupnpc.UPnP()
u.discoverdelay=200;u.discover();u.selectigd()
print("This script only affects WAN ports. Local devices will not be affected.")
p=1;i=0
while p:
    p = u.getgenericportmapping(i) ; i+=1
    if p:
        port,protocol,(toAddr,toPort),desc,x,y,z = p
        if port == 443:
            server=SERVER_NAMES[toAddr]
            print('Currently running on {}: {}'.format(server[0],server[1]))
secs = u.statusinfo()[1]
mins,secs = int(secs/60),secs%60
hrs,mins = int(mins/60),mins%60
days,hrs = int(hrs/24),hrs%24
print("Your external ip is {}".format(u.externalipaddress()))
print("Your router has been up for %d days %d:%d:%d" % (days,hrs,mins,secs))
for idx, server in enumerate(SERVER_NAMES.values()):      
    print('[{}] {} ({})'.format(idx,server[1],server[0]))
server=input('Which server would you like to switch to? [0-{}]:'.format(len(SERVER_NAMES)-1))
for port in PORTS.keys():
    print(port)
    try:
        u.deleteportmapping(port,'TCP')
    except:
        print('No such entry in array')
    u.addportmapping(port,'TCP',list(SERVER_NAMES.keys())[int(server)],port,'upnp-add-port '+str(port),'')

p=1;i=0
while p:
  p = u.getgenericportmapping(i) ; i+=1
  if p:
    port,protocol,(toAddr,toPort),desc,x,y,z = p
    if toAddr == '192.168.1.29':
      print(protocol+":"+str(port)+" -> "+toAddr+":"+str(toPort)+"\t"+desc)
p=1;i=0
while p:
    p = u.getgenericportmapping(i) ; i+=1
    if p:
        port,protocol,(toAddr,toPort),desc,x,y,z = p
        if port == 443:
            server=SERVER_NAMES[toAddr]
            print('Currently running on {}: {}'.format(server[0],server[1]))