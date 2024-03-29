# mc2scad
This script uses [NBT](https://github.com/twoolie/NBT) to parse a chunk and turn the blocks into an openscad CAD file.


## How to use:
  1. Follow the instructions to [NBT](https://github.com/twoolie/NBT) to install it
  2. locate your minecraft file you wish to process, [guide](https://help.mojang.com/customer/portal/articles/1480874-where-are-minecraft-files-stored-)
  3.  Then inside that directory locate your save files and the world you want to process
  4.  Then call the script passing in your save file location and the chunk location you want to process, redirecting the output to a .scad file.  Example:

    ./mc2scad.py --saveDirectory="~/Library/Application Support/minecraft/saves/flatWorld" --minChunkX=-15 --minChunkZ=-14  --maxChunkX=-14  --maxChunkZ=-13 --minY=60 --maxY=80 --outfile=scad/ex_flat.scad

  5.  Then open the scad file with openscad, view and print.

  ![sample image from openscad](https://github.com/t-foster/mc2scad/blob/master/images/ScreenShotSample.png)
  ![original area from minecraft](https://github.com/t-foster/mc2scad/blob/master/images/MinecraftView.png)

  6.  change the fastRender parameter from true to false to get rounded blocks

  TODO:

    * handle more block types, including half blocks, doors, windows, stairs, etc
    * handle "Inconceived chunk" errors
    * example of how to get map coordinate from f3 view
    * open source licensing