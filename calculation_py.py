import numpy as np
# initially consider sphere parametets, SI measurement system ( m, kg, s)

alt = 20000 # [m]
d = 10 #[m]
volume = 4/3 * np.pi * d **3 #  replace with new volume [kg/m^3]
Volume_streamlined_shape = 27.48 # [m^3]
C_d = 0.15 # Calculated by Solidworks based on my geometry
Surface_area = 365 #[m^2]
Velocity = 50 #[m/s]
Ref_area = (Volume_streamlined_shape)**(2/3) #[m^s]
Density_air = 1.293 #[kg/m^-3]

# varianle for propeller drag force coefs
RPM = 3500
d = 103
P = 0.0880
V0 = 20
pitch_angle = 12

##TO DO
# Number of requared solar panels + surface of them + energy genearted + curved surface 
# thrust force from the propeller analysis 
# No more then 100 kg, 8kW 
# Structural mass calculator 
# Volume and surface of the shape of GNVR 


def Drag_force(Density_air, Velocity,Ref_area, C_d ): 
 
    drag_force = 0.5 * Density_air * Velocity**2 * Ref_area *C_d 
    print(f"Drag force = {drag_force} N") 
 
Drag_force(Density_air, Velocity,Ref_area, C_d )

def ro(h):
    # tabular data ro is 0.0889
    ro_srat = 1.204 * np.exp(-10000/10400) # density till 11 km altitude
    ro_trop = ro_srat * np.exp(-(h-10000)/6300) #density in the tropo pause (11-20 km)
    return ro_trop

def lift(v, h):
    bf  = 0.0889 * v * 9.8 #Archimides forse [N]
    all_m = bf/9.8 # availible mass to floal
    return all_m

m = lift(Volume_streamlined_shape, alt)

def drag_force_propeller(pitch_angle,d, P, V0, RPM):
    pitch = np.abs(np.pi * 0.75 * d * np.tan(pitch_angle))
    A = (np.pi * ((0.0254 * d)**2))/4
    B = (RPM * 0.0254 * pitch * (1/60))**2
    C = (d/(3.29546 * pitch))**1.5
    D = (RPM * 0.0254 * pitch * 1/60)* V0
    F = P * A * (B - D) * C
    return F

propeller_drag = drag_force_propeller(pitch_angle, d, P, V0, RPM)
print(f"Propeller drag force: {propeller_drag}, N")
print(f"Availible mass for floating in the {alt} m altitude: {np.round(m,3)} kg")
