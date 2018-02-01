# CPRT 2017/2018 - Aaron Kooner
# Rover Tracking Functions List
# Rover base angle change function should go to motors, the rocer track just outputs some text

import math


# XY angle
# Uses the Equirectangular approximation to find the angle in the xy plane that is an approx
#   for short distances ** lat is latitude and long is longitude
# Inputs:   - a and b arrays for the 2 co-ordinates
# Outputs:  - angle deg
# Uses:     - gps_strd_dec
# MAY NEED TO CONVERT THE INPUTED USING AN STANDARD TO DEGREE FUNCTION
def bearing(p1, p2):
    lat1 = math.radians((p1[0]))
    long1 = math.radians((p1[1]))
    lat2 = math.radians((p2[0]))
    long2 = math.radians((p2[1]))

    #    lat1 = math.radians(gps_strd_dec(a[0]))
    #    long1 = math.radians(gps_strd_dec(a[1]))
    #    lat2 = math.radians(gps_strd_dec(b[0]))
    #    long2 = math.radians(gps_strd_dec(b[1]))

    y = math.sin(long2 - long1) * math.cos(lat1)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(long2 - long1)

    return math.degrees(math.atan2(y, x))  # need to know distance is in m or naw


# GPS distance Calculation
# Finds the distance between two points using Equirectangular projection assuming small distance
# Inputs:   -arrays a and b containing long and lat coordinates
# Outputs:  -the distance in metres or KM
# Uses:
def gps_distance(a, b):
    lat1 = math.radians((a[0]))
    long1 = math.radians((a[1]))
    lat2 = math.radians((b[0]))
    long2 = math.radians((b[1]))

    # lat1 = math.radians(gps_strd_dec(a[0]))
    # long1 = math.radians(gps_strd_dec(a[1]))
    # lat2 = math.radians(gps_strd_dec(b[0]))
    # long2 = math.radians(gps_strd_dec(b[1]))

    x = (long2 - long1) * math.cos((lat1 + lat2) / 2)
    y = lat2 - lat1

    return math.sqrt((x * x + y * y)) * 6371


# Z axis angle
# Calculates the angle in the z plane
# Inputs:   - a b arrays gps long and lat, with ha and hb heights for rover and base
# Outputs:  - angle in z direction for antenna
# Uses:     - gps_distance
def height_deg(a, b, ha, hb):
    hyp = gps_distance(a, b)

    return math.acos((ha - hb) / hyp)


# Rover xy angle difference
# Takes the old rover angle and finds the difference of angle needed to adjust
#   -if the angle is positive, needs to be rotated clock wise, if negative, needs to be counter clockwise
# Inputs:   -given the angle of the rover from the base station new, and the old angle old
# Outputs:  -outputs the differnece in angle needed to adjust
# Uses:
def rover_xyangledif(new, old):
    return old - new


# Rover z angle difference
# Takes the old rover angle and finds the difference of angle needed to adjust
#   -if the angle is positive, needs to be rotated clock wise, if negative, needs to be counter clockwise
# Inputs:   -given the angle of the rover from the base station new, and the old angle old
# Outputs:  -outputs the differnece in angle needed to adjust
# Uses:
def rover_zangledif(new, old):
    return new - old


# Base station angle changes
# Sends what change in angle is needed to point towards the rover
# Inputs:   -rover and base Height, height angles, 2 GPS coordinates
# Outputs:  -xy angle, z angle and distance
# Uses:
def rover_base_anglechange(a, b, old_a, new_height, base_height, old_h):

    return rover_zangledif(height_deg(a, b, new_height, base_height), old_h), rover_xyangledif(bearing(a, b), old_a)


# GPS tracking Main Function
# Puts all together for a full tracking function and displays text too if you need it
# Inputs:   -rover and base Height, height angles, 2 GPS coordinates
# Outputs:  -xy angle, z angle and distance
# Uses:
def rover_track(a, b, old_a, new_height, base_height, old_height_angle, new_height_angle):

    print("Longitude:", a)
    print("Latitude:", b)
    print("\nBearing:", (bearing(a, b)))
    print("Antenna xy angle difference:", rover_xyangledif(bearing(a, b), old_a))
    print("\nOld xy angle:", old_a)
    print("New height:", new_height)
    print("Old z angle:", old_height_angle)
    print("New z Angle:", height_deg(a, b, new_height, base_height))
    print("Antenna z angle difference:", rover_zangledif(height_deg(a, b, new_height, base_height), old_height_angle))
    print("Distance of rover in KM:", gps_distance(a, b))
    print("Distance of rover in M:", gps_distance(a, b) * 1000)
    print("\nAngle base station z angle:", height_deg(a, b, new_height, base_height))
    print("Angle difference of base station", rover_zangledif(height_deg(a, b, new_height, base_height),
                                                              old_height_angle))

############################################TEST BENCH############################################


# a = [39.099912, -94.581213]
# b = [38.627089, -90.200203]
# old_xyangle = 96
# old_height = 60  # degrees
# new_height = 62.5553  # metres
# base_height = 34.4287  # metres
# old_height_angle = 1.6443117779319936  # degrees
# new_height_angle = 2.6434443511575636  # degrees

# rover_track(a, b, old_xyangle, new_height, base_height, old_height_angle, new_height_angle)

# print(rover_base_anglechange(a, b, old_xyangle, new_height, base_height, old_height_angle))
