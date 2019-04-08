fastRender = true;

$fn = 8;
module minecraftCube(x,y,z,colorIn)
{
    if(fastRender == true)
    {
        color(colorIn) translate([x,y,z]) cube(1);
    }
    else
    {
        color(colorIn) translate([x,y,z])
        minkowski()
        {
            cube(0.65);
            sphere(d = 0.65);
        }
    }
}
// chunkX = 12, chunkZ = 5, offsetX = 0, offsetZ = 0
minecraftCube(-14,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,13,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,14,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,14,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,14,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,15,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,15,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,15,2,[0.3200,0.3200,0.3200]);// granite
// chunkX = 12, chunkZ = 6, offsetX = 0, offsetZ = 16
minecraftCube(-14,16,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,16,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,16,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,17,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,17,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,17,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,18,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,18,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,18,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,19,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,19,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,19,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,20,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,20,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,20,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,21,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-14,21,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-15,21,2,[0.3200,0.3200,0.3200]);// granite
// chunkX = 13, chunkZ = 5, offsetX = -16, offsetZ = 0
minecraftCube(-16,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,13,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,13,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,13,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,13,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,13,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,13,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,13,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,13,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,13,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,13,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,14,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,14,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,14,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,14,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,14,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,14,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,15,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,15,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,15,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,15,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,15,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,15,1,[0.3200,0.3200,0.3200]);// granite
// chunkX = 13, chunkZ = 6, offsetX = -16, offsetZ = 16
minecraftCube(-16,16,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,16,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,16,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,16,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,16,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,16,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,17,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,17,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,17,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,17,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,17,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,17,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,18,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,18,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,18,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,18,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,18,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,18,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,19,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,19,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,19,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,19,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,19,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,19,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,20,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,20,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,20,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,20,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,20,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,20,1,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-16,21,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-17,21,4,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-18,21,3,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-19,21,2,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,21,0,[0.3200,0.3200,0.3200]);// granite
minecraftCube(-20,21,1,[0.3200,0.3200,0.3200]);// granite
