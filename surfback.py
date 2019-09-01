import sys
import tempfile
import time

from pymol import cmd
def surfback(width,height,color="gray",showcartoon=True,dname=""):
    #if (cmd.get("bg_image_filename")==None):
    cmd.set("bg_image_filename",None)
    cmd.hide("")
    cmd.set("fog", 0)
    cmd.set("reflect", 0)
    cmd.set("ambient",1)
    cmd.set("ray_trace_mode", 0)
    cmd.show("surface")
    cmd.set("surface_color",color)
    cmd.set("spec_reflect",0)
    cmd.ray(width,height)
    # I want below to work with tmpdir but, it fails. So this script makes unwanted tmpfile to dir named as dname
    cmd.png(dname+"surf.png")
    cmd.do("ls " + dname)
    cmd.do("ls " + dname+"surf.png")
    #cmd.load_png(dname+"surf.png")
    time.sleep(0.01)
    cmd.set("bg_image_filename",dname+"surf.png")
    cmd.set("bg_image_mode",0)
    if (showcartoon):
        cmd.hide("")
        cmd.show("cartoon")
        cmd.color("white")
        cmd.set("ray_trace_mode", 3)
        cmd.set("ambient", 1)
        cmd.set("reflect",0)
        cmd.set("valence", 0)
        cmd.set("spec_reflect",0)
        cmd.set("ray_trace_color", "gray0")
    #cmd.ray(n,n)
    #cmd.png("/
    print("Ray your image in the same aspect ratio as you specified in surfback")
pymol.cmd.extend("surfback", surfback)
cmd.auto_arg[2]['surfback'] = cmd.auto_arg[0]['bg_color']
