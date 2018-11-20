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
 base_width = 160;
 base_length = 180;
 base_height = 5;
 rounded_corner_radius = 5;
 
 // SPROCKET VARIABLES
 sprocket_width = 10;
 sprocket_brace_thickness = 4;
 sprocket_brace_distance_from_center = base_width/2 - 0.5*sprocket_brace_thickness;
 sprocket_brace_height = 25 + base_height;
 
 // MOTOR PROTOTYPE
 motor_width = 32;
 motor_height = 25 + base_height;
 motor_length = 78.5;
 motor_distance_from_center = sprocket_brace_distance_from_center-sprocket_brace_thickness-0.5*motor_width-0.5*rounded_corner_radius;
 motor_y_shift = base_length/2 - motor_length/2 + rounded_corner_radius;
 
 // RASPBERRY PI PROTOTYPE
 raspberry_pi_height = 17;
 
 
 //long threaded bolt is used as axle from body
 
 module raspberry_pi() {
     square([85.6, 56.5], center = true);
 }
 
 module motor_case() {
     square([motor_width,motor_length], center=true);
 }
 
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

module left_and_right_motor_placeholders() {
    translate([motor_distance_from_center,0,0])
        motor_case();
    translate([-motor_distance_from_center,0,0])
        motor_case();
}
 
linear_extrude(5)
    base(rounded=true);

linear_extrude(sprocket_brace_height)
    left_and_right_sprocket_braces();

#linear_extrude(motor_height) {
    translate([0,motor_y_shift,0])
        left_and_right_motor_placeholders();
}

translate([0,0,-raspberry_pi_height])
    #linear_extrude(raspberry_pi_height) {
        translate([0,-base_length/4,0])
        raspberry_pi();
    }

//sprocket();









