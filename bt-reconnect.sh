bluetoothctl -- remove <your mac>
sleep 2
bluetoothctl -- scan on
sleep 5
bluetoothctl -- pair <your mac>
sleep 10
bluetoothctl -- scan off

exit 0



