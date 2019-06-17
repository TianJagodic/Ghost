# Ghost

Ghost is a linux python program made for dissapering like a ghost. It Changes your current IPv4 and your MAC address and the name of the machine your are currently using. 

## Changing the computer name
Ghost auto generates a random string of numbers and sets it as the name of the computer this looks something like this `6011254269962487` this will show up as the name of the computer in any situation including the terminal.

## Changing the MAC address 
Ghost will for now only spoof the MAC and change it for the wireless adapter only. It should look something like this `23:21:83:10:43:29` and yes only numbers in order to check if there is an actual change.

## Changing the IP address
Ghost will first scan the network establish the mask and pick one that is not taken then assign it to your machine.