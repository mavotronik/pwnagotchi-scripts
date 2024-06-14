sudo bluetoothctl -- remove <your mac>
sleep 2
sudo timeout -s 2 10 sudo bluetoothctl -- scan on
sleep 1
sudo bluetoothctl -- pair <your mac>

exit 0



