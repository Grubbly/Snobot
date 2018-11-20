/*
 * snobot_body.scad
 * Tristan Van Cise
 * CS 680 - Project 2
 * 11/19/2018
 *
 * Description:
 *  Snobot's body component
 */
 
 base_width = 130;
 base_length = 180;
 
 module base(rounded=true) {
     if(rounded) {
        minkowski() {
            square([base_width, base_length], center=true);
            circle(r=5);
        }
     } else {
        square([base_width, base_length], center=true);
     }
}
 
 base(rounded=true);