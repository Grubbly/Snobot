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

module motor_axle() {
    translate([-12.5,0,0])
        rotate([0,90,0])
            cylinder(d=6, h=13, center=false);
}

module sprocket_fill(col = "Blue") {
    color(col, 1.0)
    translate([-12.49,0,0])
        rotate([0,90,0])
            cylinder(d=5.95, h=10, center=false, $fn=100);
}


translate([-43,0,0])
rotate([0,0,90])
union() {
    sprocket(scale_factor=2);
    difference() {
    scale([1,2,2])
        sprocket_fill(col="Red");
        
        // Stretch to eliminate z-buffer fighting
        translate([5,0,0])
            scale([2,1,1])
                sprocket_fill();
    }
}