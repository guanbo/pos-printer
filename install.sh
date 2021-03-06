#!/bin/sh

# Description: Install POS Printer service

echo "Install POS Printer"
echo "..."

# check for root user 
if [ `whoami` != "root" ] ; then
	echo "You must run this script as root. Sorry!"
	exit 1
fi

# install program 
INSTALL_DIR="/usr/local/bin/pos-printer"
mkdir -p $INSTALL_DIR
cp *.py *.html $INSTALL_DIR
cp -R utils $INSTALL_DIR/
chmod -R 755 $INSTALL_DIR
# cp update.sh $INSTALL_DIR
# chmod 755 $INSTALL_DIR/*.sh
cp adapter-printers /etc/

# install startup script
INIT_SCRIPT_FILE="pos-printer"
INIT_SCRIPT="/etc/init.d/"$INIT_SCRIPT_FILE
cp init.pos-printer.sh $INIT_SCRIPT
chmod 755 $INIT_SCRIPT

update-rc.d $INIT_SCRIPT_FILE defaults

echo "Install Done"