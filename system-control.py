import pwnagotchi
# import logging
import sys

if (len(sys.argv) !=2):
    print("No valid command. Exit . . .")
    sys.exit()
    
cmd = sys.argv[1]
print ("cmd = " + cmd)
if cmd not in ('shutdown', 'restart-auto', 'restart-manu', 'reboot-auto', 'reboot-manu'):
    print("Invalid command. Exit . . .")
    sys.exit()
    
if (cmd == "shutdown"):
    print("ok")
    pwnagotchi.shutdown()
elif cmd == ("restart-auto"):
    print("ok")
    pwnagotchi.restart('auto')
elif cmd == ("restart-manu"):
    print("ok")
    pwnagotchi.restart('manual')
elif cmd == ("reboot-auto"):
    print("ok")
    pwnagotchi.reboot('auto')
elif cmd == ("reboot-manu"):
    print("ok")
    pwnagotchi.reboot('manual')
    