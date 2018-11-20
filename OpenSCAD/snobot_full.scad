/*
 * snobot_full.scad
 * Tristan Van Cise
 * CS 680 - Project 2
 * 11/19/2018
 *
 * Description:
 *  Snobot full component model
 */
 
 // VISIBILITY VARIABLES
 electronics_on = false;
 sprockets_on = false;
 
 // BASE VARIABLES
 base_width = 160;
 base_length = 180;
 base_height = 5;
 rounded_corner_radius = 5;
 
 // SPROCKET VARIABLES
 sprocket_width = 10;
 sprocket_brace_thickness = 4;
 sprocket_brace_distance_from_center = base_width/2 - 0.5*sprocket_brace_thickness;
 sprocket_distance_from_center = sprocket_brace_distance_from_center + 2*sprocket_width;
 sprocket_brace_height = 25 + base_height;
 
 // MOTOR PROTOTYPE
 motor_width = 32;
 motor_height = 25 + base_height;
 motor_length = 78.5;
 motor_distance_from_center = sprocket_brace_distance_from_center-sprocket_brace_thickness-0.5*motor_width-0.5*rounded_corner_radius;
 motor_y_shift = base_length/2 - motor_length/2 + rounded_corner_radius;
 
 // RASPBERRY PI PROTOTYPE
 raspberry_pi_height = 17;
 
 // L298N PROTOTYPE
 L298N_height = 26;
 L298N_side_length = 43;
 
 // BRIDGE 
 // -------
 
 // BREADBOARD PROTOTYPE
 breadboard_width = 55;
 breadboard_length = 85;
 
 // M3 BOLTS
 m3_radius = 1.5;
 m3_diameter = 2*m3_radius;
 m3_y_shift = base_width/2 + 2*rounded_corner_radius;
 m3_side_shift = base_width/2;
 
 //long threaded bolt is used as axle from body

 module snobot_text() {
     
 }

 module m3_bolt(height=5) {
     cylinder(r=m3_radius,h=height,center=true,$fn=100);
 }
 
 module side_base_m3_bolts(height) {
    translate([m3_side_shift,0,0]) {
        m3_bolt(height=height);
    
        translate([0,m3_y_shift,0])
            m3_bolt(height=height);
    
        translate([0,-m3_y_shift,0])
            m3_bolt(height=height);
    }
 }
 
 module central_base_m3_bolts(height) {
     translate([0,m3_y_shift,0])
        m3_bolt(height=height);
 }
 
 module m3_base(height=100) {
    difference() {
        linear_extrude(5) // Thickness control for roof
            base(rounded=true);

        side_base_m3_bolts(height);

        mirror()
            side_base_m3_bolts(height);
        
        central_base_m3_bolts(height);
        
        scale([1,-1,1])
            central_base_m3_bolts(height);
    }
 }
 
 module perimeter_m3_bolts() {
    side_base_m3_bolts(height);

    mirror()
        side_base_m3_bolts(height);
    
    central_base_m3_bolts(height);
        
    scale([1,-1,1])
        central_base_m3_bolts(height);
 }

 module breadboard() {
     square([breadboard_width, breadboard_length]);
 }
 
 module L298N() {
     square([L298N_side_length, L298N_side_length]);
 }
 
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

module sprocket(scale_factor=1) {
   rotate([0,90,0]) {
       scale([scale_factor,scale_factor,1])
       sprocket_base_import();
   }
} 
 
 module base(rounded=true) {
     if(rounded) {
        minkowski() {
            square([base_width, base_length], center=true);
            circle(r=rounded_corner_radius,$fn=100);
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

module electronic_components(no_motors=false) {
    if(!no_motors) {
        linear_extrude(motor_height) {
            translate([0,motor_y_shift,0])
                left_and_right_motor_placeholders();
        }
    }

    translate([25,0,0])
        linear_extrude(raspberry_pi_height) {
            translate([0,-base_length/5 ,0])
                raspberry_pi();
        }
    
    translate([-70,0,0])
        linear_extrude(L298N_height) {
            translate([0,-base_length/5 - L298N_side_length/2,0])
                L298N();
        }
    
    translate([-30,40,0])
        linear_extrude(15) {
            translate([0,-base_length/5 ,0])
                breadboard();
        }
}

module place_holder_sprockets() {
    translate([sprocket_distance_from_center,base_length/2.5,sprocket_brace_height/2])
        sprocket(2);
    
    mirror()
        translate([sprocket_distance_from_center,base_length/2.5,sprocket_brace_height/2])
            sprocket(2);
    
    translate([sprocket_distance_from_center,-base_length/2.5,sprocket_brace_height/2])
        sprocket(2);
    
    mirror()
        translate([sprocket_distance_from_center,-base_length/2.5,sprocket_brace_height/2])
            sprocket(2);
}

module body_roof() {
    difference() {
        m3_base();
        
        translate([-29,0,4])
            linear_extrude(2)
                #text("SNOBOT");
    }
}

module body_version_one() {
    linear_extrude(5)
        base(rounded=true);

    //translate([0,0,sprocket_brace_height])
    //linear_extrude(5)
    //    base(rounded=true);

    linear_extrude(sprocket_brace_height)
        left_and_right_sprocket_braces();
    
    if(electronics_on) {
        #electronic_components();
    }
    if(sprockets_on) {
        place_holder_sprockets();
    }
}

// Needs above enclosure mounting points for motors
// to form triangular tank track
module body_version_two() {
    additive_depth = 20;
    difference() {
        linear_extrude(sprocket_brace_height+additive_depth)
            base(rounded=true);
        
        translate([0,0,-1])
        linear_extrude(sprocket_brace_height+additive_depth-5)
        scale([0.94,0.94,1])
            base(rounded=false);
        
        perimeter_m3_bolts(height=20);
    }

    translate([0,-10,0])
    
    if(electronics_on) {
        #electronic_components(no_motors=true);
    }
    if(sprockets_on) {
        place_holder_sprockets();
    }
}

body_version_two();
