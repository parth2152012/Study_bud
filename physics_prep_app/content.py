"""Content module for Physics JEE & NSEP Prep app.

Contains syllabus hierarchy, chapter weightage, formulas, and concept notes.
"""

from __future__ import annotations

SYLLABUS_CONTENT = {
    "Mechanics": {
        "section_weightage": "20–25%",
        "chapters": {
            "Units & Measurement": {
                "weightage": "2–3%",
                "formulas": [
                    r"\text{Error} = \text{Measured Value} - \text{True Value}",
                    r"\text{Relative Error} = \frac{\Delta a}{a}",
                    r"\text{Percentage Error} = \frac{\Delta a}{a}\times 100",
                    r"[Q] = M^aL^bT^c",
                    r"\bar{x} = \frac{x_1 + x_2 + \cdots + x_n}{n}",
                ],
                "concepts": [
                    "Distinguish between fundamental and derived quantities.",
                    "Understand SI base units and prefixes.",
                    "Use significant figures in arithmetic operations.",
                    "Apply dimensional analysis to verify equations.",
                    "Identify random and systematic errors in experiments.",
                ],
            },
            "Motion in Straight Line": {
                "weightage": "2–3%",
                "formulas": [
                    r"v = u + at",
                    r"s = ut + \frac{1}{2}at^2",
                    r"v^2 = u^2 + 2as",
                    r"s_n = u + \frac{a}{2}(2n-1)",
                    r"v_{avg} = \frac{\text{total displacement}}{\text{total time}}",
                ],
                "concepts": [
                    "Differentiate distance and displacement.",
                    "Interpret velocity-time and acceleration-time graphs.",
                    "Uniform and non-uniform motion basics.",
                    "Relative velocity in one dimension.",
                    "Free-fall as uniformly accelerated motion.",
                ],
            },
            "Motion in a Plane": {
                "weightage": "2–3%",
                "formulas": [
                    r"\vec{r} = x\hat{i} + y\hat{j}",
                    r"R = \sqrt{A^2 + B^2 + 2AB\cos\theta}",
                    r"R_{max} = \frac{u^2}{g}",
                    r"T = \frac{2u\sin\theta}{g}",
                    r"H = \frac{u^2\sin^2\theta}{2g}",
                ],
                "concepts": [
                    "Vector addition using triangle/parallelogram law.",
                    "Projectile motion as 2D independent motions.",
                    "Horizontal range and trajectory interpretation.",
                    "Relative velocity in two dimensions.",
                    "Uniform circular motion kinematics.",
                ],
            },
            "Laws of Motion": {
                "weightage": "3–4%",
                "formulas": [
                    r"\vec{F} = m\vec{a}",
                    r"\vec{p} = m\vec{v}",
                    r"\vec{J} = \Delta \vec{p}",
                    r"f_s \leq \mu_s N",
                    r"f_k = \mu_k N",
                ],
                "concepts": [
                    "Newton's three laws and inertial frames.",
                    "Free-body diagrams for force analysis.",
                    "Tension and normal reaction in connected systems.",
                    "Limiting and kinetic friction behavior.",
                    "Pseudo force in non-inertial frames.",
                ],
            },
            "Work, Energy, Power": {
                "weightage": "3–4%",
                "formulas": [
                    r"W = \vec{F}\cdot\vec{s} = Fs\cos\theta",
                    r"K = \frac{1}{2}mv^2",
                    r"U = mgh",
                    r"P = \frac{dW}{dt}",
                    r"W_{net} = \Delta K",
                ],
                "concepts": [
                    "Work-energy theorem applications.",
                    "Conservative vs non-conservative forces.",
                    "Potential energy curves and stability.",
                    "Law of conservation of mechanical energy.",
                    "Power in variable force systems.",
                ],
            },
            "Rotational Motion": {
                "weightage": "4–5%",
                "formulas": [
                    r"\tau = I\alpha",
                    r"L = I\omega",
                    r"K_{rot} = \frac{1}{2}I\omega^2",
                    r"v = r\omega",
                    r"a_t = r\alpha",
                ],
                "concepts": [
                    "Angular kinematics parallels linear kinematics.",
                    "Moment of inertia and radius of gyration.",
                    "Rolling motion and no-slip condition.",
                    "Conservation of angular momentum.",
                    "Torque in equilibrium and dynamics.",
                ],
            },
            "Gravitation": {
                "weightage": "2–3%",
                "formulas": [
                    r"F = G\frac{m_1m_2}{r^2}",
                    r"g = \frac{GM}{R^2}",
                    r"U = -G\frac{Mm}{r}",
                    r"v_e = \sqrt{\frac{2GM}{R}}",
                    r"T^2 \propto r^3",
                ],
                "concepts": [
                    "Universal gravitation and inverse square law.",
                    "Variation of g with altitude and depth.",
                    "Gravitational potential and field relation.",
                    "Satellite motion and orbital velocity.",
                    "Kepler's laws significance in astronomy.",
                ],
            },
        },
    },
    "Heat & Thermodynamics": {
        "section_weightage": "8–10%",
        "chapters": {
            "Thermal Properties": {
                "weightage": "2–3%",
                "formulas": [
                    r"Q = mc\Delta T",
                    r"Q = mL",
                    r"\Delta L = \alpha L\Delta T",
                    r"\Delta V = \gamma V\Delta T",
                    r"\Delta A = 2\alpha A\Delta T",
                ],
                "concepts": [
                    "Heat transfer modes: conduction, convection, radiation.",
                    "Specific heat and latent heat distinction.",
                    "Thermal expansion in solids and liquids.",
                    "Calorimetry and heat balance method.",
                    "Anomalous expansion of water.",
                ],
            },
            "Thermodynamics": {
                "weightage": "3–4%",
                "formulas": [
                    r"\Delta U = Q - W",
                    r"W = \int P\,dV",
                    r"PV = nRT",
                    r"\eta = \frac{W}{Q_h}",
                    r"\eta_{Carnot} = 1 - \frac{T_c}{T_h}",
                ],
                "concepts": [
                    "State variables and process paths.",
                    "Isothermal, adiabatic, isobaric and isochoric processes.",
                    "First law as energy conservation principle.",
                    "Second law and entropy direction.",
                    "Heat engine, refrigerator and COP basics.",
                ],
            },
            "Kinetic Theory": {
                "weightage": "2–3%",
                "formulas": [
                    r"PV = \frac{1}{3}Nm\overline{c^2}",
                    r"\overline{K} = \frac{3}{2}kT",
                    r"v_{rms} = \sqrt{\frac{3RT}{M}}",
                    r"v_{avg} = \sqrt{\frac{8RT}{\pi M}}",
                    r"v_{mp} = \sqrt{\frac{2RT}{M}}",
                ],
                "concepts": [
                    "Postulates of ideal gas kinetic theory.",
                    "Pressure as molecular collisions outcome.",
                    "Degrees of freedom and equipartition theorem.",
                    "Mean, RMS, most probable speeds comparison.",
                    "Real gas deviations and van der Waals idea.",
                ],
            },
        },
    },
    "Oscillations & Waves": {
        "section_weightage": "10–11%",
        "chapters": {
            "Oscillations": {
                "weightage": "5%",
                "formulas": [
                    r"x = A\sin(\omega t + \phi)",
                    r"\omega = \sqrt{\frac{k}{m}}",
                    r"T = 2\pi\sqrt{\frac{m}{k}}",
                    r"a = -\omega^2x",
                    r"E = \frac{1}{2}kA^2",
                ],
                "concepts": [
                    "Simple harmonic motion conditions.",
                    "Phase, amplitude, and angular frequency meaning.",
                    "Energy interchange between K and U in SHM.",
                    "Spring-mass and pendulum approximations.",
                    "Damped and forced oscillations basics.",
                ],
            },
            "Waves": {
                "weightage": "5–6%",
                "formulas": [
                    r"v = f\lambda",
                    r"y = A\sin(kx-\omega t)",
                    r"k = \frac{2\pi}{\lambda}",
                    r"\omega = 2\pi f",
                    r"L = n\frac{\lambda}{2}\,\,(\text{string fixed ends})",
                ],
                "concepts": [
                    "Transverse vs longitudinal wave properties.",
                    "Superposition principle and interference.",
                    "Standing waves and harmonics.",
                    "Beat frequency and resonance.",
                    "Doppler effect in sound waves.",
                ],
            },
        },
    },
    "Electricity & Magnetism": {
        "section_weightage": "20%+",
        "chapters": {
            "Electrostatics": {
                "weightage": "4–5%",
                "formulas": [
                    r"F = k\frac{q_1q_2}{r^2}",
                    r"E = k\frac{q}{r^2}",
                    r"V = k\frac{q}{r}",
                    r"C = \frac{Q}{V}",
                    r"U = \frac{1}{2}CV^2",
                ],
                "concepts": [
                    "Coulomb's law and superposition.",
                    "Electric field lines and potential surfaces.",
                    "Gauss law and symmetry-based calculations.",
                    "Capacitor combinations and dielectric effect.",
                    "Electrostatic potential energy systems.",
                ],
            },
            "Current Electricity": {
                "weightage": "4–5%",
                "formulas": [
                    r"I = \frac{dq}{dt}",
                    r"V = IR",
                    r"R = \rho\frac{L}{A}",
                    r"P = VI = I^2R = \frac{V^2}{R}",
                    r"\varepsilon = I(R+r)",
                ],
                "concepts": [
                    "Drift velocity and current density.",
                    "Resistors in series and parallel.",
                    "Kirchhoff's loop and junction rules.",
                    "Cells with internal resistance.",
                    "Wheatstone bridge and meter bridge principles.",
                ],
            },
            "Moving Charges & Magnetism": {
                "weightage": "4%",
                "formulas": [
                    r"\vec{F} = q(\vec{v}\times\vec{B})",
                    r"F = BIL\sin\theta",
                    r"B = \frac{\mu_0I}{2\pi r}",
                    r"r = \frac{mv}{qB}",
                    r"\tau = NABI\sin\theta",
                ],
                "concepts": [
                    "Magnetic force on moving charge and current.",
                    "Motion in uniform magnetic field.",
                    "Biot–Savart and Ampere laws.",
                    "Torque on current loop and galvanometer basics.",
                    "Earth's magnetism and dip angle.",
                ],
            },
            "Electromagnetic Induction": {
                "weightage": "3–4%",
                "formulas": [
                    r"\mathcal{E} = -\frac{d\Phi_B}{dt}",
                    r"\Phi_B = BA\cos\theta",
                    r"\mathcal{E} = Blv",
                    r"L = \frac{N\Phi}{I}",
                    r"U = \frac{1}{2}LI^2",
                ],
                "concepts": [
                    "Faraday and Lenz laws for induced emf.",
                    "Self and mutual inductance.",
                    "Eddy currents and practical uses.",
                    "Energy stored in inductor magnetic field.",
                    "Generator and transformer principles.",
                ],
            },
            "Alternating Current": {
                "weightage": "2–3%",
                "formulas": [
                    r"i = I_0\sin\omega t",
                    r"V_{rms} = \frac{V_0}{\sqrt{2}}",
                    r"I_{rms} = \frac{I_0}{\sqrt{2}}",
                    r"X_L = \omega L,\,X_C = \frac{1}{\omega C}",
                    r"Z = \sqrt{R^2 + (X_L - X_C)^2}",
                ],
                "concepts": [
                    "Sinusoidal current and voltage basics.",
                    "Phase difference in R, L, C circuits.",
                    "Impedance and resonance condition.",
                    "Power factor and average power.",
                    "Transformer losses and efficiency.",
                ],
            },
            "Electromagnetic Waves": {
                "weightage": "2%",
                "formulas": [
                    r"c = \frac{1}{\sqrt{\mu_0\epsilon_0}}",
                    r"E = cB",
                    r"u = \frac{1}{2}\epsilon_0E^2 + \frac{1}{2\mu_0}B^2",
                    r"I = \frac{1}{2}c\epsilon_0E_0^2",
                    r"\lambda\nu = c",
                ],
                "concepts": [
                    "EM waves are transverse and self-propagating.",
                    "No medium required for propagation.",
                    "Spectrum order and applications.",
                    "Momentum and energy transport by EM waves.",
                    "Polarization concept overview.",
                ],
            },
        },
    },
    "Optics": {
        "section_weightage": "High weightage",
        "chapters": {
            "Ray Optics": {
                "weightage": "6–7%",
                "formulas": [
                    r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}",
                    r"m = \frac{h_i}{h_o} = \frac{v}{u}",
                    r"n_1\sin i = n_2\sin r",
                    r"\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)",
                    r"\frac{1}{f} = \frac{1}{v} + \frac{1}{u}\,\,(\text{lens sign convention form})",
                ],
                "concepts": [
                    "Reflection and refraction laws.",
                    "Image formation by mirrors and lenses.",
                    "Total internal reflection and critical angle.",
                    "Lens maker formula and power of lens.",
                    "Optical instruments basics (microscope/telescope).",
                ],
            },
            "Wave Optics": {
                "weightage": "5–6%",
                "formulas": [
                    r"\Delta x = \frac{\lambda D}{d}",
                    r"\beta = \frac{\lambda D}{d}",
                    r"a\sin\theta = n\lambda\,\,(\text{maxima})",
                    r"a\sin\theta = (2n+1)\frac{\lambda}{2}\,\,(\text{minima})",
                    r"d\sin\theta = n\lambda\,\,(\text{grating})",
                ],
                "concepts": [
                    "Interference in Young's double slit experiment.",
                    "Diffraction from single slit.",
                    "Polarization confirms transverse nature of light.",
                    "Coherent sources requirements.",
                    "Resolving power and optical limits.",
                ],
            },
        },
    },
}


def get_sections() -> list[str]:
    """Return all top-level syllabus sections."""
    return list(SYLLABUS_CONTENT.keys())


def get_chapters(section: str) -> list[str]:
    """Return chapter list for a selected section."""
    return list(SYLLABUS_CONTENT.get(section, {}).get("chapters", {}).keys())
