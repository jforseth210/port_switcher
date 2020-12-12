# Port Switcher

THIS DOESN'T WORK. DON'T USE IT.

## Intro
This is a simple python script to quickly switch between two servers using uPnP. 
Most of this work isn't my own. This script primarily uses Silas S. Brown's (UPnP router command-line control scripts)[https://ssb22.user.srcf.net/setup/upnp.html] and (Miniupnc)[http://miniupnp.tuxfamily.org/]

Basically, you configure a list of servers (I have a primary and a backup) and a list of ports. The script asks you which server you want to use, and then switches all of the ports over. 

## Getting started
Run
```pip install -r requirements.txt```

Rename ```example_config.py``` ```config.py```.

Input your port and server information. 
Run ```python port_switcher.py```

## How does it work?
I don't really know, to be completely honest. As far as I know it's editing something called "UPnP NAT-T".
The way I understand it, when an external device connects on a certain port, your router directs it to one of the devices on your network. However, it doesn't seem to affect LAN connections.
If you have questions here, Google will probably be WAY more helpful than I am. 

## Planned features
I don't know. This was created so that if one of my servers crashed, I could quickly change the port settings without editing each one in my router's somewhat painful to use GUI. It does that. 

I may try to figure out something for LAN connections. (Again, not really sure how this all works).
I may also try to add a feature where it sends a request and switches to the backup server if the request fails. (How cool would that be!) 

## Contributing
You're welcome to modify my code to suit your needs. (After all most of it isn't mine anyway). If you'd like to share your ideas: Open an issue or submit a PR. I welcome your ideas and feedback. 
