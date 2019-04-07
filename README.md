# mc2scad
This script uses [NBT](https://github.com/twoolie/NBT) to parse a chunk and turn the blocks into an openscad CAD file.


## How to use:
  1. Follow the instructions to [NBT](https://github.com/twoolie/NBT) to install it
  2. locate your minecraft file you wish to process, [guide](https://help.mojang.com/customer/portal/articles/1480874-where-are-minecraft-files-stored-)
  3.  Then inside that directory locate your save files and the world you want to process
  4.  Then call the script passing in your save file location and the chunk location you want to process, redirecting the output to a .scad file.  Example:

    ./script.py "\~/Library/Application Support/minecraft/saves/First World" 0 0 > ex.scad

  5.  Then open the scad file with openscad, view and print.

  ![sample image from openscad](https://github.com/t-foster/mc2scad/blob/master/ScreenShotSample.png)

  TODO:

    * change input parameters to handle multiple chunks 
    * change input to handle y axis ranges
    * handle more block types, including half blocks, doors, windows, steps, etc
    * handle "Inconceived chunk" errors
    * input map coordinate from f3 view