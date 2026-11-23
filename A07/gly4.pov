
#include "gly.pov"

// Camera
camera {
    location <0, 0, -25>
    look_at <0, 0, 0>
    right x*image_width/image_height
}

// Lighting
light_source {
    <0, 10, -20>
    color rgb <1, 1, 1>
}

// Background
background {
    color rgb <1, 1, 1>
}

// Four glycine molecules at the vertices of a square

#declare Glycine = object {
    mol_0
    translate mol_0_center
}

// Top left
object { Glycine translate <-5, 5, 0> }

// Top right
object { Glycine translate <5, 5, 0> }

// Bottom left
object { Glycine translate <-5, -5, 0> }

// Bottom right
object { Glycine translate <5, -5, 0> }
