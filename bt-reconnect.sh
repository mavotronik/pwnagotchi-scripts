### sh bt-reconnect.sh <your_mac>

MAC=$1

sudo bluetoothctl -- remove $MAC
sleep 2
sudo timeout -s 2 10 sudo bluetoothctl -- scan on
sleep 1
sudo bluetoothctl -- pair $MAC

exit 0
