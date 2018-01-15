
## ref: http://edge.rit.edu/edge/P14651/public/Miscellaneous/Design%20rules%20for%20vacuum%20chambers.pdf
## ref2: https://plastics.ulprospector.com/generics/3/c/t/acrylic-properties-processing

import numpy as np


def circumferential_stress(
        diameter,
        wall_thickness,
        pressure=1e5):
    radius = diameter/2
    return pressure*(radius)/wall_thickness


def axial_stress(
        diameter,
        wall_thickness,
        axial_force,
        pressure=1e5):
    radius = diameter/2
    return (pressure*radius)/(2*wall_thickness) +\
                axial_force/(2*np.pi*radius*wall_thickness)


def von_mises_stress(
        diameter,
        wall_thickness,
        axial_force,
        pressure=1e5):
    radius = diameter/2
    return 0.5 * (3*(pressure*radius/wall_thickness)**2 +\
                  (axial_force/(np.pi*radius*wall_thickness))**2)**0.5


def buckling_pressure(
        diameter,
        wall_thickness,
        youngs_modulus,
        poisson_ratio=0.1**0.5):
    """
    This approximates the pressure at which given tube will fail.
    """

    radius = diameter/2
    return (0.25*youngs_modulus)/(1-poisson_ratio**2) * (wall_thickness/radius)**3


def print_result(
        comment,
        result,
        criterion,
        unit="Pa"):
    print(comment)
    res, scaling = format_si(result)
    print(f"({criterion(result)})\t{res} {scaling}{unit}")

def format_si(value):
    thresholds = [1e9, 1e6, 1e3, 1, 1e-3, 1e-6, 1e-9]
    units = ["G", "M", "k", "", "m", "u", "n"]

    if not isinstance(value, (list, tuple)):
        for thr, unit in zip(thresholds, units):
            if value>thr:
                return (round(value/thr, 2), unit)
    else:
        raise TypeError("This can't take a list (or tuple)")


g = 9.81
psi_to_pa = 6894.76 # let"s keep everything in Pascals

diameter = 0.05
wall_thickness = 0.003
length = 0.12
youngs_modulus = 342000 * psi_to_pa
tensile_strength_yield = 5370 * psi_to_pa

top_cover_weight = 0.2
axial_force = top_cover_weight*g

safety_factor = 1.5

pressure = 1e5


if __name__ == "__main__":

    print("The tensile strength is: "
          f"{format_si(tensile_strength_yield)[0]} "
          f"{format_si(tensile_strength_yield)[1]}Pa")
    print(f"The Young's modulus is: {format_si(youngs_modulus)[0]}"
          f" {format_si(youngs_modulus)[1]}Pa")

    print_result(
        "Circumferential stress:",
        circumferential_stress(diameter, wall_thickness),
        lambda result: "pass" if safety_factor*result<tensile_strength_yield else "fail",
        "Pa")

    print_result(
        "Axial stress:",
        axial_stress(diameter, wall_thickness, axial_force),
        lambda result: "pass" if safety_factor*result<tensile_strength_yield else "fail",
        "Pa")

    print_result(
        "Von Mises stress:",
        von_mises_stress(diameter, wall_thickness, axial_force),
        lambda result: "pass" if safety_factor*result<tensile_strength_yield else "fail",
        "Pa")

    print_result(
        "Buckling pressure:",
        buckling_pressure(diameter, wall_thickness, youngs_modulus),
        lambda result: "pass" if safety_factor*result>pressure else "fail",
        "Pa")
