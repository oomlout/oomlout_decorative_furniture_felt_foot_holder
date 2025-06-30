$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 12, r = 22.5000000000);
		}
	}
	union() {
		#translate(v = [0, 0, -6.0000000000]) {
			cylinder(h = 12, r = 13.5000000000);
		}
		translate(v = [0, 0, 4.0000000000]) {
			cylinder(h = 2, r = 20.5000000000);
		}
	}
}