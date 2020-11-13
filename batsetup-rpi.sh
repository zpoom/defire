iw wlan0 set type ibss

#new
#ifconfig wlan0 mtu 1532
#iwconfig wlan0 channel 3

ip link set wlan0 up

iw wlan0 ibss join defire 2432
# replace <adhocnetworkname> with a ssid for example: rpiadhoc
# replace <password> with a password of length 5 or 13 (WEP) for example: abcdefghijklm

modprobe batman-adv
batctl if add wlan0

ip link set up dev wlan0
ip link set up dev bat0

#new
#ifconfig bat0 172.27.0.10/16

batctl gw_mode client # optional if there is a gateway for internet in your network

sleep 10
alfred -i bat0 -m -p 1 &
sleep 10
batadv-vis -i bat0 -s &
