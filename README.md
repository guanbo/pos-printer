POS Printer for POS
===========

POS Printer for printing Receipt of POS. 

Printer base on [ESCPOS](https://code.google.com/p/python-escpos/), and write by python.

Scaner base on [Python-evdev](https://github.com/gvalkov/python-evdev).

## Quick Start

### Printer

#### Requirements

Install [python-escpos](https://code.google.com/p/python-escpos/wiki/Installation)

#### Install printer-service
```
$ git clone https://github.com/guanbo/pos_printer
$ cd pos_printer
$ sudo ./pos-printer.py &
$ curl -X POST -d "Hello Printer" http://youIPAddress:8000
```
### Bonjour

```shell
$ sudo cp extensivepromini.service /etc/avahi/services/
$ sudo /etc/init.d/avahi-daemon restart
```

### Scaner (Deprecated)

#### Requirements
```
$ sudo apt-get install python-dev
# sudo apt-get install linux-headers-$(uname -r)
$ wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python
```

#### Install python-evdev
```
$ git clone https://github.com/gvalkov/python-evdev.git
$ cd python-evdev
$ sudo python setup.py install
```

## Troubleshoot
- How to access server by hostname`.local`  

```
$ sudo apt-get update
$ sudo apt-get install avahi-daemon
$ sudo vi /etc/hostname
# change your hostname and save
```

- Can't apt-get install `pyserial`

```
$ sudo apt-get install python-serial
```

## Update

update firmware and reboot

### automatic update
#### cron
call update script on schedule

    export VISUAL=vi
    crontab -e 
    
enter following code into cron file

	@daily /home/pi/deploy/pos-printer/update-auto.sh 2>&1 >> /home/pi/deploy/pos-update.log
	@yearly rm /home/pi/deploy/pos-update.log	

### manual update
```
$ cd path/to/pos-printer
$ sh update.sh
```
### web update
```
$ curl -v -X POST http://exprominisrv.local:8000/update
```

## Backup

dump all img to disk for backup

### dump image
	$ diskutil umount /dev/disk1s1
	$ sudo dd if=/dev/rdisk1 of=/tmp/rpi20140301.img bs=1m
	$ diskutil umount /dev/disk1s1
  
### restore image
	$ diskutil umount /dev/disk1s1
	$ sudo dd of=/dev/rdisk1 if=/tmp/rpi20140301.img bs=1m
	$ diskutil umount /dev/disk1s1
  
