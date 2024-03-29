#!/usr/bin/env python
"""
Print the block names and counts for a layer in an Anvil chunk
Updated to support Anvil format version 1631
Section specific code moved to AnvilChunk class
"""

import os, sys
import colorsys
import argparse

# local module
try:
    import nbt
except ImportError:
    # nbt not in search path. Let's see if it can be found in the parent folder
    extrasearchpath = os.path.realpath(os.path.join(__file__,os.pardir,os.pardir))
    if not os.path.exists(os.path.join(extrasearchpath,'nbt')):
        raise
    sys.path.append(extrasearchpath)
import nbt

## block_ignore and block_colors taken from https://github.com/twoolie/NBT/blob/master/examples/map.py and modified
# List of blocks to ignore
# Uncomment all the lines to show underground structures
# TODO: move this list into a separate config file

block_ignore = [
    'air','cave_air',  # At least these ones
#    'grass_block', 'water', 'lava', 'snow', 'ice',
#    'grass', 'tall_grass', 'dead_bush',
#    'seagrass', 'tall_seagrass', 'kelp', 'kelp_plant',
#    'dandelion', 'poppy', 'oxeye_daisy', 'white_tulip',
#    'azure_bluet', 'lilac', 'rose_bush', 'peony', 'blue_orchid',
#    'lily_pad', 'sugar_cane', 'vine', 'pumpkin', 'cactus',
#    'wheat', 'potatoes', 'beetroots', 'carrots',
#    'oak_leaves', 'dark_oak_leaves', 'birch_leaves',
#    'acacia_leaves', 'spruce_leaves',
#    'oak_log', 'dark_oak_log', 'birch_log',
#    'acacia_log', 'spruce_log',
#    'brown_mushroom', 'red_mushroom',
#    'brown_mushroom_block', 'red_mushroom_block', 'mushroom_stem',
#     'grass_path', 'farmland', 'dirt',
#    'stone', 'sand', 'gravel', 'clay',
#    'sandstone', 'diorite', 'andesite', 'granite', 'obsidian',
#    'coal_ore', 'iron_ore', 'gold_ore', 'diamond_ore',
#    'redstone_ore', 'lapis_ore', 'emerald_ore',
#    'cobweb',
    ]


# Map of block colors from names
# Legacy block numeric identifiers are now hidden by Block class
# and mapped to alpha identifiers in best effort
# TODO: move this map into a separate config file

block_colors_hsl = {
    'acacia_leaves':        {'h':114, 's':64,  'l':22 },
    'acacia_log':           {'h':35,  's':93,  'l':30 },
    'air':                  {'h':0,   's':0,   'l':0  },
    'andesite':             {'h':0,   's':0,   'l':32 },
    'azure_bluet':          {'h':0,   's':0,   'l':100},
    'bedrock':              {'h':0,   's':0,   'l':10 },
    'birch_leaves':         {'h':114, 's':64,  'l':22 },
    'birch_log':            {'h':35,  's':93,  'l':30 },
    'blue_orchid':          {'h':0,   's':0,   'l':100},
    'bookshelf':            {'h':0,   's':0,   'l':100},
    'brown_mushroom':       {'h':0,   's':0,   'l':100},
    'brown_mushroom_block': {'h':0,   's':0,   'l':100},
    'cactus':               {'h':126, 's':61,  'l':20 },
    'cave_air':             {'h':0,   's':0,   'l':0  },
    'chest':                {'h':0,   's':100, 'l':50 },
    'clay':                 {'h':7,   's':62,  'l':23 },
    'coal_ore':             {'h':0,   's':0,   'l':10 },
    'cobblestone':          {'h':0,   's':0,   'l':25 },
    'cobblestone_stairs':   {'h':0,   's':0,   'l':25 },
    'crafting_table':       {'h':0,   's':0,   'l':100},
    'dandelion':            {'h':60,  's':100, 'l':60 },
    'dark_oak_leaves':      {'h':114, 's':64,  'l':22 },
    'dark_oak_log':         {'h':35,  's':93,  'l':30 },
    'dark_oak_planks':      {'h':35,  's':93,  'l':30 },
    'dead_bush':            {'h':0,   's':0,   'l':100},
    'diorite':              {'h':0,   's':0,   'l':32 },
    'dirt':                 {'h':27,  's':51,  'l':15 },
    'end_portal_frame':     {'h':0,   's':100, 'l':50 },
    'farmland':             {'h':35,  's':93,  'l':15 },
    'fire':                 {'h':55,  's':100, 'l':50 },
    'flowing_lava':         {'h':16,  's':100, 'l':48 },
    'flowing_water':        {'h':228, 's':50,  'l':23 },
    'glass_pane':           {'h':0,   's':0,   'l':100},
    'granite':              {'h':0,   's':0,   'l':32 },
    'grass':                {'h':94,  's':42,  'l':25 },
    'grass_block':          {'h':94,  's':42,  'l':32 },
    'gravel':               {'h':21,  's':18,  'l':20 },
    'ice':                  {'h':240, 's':10,  'l':95 },
    'infested_stone':       {'h':320, 's':100, 'l':50 },
    'iron_ore':             {'h':22,  's':65,  'l':61 },
    'iron_bars':            {'h':22,  's':65,  'l':61 },
    'ladder':               {'h':35,  's':93,  'l':30 },
    'lava':                 {'h':16,  's':100, 'l':48 },
    'lilac':                {'h':0,   's':0,   'l':100},
    'lily_pad':             {'h':114, 's':64,  'l':18 },
    'lit_pumpkin':          {'h':24,  's':100, 'l':45 },
    'mossy_cobblestone':    {'h':115, 's':30,  'l':50 },
    'mushroom_stem':        {'h':0,   's':0,   'l':100},
    'oak_door':             {'h':35,  's':93,  'l':30 },
    'oak_fence':            {'h':35,  's':93,  'l':30 },
    'oak_fence_gate':       {'h':35,  's':93,  'l':30 },
    'oak_leaves':           {'h':114, 's':64,  'l':22 },
    'oak_log':              {'h':35,  's':93,  'l':30 },
    'oak_planks':           {'h':35,  's':93,  'l':30 },
    'oak_pressure_plate':   {'h':35,  's':93,  'l':30 },
    'oak_stairs':           {'h':114, 's':64,  'l':22 },
    'peony':                {'h':0,   's':0,   'l':100},
    'pink_tulip':           {'h':0,   's':0,   'l':0  },
    'poppy':                {'h':0,   's':100, 'l':50 },
    'pumpkin':              {'h':24,  's':100, 'l':45 },
    'rail':                 {'h':33,  's':81,  'l':50 },
    'red_mushroom':         {'h':0,   's':50,  'l':20 },
    'red_mushroom_block':   {'h':0,   's':50,  'l':20 },
    'rose_bush':            {'h':0,   's':0,   'l':100},
    'sugar_cane':           {'h':123, 's':70,  'l':50 },
    'sand':                 {'h':53,  's':22,  'l':58 },
    'sandstone':            {'h':48,  's':31,  'l':40 },
    'seagrass':             {'h':94,  's':42,  'l':25 },
    'sign':                 {'h':114, 's':64,  'l':22 },
    'spruce_leaves':        {'h':114, 's':64,  'l':22 },
    'spruce_log':           {'h':35,  's':93,  'l':30 },
    'stone':                {'h':0,   's':0,   'l':32 },
    'stone_slab':           {'h':0,   's':0,   'l':32 },
    'tall_grass':           {'h':94,  's':42,  'l':25 },
    'tall_seagrass':        {'h':94,  's':42,  'l':25 },
    'torch':                {'h':60,  's':100, 'l':50 },
    'snow':                 {'h':240, 's':10,  'l':85 },
    'spawner':              {'h':180, 's':100, 'l':50 },
    'vine':                 {'h':114, 's':64,  'l':18 },
    'wall_torch':           {'h':60,  's':100, 'l':50 },
    'water':                {'h':228, 's':50,  'l':23 },
    'wheat':                {'h':123, 's':60,  'l':50 },
    'white_wool':           {'h':0,   's':0,   'l':100},
    }

def printHelperModules(file):
    file.write("fastRender = true;\n")
    file.write("\n")
    file.write("$fn = 8;\n")
    file.write("module minecraftCube(x,y,z,colorIn)\n")
    file.write("{\n")
    file.write("    if(fastRender == true)\n")
    file.write("    {\n")
    file.write("        color(colorIn) translate([x,y,z]) cube(1);\n")
    file.write("    }\n")
    file.write("    else\n")
    file.write("    {\n")
    file.write("        color(colorIn) translate([x,y,z])\n")
    file.write("        minkowski()\n")
    file.write("        {\n")
    file.write("            cube(0.65);\n")
    file.write("            sphere(d = 0.65);\n")
    file.write("        }\n")
    file.write("    }\n")
    file.write("}\n")

def printScadCube(x,y,z, r,g,b, type,file):
    ##  call a helper function that can do minkowski optionally
    file.write("minecraftCube(%i,%i,%i,[%.4f,%.4f,%.4f]);// %s\n"% (x, z, y, r,g,b, type))


## globals, will be modified in __main__
globalMinX = 0
globalMinZ = 0
globalMinY = 0

blocks = {}
block_colors_rgb = {}
## functionality here modified from https://github.com/twoolie/NBT/blob/master/examples/anvil_blockdata.py

def main(world_folder, chunkx, chunkz, maxY, file):

    world = nbt.world.WorldFolder(world_folder)
    if not isinstance(world, nbt.world.AnvilWorldFolder):
        print("%s is not an Anvil world" % (world_folder))
        return 65 # EX_DATAERR


    offsetX = (globalMinX - chunkx ) * 16
    offsetZ = (chunkz - globalMinZ) * 16
    file.write("// chunkX = %s, chunkZ = %s, offsetX = %s, offsetZ = %s\n"% (chunkx, chunkz, offsetX, offsetZ))

    try:
        chunk = world.get_chunk(chunkx, chunkz)
        for z in range(0, 16):
            for x in range(0, 16):
                for y in range(globalMinY,maxY+1):

                    b = chunk.get_block(x, y, z)
                    ## TODO handle more types


                    if b != None:
                        if b not in block_colors_rgb and b in block_colors_hsl:
                            # translate hsl to rgb
                            hsl = block_colors_hsl[b]
                            rgb = colorsys.hls_to_rgb(hsl['h']/360.0,hsl['l']/100.0,hsl['s']/100.0) 
                            block_colors_rgb[b] = rgb

                        if b in block_colors_rgb and b not in block_ignore:
                            rgb = block_colors_rgb[b]
                            printScadCube( offsetX-x, y-globalMinY, offsetZ+z , rgb[0], rgb[1], rgb[2], b, file)

                        if b not in blocks:
                            blocks[b] = 0
                        blocks[b] = blocks[b] + 1


    except nbt.region.InconceivedChunk:
        print("Inconceived chunk")

    return 0 # NOERR

def printBlockCounts():
    for n in blocks.keys():
        print("// %s: %i" % (n, blocks[n]))
        if n not in block_colors_rgb:
            print("  // unhandled type!!!!")

def usage(message=None, appname=None):
    if appname == None:
        appname = os.path.basename(sys.argv[0])
    print("Usage: %s WORLD_FOLDER CHUNK-X CHUNK-Z " % appname)
    if message:
        print("%s: error: %s" % (appname, message))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Convert minecraft save file into openscad cad file.')
    parser.add_argument("--saveDirectory", required=True, dest="saveDirectory")
    parser.add_argument("--minChunkX", required=True, dest="minChunkX")
    parser.add_argument("--minChunkZ", required=True, dest="minChunkZ")
    parser.add_argument("--maxChunkX", required=True, dest="maxChunkX")
    parser.add_argument("--maxChunkZ", required=True, dest="maxChunkZ")
    parser.add_argument("--minY", required=True, dest="minY")
    parser.add_argument("--maxY", required=True, dest="maxY")
    parser.add_argument("--outfile", required=True, dest="outfile")
    parseValues = parser.parse_args()

    globalMinY = min(int(parseValues.minY), int(parseValues.maxY))
    globalMinX = min(int(parseValues.minChunkX), int(parseValues.maxChunkX))
    globalMinZ = min(int(parseValues.minChunkZ), int(parseValues.maxChunkZ))
    maxChunkX = max(int(parseValues.minChunkX), int(parseValues.maxChunkX))
    maxChunkZ = max(int(parseValues.minChunkZ), int(parseValues.maxChunkZ))
    maxY = max(int(parseValues.minY), int(parseValues.maxY))

    file = open(parseValues.outfile, 'w')

    # clean path name, eliminate trailing slashes:
    world_folder = parseValues.saveDirectory
    if (not os.path.exists(world_folder)):
        usage("No such folder as "+world_folder)
        sys.exit(72) # EX_IOERR

    printHelperModules(file)
    for x in range(globalMinX, maxChunkX+1):
        for z in range(globalMinZ, maxChunkZ+1):
            main(world_folder, x, z, maxY, file)

    printBlockCounts()
    file.close()