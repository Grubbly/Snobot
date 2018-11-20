/*
 * snobot_full.scad
 * Tristan Van Cise
 * CS 680 - Project 2
 * 11/19/2018
 *
 * Description:
 *  Snobot full component model
 */
 
 // BASE VARIABLES
 base_width = 130;
 base_length = 180;
 rounded_corner_radius = 7;
 
 // SPROCKET VARIABLES
 sprocket_width = 10;
 sprocket_brace_thickness = 10;
 sprocket_brace_distance_from_center = base_width/2 - 0.5*sprocket_brace_thickness;
 
 //long threaded bolt is used as axle from body
 
 module sprocket_base_import() {
     color("Lime", 1.0)
        import("..\\3rd_Party\\sprocket.stl", convexity = 10, center = true);
 }

module sprocket() {
   rotate([0,90,0]) {
       sprocket_base_import();
   }
} 
 
 module base(rounded=true) {
     if(rounded) {
        minkowski() {
            square([base_width, base_length], center=true);
            circle(r=rounded_corner_radius);
        }
     } else {
        square([base_width, base_length], center=true);
     }
}

module sprocket_brace() {
    minkowski() {
        square([sprocket_brace_thickness, base_length], center = true);
        circle(r=rounded_corner_radius);
    }
}

module left_and_right_sprocket_braces() {
    translate([sprocket_brace_distance_from_center,0,0])
        #sprocket_brace();
    
    translate([-sprocket_brace_distance_from_center,0,0])
        #sprocket_brace();
}
 
base(rounded=true);

left_and_right_sprocket_braces();

sprocket();









