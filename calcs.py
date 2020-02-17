# All calculations involving the sub.
# For those of you who write the code, please
# comment your Discord username in case
# of questions from others.

# Made by RedLightning
def calc_ballast_volume (
	sub_vol, struct_vol, struct_weight, water_density=1
):
	'''Calculates the volume of ballast needed,
	assumed to be of the same density as the water around.'''
	
	# Water density defaults to 1, all other units
	# are in kg, m, cm, etc.

	struct_density = struct_weight/struct_vol

	# Density if all space is air (air density is assumed to be zero)
	# Structure density 'evenly spaced' throughout the sub
	empty_density = struct_density/(sub_vol/struct_vol)
	
	# If empty_density is too high, the sub will sink no matter what
	if empty_density > water_density:
		print(f"""The structure weight of {struct_weight}
 is too high. It can be at most {water_density*struct_vol}.""")
		return None

	# Density if all available space is water
	full_density = empty_density + (water_density/sub_vol)

	# We want this algorithm to return 0 if water_density is empty_density.
	# We also want it to return sub_vol - struct_vol if water_density is full_density.

	# First, we calculate how far (from 0 to 1) the water_density is.
	# To do this, we 'shift' the scale so empty_density is 0, and full_density is some other #.
	zero_centered_water_density = water_density - empty_density
	zero_to_one_scaled_density = zero_centered_water_density/(full_density - empty_density)

	# Finally, rescale it and return the result.
	return zero_to_one_scaled_density*(sub_vol - struct_vol)
