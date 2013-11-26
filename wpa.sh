#!/bin/sh

# Description: Setup WPA of Wifi

echo "Setup WPA ..."

# check for root user 
if [ `whoami` != "root" ] ; then
	echo "You must run this script as root. Sorry!"
	exit 1
fi

#check for paramerter
if [ ! "$1" ] || [ ! "$2" ] ; then
	echo "Usage: wpa.sh <ssid> <passphrase>"
	exit 1
fi

echo "Generate WPA"
WPA_SUPPLICANT_CONF_FILE="/etc/wpa_supplicant/wpa_supplicant.conf"
echo "ctrl_interface=DIR=/var/run/wpa_supplicant" > $WPA_SUPPLICANT_CONF_FILE
echo "GROUP=netdev" >> $WPA_SUPPLICANT_CONF_FILE
echo "update_config=1" >> $WPA_SUPPLICANT_CONF_FILE

wpa_passphrase $1 $2 | tee -a $WPA_SUPPLICANT_CONF_FILE

echo "Set SSID: $1 Passphrase: $2 Done."