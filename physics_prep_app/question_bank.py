"""Question bank module for chapter-wise MCQs."""

from __future__ import annotations

QUESTION_BANK = {
    "Units & Measurement": [
        {"question": "Which quantity is dimensionless?", "options": ["Strain", "Force", "Pressure", "Momentum"], "answer": "Strain", "difficulty": "Easy", "tag": "JEE"},
        {"question": "SI unit of pressure is:", "options": ["Newton", "Pascal", "Joule", "Watt"], "answer": "Pascal", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Significant figures in 0.00450 are:", "options": ["2", "3", "4", "5"], "answer": "3", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "Dimensions of Planck constant h are:", "options": ["ML^2T^-1", "MLT^-2", "ML^2T^-2", "M^0L^0T^0"], "answer": "ML^2T^-1", "difficulty": "Hard", "tag": "NSEP"},
        {"question": "Random errors can be reduced by:", "options": ["Changing unit", "Taking mean of observations", "Ignoring outliers", "Changing instrument"], "answer": "Taking mean of observations", "difficulty": "Medium", "tag": "JEE"},
    ],
    "Motion in Straight Line": [
        {"question": "Slope of displacement-time graph gives:", "options": ["Acceleration", "Velocity", "Force", "Jerk"], "answer": "Velocity", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Area under velocity-time graph gives:", "options": ["Acceleration", "Displacement", "Speed", "Momentum"], "answer": "Displacement", "difficulty": "Easy", "tag": "JEE"},
        {"question": "For uniformly accelerated motion, v-u equals:", "options": ["a/t", "at", "2as", "s/t"], "answer": "at", "difficulty": "Easy", "tag": "JEE"},
        {"question": "A body dropped from rest has after t seconds velocity:", "options": ["gt", "g/t", "t/g", "g^2t"], "answer": "gt", "difficulty": "Medium", "tag": "JEE"},
        {"question": "If average velocity is zero, displacement is:", "options": ["Maximum", "Minimum", "Zero", "Infinite"], "answer": "Zero", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Motion in a Plane": [
        {"question": "Range of projectile is maximum at angle:", "options": ["30°", "45°", "60°", "90°"], "answer": "45°", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Time of flight for projection u at angle theta is:", "options": ["u cosθ/g", "2u sinθ/g", "u sinθ/2g", "u^2/g"], "answer": "2u sinθ/g", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Unit vector along x-axis is:", "options": ["ĵ", "k̂", "î", "none"], "answer": "î", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Centripetal acceleration direction is:", "options": ["Tangential", "Outward", "Toward center", "Random"], "answer": "Toward center", "difficulty": "Easy", "tag": "JEE"},
        {"question": "For two vectors A and B, maximum resultant is:", "options": ["A-B", "A+B", "AB", "A/B"], "answer": "A+B", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Laws of Motion": [
        {"question": "Newton's first law defines:", "options": ["Momentum", "Inertia", "Impulse", "Power"], "answer": "Inertia", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Impulse equals change in:", "options": ["Kinetic energy", "Velocity", "Momentum", "Force"], "answer": "Momentum", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Friction force on rough surface is proportional to:", "options": ["Area", "Normal reaction", "Speed only", "Mass only"], "answer": "Normal reaction", "difficulty": "Medium", "tag": "JEE"},
        {"question": "In elevator accelerating up, apparent weight is:", "options": ["mg", "m(g-a)", "m(g+a)", "zero"], "answer": "m(g+a)", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "Action-reaction pair acts on:", "options": ["Same body", "Different bodies", "Earth only", "Contact only"], "answer": "Different bodies", "difficulty": "Easy", "tag": "JEE"},
    ],
    "Work, Energy, Power": [
        {"question": "SI unit of work is:", "options": ["Watt", "Joule", "Newton", "Pascal"], "answer": "Joule", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Kinetic energy depends on:", "options": ["Mass only", "Velocity only", "Both mass and velocity", "Height"], "answer": "Both mass and velocity", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Power is rate of:", "options": ["Force", "Displacement", "Doing work", "Momentum change"], "answer": "Doing work", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Work done by conservative force over closed path is:", "options": ["Maximum", "Minimum", "Zero", "Infinity"], "answer": "Zero", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "If net work done is negative, kinetic energy:", "options": ["Increases", "Decreases", "Unchanged", "Becomes zero always"], "answer": "Decreases", "difficulty": "Medium", "tag": "JEE"},
    ],
    "Rotational Motion": [
        {"question": "Rotational analogue of force is:", "options": ["Work", "Power", "Torque", "Momentum"], "answer": "Torque", "difficulty": "Easy", "tag": "JEE"},
        {"question": "SI unit of moment of inertia is:", "options": ["kg m", "kg m^2", "N m", "kg/m"], "answer": "kg m^2", "difficulty": "Medium", "tag": "JEE"},
        {"question": "For pure rolling, v equals:", "options": ["r/ω", "rω", "ω/r", "rω^2"], "answer": "rω", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Angular momentum conserved when:", "options": ["Net force zero", "Net torque zero", "Velocity zero", "Power zero"], "answer": "Net torque zero", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "Kinetic energy of rotating body is:", "options": ["Iω", "Iω^2", "1/2 Iω^2", "2Iω"], "answer": "1/2 Iω^2", "difficulty": "Easy", "tag": "JEE"},
    ],
    "Gravitation": [
        {"question": "Acceleration due to gravity on earth surface is nearly:", "options": ["9.8 m/s^2", "98 m/s^2", "0.98 m/s^2", "1 m/s^2"], "answer": "9.8 m/s^2", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Escape velocity is:", "options": ["√(GM/R)", "√(2GM/R)", "GM/R", "2GM/R"], "answer": "√(2GM/R)", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Gravitational potential is taken zero at:", "options": ["Center of earth", "Surface", "Infinity", "Orbit"], "answer": "Infinity", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Weight of body at earth center is:", "options": ["mg", "mg/2", "2mg", "Zero"], "answer": "Zero", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "Kepler's third law relates:", "options": ["T and r", "v and r", "m and r", "g and r"], "answer": "T and r", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Thermal Properties": [
        {"question": "Heat required to raise temperature is:", "options": ["Q=mcΔT", "Q=mL", "Q=PV", "Q=IR"], "answer": "Q=mcΔT", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Unit of latent heat is:", "options": ["J/kg", "J", "kg/J", "W"], "answer": "J/kg", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Coefficient of linear expansion has unit:", "options": ["K", "K^-1", "m", "m^-1"], "answer": "K^-1", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Convection mainly occurs in:", "options": ["Solids", "Fluids", "Vacuum", "Metals only"], "answer": "Fluids", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Water has maximum density at:", "options": ["0°C", "4°C", "10°C", "100°C"], "answer": "4°C", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Thermodynamics": [
        {"question": "First law of thermodynamics is:", "options": ["Q=W", "ΔU=Q-W", "PV=nRT", "S=Q/T"], "answer": "ΔU=Q-W", "difficulty": "Easy", "tag": "JEE"},
        {"question": "In isochoric process, work done is:", "options": ["Maximum", "Minimum", "Zero", "Negative"], "answer": "Zero", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Carnot engine efficiency depends on:", "options": ["Gas type", "Temperatures", "Pressure", "Volume"], "answer": "Temperatures", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Entropy of isolated system:", "options": ["Decreases", "Constant or increases", "Always zero", "Always decreases"], "answer": "Constant or increases", "difficulty": "Hard", "tag": "NSEP"},
        {"question": "Adiabatic process has:", "options": ["Q=0", "W=0", "ΔU=0", "T=0"], "answer": "Q=0", "difficulty": "Medium", "tag": "JEE"},
    ],
    "Kinetic Theory": [
        {"question": "RMS speed is proportional to:", "options": ["√T", "T", "1/T", "1/√T"], "answer": "√T", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Average kinetic energy of ideal gas molecule is:", "options": ["kT", "3/2 kT", "2kT", "1/2 kT"], "answer": "3/2 kT", "difficulty": "Medium", "tag": "JEE"},
        {"question": "At constant temperature, ideal gas pressure is due to:", "options": ["Gravity", "Molecular collisions", "Friction", "Volume"], "answer": "Molecular collisions", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Degree of freedom for monoatomic gas is:", "options": ["2", "3", "5", "6"], "answer": "3", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Relation among speeds is:", "options": ["vrms < vavg < vmp", "vmp < vavg < vrms", "vavg < vrms < vmp", "all equal"], "answer": "vmp < vavg < vrms", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Oscillations": [
        {"question": "SHM acceleration is:", "options": ["Proportional to x", "Proportional to -x", "Constant", "Zero"], "answer": "Proportional to -x", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Time period of spring block is:", "options": ["2π√(m/k)", "2π√(k/m)", "√(m/k)", "π√(m/k)"], "answer": "2π√(m/k)", "difficulty": "Easy", "tag": "JEE"},
        {"question": "At mean position in SHM, velocity is:", "options": ["Zero", "Maximum", "Minimum", "Negative"], "answer": "Maximum", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Energy in ideal SHM is:", "options": ["Variable", "Constant", "Zero", "Infinity"], "answer": "Constant", "difficulty": "Medium", "tag": "JEE"},
        {"question": "When forcing frequency equals natural frequency, it is:", "options": ["Damping", "Beat", "Resonance", "Interference"], "answer": "Resonance", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Waves": [
        {"question": "Wave speed formula is:", "options": ["v=f/λ", "v=fλ", "v=λ/f", "v=f+λ"], "answer": "v=fλ", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Two waves in phase produce:", "options": ["Destructive interference", "Constructive interference", "No wave", "Random phase"], "answer": "Constructive interference", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Beat frequency equals:", "options": ["f1+f2", "|f1-f2|", "f1f2", "f1/f2"], "answer": "|f1-f2|", "difficulty": "Medium", "tag": "JEE"},
        {"question": "For closed organ pipe, fundamental wavelength is:", "options": ["2L", "L", "4L", "L/2"], "answer": "4L", "difficulty": "Hard", "tag": "NSEP"},
        {"question": "Doppler effect is due to change in:", "options": ["Amplitude", "Frequency", "Intensity", "Speed of source"], "answer": "Frequency", "difficulty": "Medium", "tag": "JEE"},
    ],
    "Electrostatics": [
        {"question": "Unit of electric field is:", "options": ["N/C", "C/N", "J/C", "V/A"], "answer": "N/C", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Potential difference unit is:", "options": ["Ohm", "Volt", "Tesla", "Farad"], "answer": "Volt", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Capacitance of parallel plate capacitor increases with:", "options": ["Distance", "Area", "Both decrease", "Temperature only"], "answer": "Area", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Gauss law is most useful in cases of:", "options": ["No symmetry", "High symmetry", "Random charges", "Only dipoles"], "answer": "High symmetry", "difficulty": "Medium", "tag": "NSEP"},
        {"question": "Electric field inside conductor at electrostatic equilibrium is:", "options": ["Infinite", "Non-zero", "Zero", "Depends on shape"], "answer": "Zero", "difficulty": "Easy", "tag": "JEE"},
    ],
    "Current Electricity": [
        {"question": "Ohm's law is:", "options": ["V=IR", "P=IV", "Q=It", "R=ρL/A"], "answer": "V=IR", "difficulty": "Easy", "tag": "JEE"},
        {"question": "SI unit of resistivity is:", "options": ["Ωm", "Ω/m", "Ωm^2", "S/m"], "answer": "Ωm", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Current in series circuit is:", "options": ["Different", "Same", "Zero", "Infinite"], "answer": "Same", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Kirchhoff's junction rule is based on conservation of:", "options": ["Energy", "Charge", "Mass", "Momentum"], "answer": "Charge", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Maximum power transfer occurs when load resistance equals:", "options": ["Zero", "r", "2r", "infinite"], "answer": "r", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Moving Charges & Magnetism": [
        {"question": "Magnetic force on stationary charge is:", "options": ["Maximum", "Minimum", "Zero", "Infinite"], "answer": "Zero", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Force on current carrying conductor is:", "options": ["BIL sinθ", "BIL cosθ", "IL/B", "B/I"], "answer": "BIL sinθ", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Path of charge entering perpendicular to B is:", "options": ["Straight line", "Parabola", "Circle", "Ellipse"], "answer": "Circle", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Unit of magnetic field is:", "options": ["Tesla", "Weber", "Henry", "Ohm"], "answer": "Tesla", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Cyclotron frequency depends on:", "options": ["velocity", "radius", "qB/m", "mass density"], "answer": "qB/m", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Electromagnetic Induction": [
        {"question": "Induced emf is due to change in:", "options": ["Current", "Flux", "Resistance", "Charge"], "answer": "Flux", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Lenz's law is based on conservation of:", "options": ["Mass", "Charge", "Energy", "Momentum"], "answer": "Energy", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Unit of inductance is:", "options": ["Tesla", "Henry", "Weber", "Farad"], "answer": "Henry", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Motional emf is:", "options": ["Blv", "B/lv", "Bv/l", "lv/B"], "answer": "Blv", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Energy stored in inductor is:", "options": ["LI", "L/I", "1/2 LI^2", "I^2/L"], "answer": "1/2 LI^2", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Alternating Current": [
        {"question": "RMS value of AC current is:", "options": ["I0", "I0/2", "I0/√2", "√2 I0"], "answer": "I0/√2", "difficulty": "Easy", "tag": "JEE"},
        {"question": "In pure resistor circuit, phase difference between V and I is:", "options": ["0", "π/2", "π", "π/4"], "answer": "0", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Inductive reactance is:", "options": ["1/ωL", "ωL", "R/ω", "ωC"], "answer": "ωL", "difficulty": "Medium", "tag": "JEE"},
        {"question": "At resonance in RLC circuit:", "options": ["XL>XC", "XC>XL", "XL=XC", "R=0"], "answer": "XL=XC", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Power factor equals:", "options": ["sinφ", "cosφ", "tanφ", "cotφ"], "answer": "cosφ", "difficulty": "Medium", "tag": "NSEP"},
    ],
    "Electromagnetic Waves": [
        {"question": "Speed of EM wave in vacuum is:", "options": ["3×10^6 m/s", "3×10^8 m/s", "3×10^5 m/s", "3×10^10 m/s"], "answer": "3×10^8 m/s", "difficulty": "Easy", "tag": "JEE"},
        {"question": "EM waves are:", "options": ["Longitudinal", "Transverse", "Mechanical", "Scalar"], "answer": "Transverse", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Which has highest frequency?", "options": ["Infrared", "Visible", "X-rays", "Microwaves"], "answer": "X-rays", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Relation between E and B in EM wave:", "options": ["E=B", "E=cB", "B=cE", "E=B/c^2"], "answer": "E=cB", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Energy flow direction in EM wave is given by:", "options": ["Lorentz force", "Poynting vector", "Coulomb law", "Gauss law"], "answer": "Poynting vector", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Ray Optics": [
        {"question": "Snell's law is:", "options": ["n1sin i=n2sin r", "n1cos i=n2cos r", "n1tan i=n2tan r", "n1i=n2r"], "answer": "n1sin i=n2sin r", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Power of lens unit is:", "options": ["Meter", "Diopter", "Watt", "Tesla"], "answer": "Diopter", "difficulty": "Easy", "tag": "JEE"},
        {"question": "A convex lens forms real image when object is:", "options": ["At focus", "Inside focus", "Beyond focus", "At center only"], "answer": "Beyond focus", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Critical angle occurs when refracted ray angle is:", "options": ["0°", "45°", "90°", "180°"], "answer": "90°", "difficulty": "Medium", "tag": "JEE"},
        {"question": "For mirror, magnification m equals:", "options": ["u/v", "-v/u", "f/v", "v-f"], "answer": "-v/u", "difficulty": "Hard", "tag": "NSEP"},
    ],
    "Wave Optics": [
        {"question": "In YDSE, fringe width is:", "options": ["λd/D", "λD/d", "dD/λ", "D/λd"], "answer": "λD/d", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Interference requires sources to be:", "options": ["Coherent", "Incoherent", "Monochromatic only", "Polarized"], "answer": "Coherent", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Central fringe in YDSE is:", "options": ["Dark", "Bright", "Alternating", "Absent"], "answer": "Bright", "difficulty": "Easy", "tag": "JEE"},
        {"question": "Polarization proves light is:", "options": ["Longitudinal", "Transverse", "Particle only", "Not a wave"], "answer": "Transverse", "difficulty": "Medium", "tag": "JEE"},
        {"question": "Single slit diffraction minima occur at:", "options": ["a sinθ=nλ", "d sinθ=nλ", "a sinθ=(2n+1)λ/2", "a sinθ=nλ/2"], "answer": "a sinθ=nλ", "difficulty": "Hard", "tag": "NSEP"},
    ],
}


def get_all_questions() -> list[dict]:
    """Flatten and return all chapter questions with chapter metadata."""
    flattened = []
    for chapter, questions in QUESTION_BANK.items():
        for q in questions:
            flattened.append({**q, "chapter": chapter})
    return flattened
