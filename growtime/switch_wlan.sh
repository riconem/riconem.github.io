#!/bin/bash

config=$1

sudo cp /etc/wpa_supplicant/wpa_supplicant_$1.conf /etc/wpa_supplicant/wpa_supplicant.conf

sudo wpa_cli -i wlan0 reconfigure
