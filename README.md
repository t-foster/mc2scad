# mc2scad
This script uses [NBT](https://github.com/twoolie/NBT) to parse a chunk and turn the blocks into an openscad CAD file.


## How to use:
  1. Follow the instructions to [NBT](https://github.com/twoolie/NBT) to install it
  2. locate your minecraft file you wish to process, [guide](https://help.mojang.com/customer/portal/articles/1480874-where-are-minecraft-files-stored-)
  3.  Then inside that directory locate your save files and the world you want to process
  4.  Then call the script passing in your save file location and the chunk location you want to process, redirecting the output to a .scad file

    ./script.py "/Users/troyfoster/Library/Application Support/minecraft/saves/First World" 0 0 > ex.scad

  5.  Then open the scad file with openscad, view and print.

  [[https://github.com/t-foster/mc2scad/blob/master/Screen%20Shot%202019-04-05%20at%209.49.08%20PM.png|sample image from openscad]]