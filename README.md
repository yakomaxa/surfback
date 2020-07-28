# surfback
A pymol script to use flat surface representation as background image

# Usage
You have to load this  as usual 

```run surfback.py```

# Sample PyMOL command

load 1mbn
surfback 800,800, blue # make a blue surface background image of 800x800
ray 800, 800 # ray the model in same size as specified above
png model_with_surfacebackground.png


