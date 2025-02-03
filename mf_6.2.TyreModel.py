from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    computed_field,
)
import numpy as np
from pathlib import Path
from typing import Type
    
class MF62tire(BaseModel):
    """Base model containing shared properties between linear and nonlinear models"""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    # ----------------------#
    # MDI_HEADER            #
    # ----------------------#

    FILE_TYPE: str = Field(
        default= 'tir',
        description="File Type",
    )
    FILE_VERSION: float = Field(
        default= 3,
        description="File version",
    )
    FILE_FORMAT: str = Field(
        default= 'ASCII',
        description="File format",
    )

    # -----------------#
    # Units            #
    # -----------------#

    LENGTH: str = Field(
        description="Length Unit",
    )
    FORCE: str = Field(
        description="Force Unit",
    )
    ANGLE: str = Field(
        description="Angle Unit",
    )
    MASS: str = Field(
        description="Mass Unit",
    )
    TIME: str = Field(
        description="Time Unit",
    )

    # ----------------------#
    # Model                 #
    # ----------------------#

    FITTYP: float = Field(
        description="Magic Formula version number",
    )
    plus: int = Field( 
        default = 1,
        description="moment representaiton 0=ground frame, 1=wheel frame"
    )
    TYRESIDE: str = Field(
        description="Position of tyre during measyrments",
    )
    LONGVL: float = Field(
        description="Reference speed"
    )
    VXLOW: float = Field(
        description="Lower boundary velocity in slip calculation"
    )
    ROAD_INCREMENT: float = Field(
        description="Increment in raod sampling"
    )
    ROAD_DIRECTION: float = Field(
        description="direction of travelled distance"
    )
    PROPERTY_FILE_FORMAT: float = Field(
        default = 0,
        description="Tyre model selection (Adams only)"
    )
    USE_MODE: float = Field(
        default = 0,
        description="Tyre use mode switch (Adams only)"
    )
    HMAX_LOCAL: float = Field(
        default = 0,
        description="Local integration time step (Adams only)"
    )
    TIME_SWITCH_INTEG: float = Field(
        default = 0,
        description="Time when local integrator is activ ated (Adams only)"
    )

    # ----------------------#
    # Dimension             #
    # ----------------------#

    UNLOADED_RADIUS: float = Field(
        description="Free tyre radius"
    )
    WIDTH: float = Field(
        description="Nominal section width of the tyre"
    )
    RIM_RADIUS: float = Field(
        description="Nominal rim radius"
    )
    RIM_WIDTH: float = Field(
        description="Rim Width"
    )
    ASPECT_RATIO: float = Field(
        description="Nominal aspect ratio"
    )

    # ----------------------#
    # Operating Conditions  #
    # ----------------------#

    INFLPRES: float = Field(
        description="Tyre inflation pressure"
    )
    NOMPRES: float = Field(
        description="Nominal pressure used in (MF) equations"
    )

    # ----------------------#
    # Inertia               #
    # ----------------------#

    MASS: float = Field(
        description="Tyre mass"
    )
    IXX: float = Field(
        description="Trey diametral moment of inertia"
    )
    IYY: float = Field(
        description="Tyre polar moment of inertia "
    )
    BELT_MASS: float = Field(
        description="Belt mass"
    )
    BELT_IXX: float = Field(
        description="Belt dimentional moment of inertia"
    )
    BELT_IYY: float = Field(
        description="Belt polar moment of inertia"
    )
    GRAVITY: float = Field(
        description="Gravity acting on belt in Z direction"
    )

    # ----------------------#
    # Vertical              #
    # ----------------------#

    FNOMIN: float = Field(
        default = 0,
        description="Nominal wheel load"
    )
    VERTICAL_STIFFNESS: float = Field(
        description="Tyre vertical stiffness"
    )
    VERTICAL_DAMPENING: float = Field(
        default = 1,
        description="Tyre vertical dampening"
    )
    MC_CONTOR_A: float = Field(
        default = 1,
        description="Motorcycle contour ellipse A"
    )
    MC_CONTOR_B: float = Field(
        default = 1,
        description="Motorcycle contour ellipse B"
    )
    BREFF: float = Field(
        description="Low load stifdness of effective rolling radius"
    )
    DREFF: float = Field(
        description="Peak value of effective rolling radius"
    )
    FREFF: float = Field(
        description="High load stiffness of effective a rolling radius"
    )
    Q_RE0: float = Field(
        description="Ratio of free tyre radiu with nominal tyre radius"
    )
    Q_V1: float = Field(
        description="Tyre radius increase with speed"
    )
    Q_V2: float = Field(
        description="Vertical stiffness increase with speed"
    )
    Q_FZ2: float = Field(
        description="Quadratic term in load vs. deflection"
    )
    Q_FCX: float = Field(
        description="Longitudinal force influence on vertical stiffness"
    )
    Q_FCY: float = Field(
        description="Lateral force influence on vertical stiffness"
    )
    Q_FCY2: float = Field(
        default = 1,
        description="Explicit load dependences for including the lateral force influence on vertical stiffness"
    )
    Q_CAM: float = Field(
        description="Linear load dependent camber angle influence on vertical stiffness"
    )
    Q_CAM1: float = Field(
        description="Linear load dependent camber angle influence on vertical stiffness"
    )
    Q_CAM2: float = Field(
        description="Quadratic load dependent camber angle influence on vertical stiffness"
    )
    Q_CAM3: float = Field(
        description="Linear load and camber angle dependent reduction on vertical stiffness"
    )
    Q_FYS1: float = Field(
        description="Combined camber angle and side slip angle effect on vertical stiffness (constant)"
    )
    Q_FYS2: float = Field(
        description="Combined camber angle and side slip angle linear effect on vertical stiffness"
    )
    Q_FYS3: float = Field(
        description="Combined camber angle and side slip angle quadratic effect on vertical stiffness"
    )
    PFZ1: float = Field(
        description="Pressure effect on vertical stiffness"
    )
    BOTTOM_OFFST: float = Field(
        description="Distance to rim when bottoming starts to occur"
    )
    BOTTOM_STIFF: float = Field(
        description="Vertical stiffness of bottomed tyre"
    )

    # ----------------------#
    # Structural            #
    # ----------------------#

    LONGITUDINAL_STIFFNESS: float = Field(
        description="Tyre overall longitudinal stiffness"
    )
    LATERAL_STIFFNESS: float = Field(
        description="Tyre overall lateral stiffness"
    )
    YAW_STIFFNESS: float = Field(
        description="Tyre overall yaw stiffness"
    )
    FREQ_LONG: float = Field(
        description="Undamped frequency fore/aft and vertical mode"
    )
    FREQ_LAT: float = Field(
        description="Undamped frequency lateral mode"
    )
    FREQ_YAW: float = Field(
        description="Undamped frequency yaw and camber mode"
    )
    FREQ_WINDUP: float = Field(
        description="Undamped frequency wind-up mode"
    )
    DAMP_LONG: float = Field(
        description="Dimensionless damping fore/aft and vertical mode"
    )
    DAMP_LAT: float = Field(
        description="Dimensionless damping lateral mode"
    )
    DAMP_YAW: float = Field(
        description="Dimensionless damping yaw and camber mode"
    )
    DAMP_WINDUP: float = Field(
        description="Dimensionless damping wind-up mode"
    )
    DAMP_RESIDUAL: float = Field(
        description="Residual damping (proportional to stiffness)"
    )
    DAMP_VLOW: float = Field(
        description="Additional low speed damping (proportional to stiffness)"
    )
    Q_BVX: float = Field(
        description="Load and speed inf luence on in-plane translation stiffness"
    )
    Q_BVT: float = Field(
        description="Load and speed inf luence on in-plane rotation stiffness"
    )
    PCFX1: float = Field(
        description="Tyre overall longitudinal stiffness vertical deflection dependency linear term"
    )
    PCFX2: float = Field(
        description="Tyre overall longitudinal stiffness vertical deflection dependency quadratic term"
    )
    PCFX3: float = Field(
        description="Tyre overall longitudinal stiffness pressure dependency"
    )
    PCFY1: float = Field(
        description="Tyre overall lateral stiffness vertical deflection dependency linear term"
    )
    PCFY2: float = Field(
        description="Tyre overall lateral stiffness vertical deflection dependency quadratic term"
    )
    PCFY3: float = Field(
        description="Tyre overall lateral stiffness pressure dependency"
    )
    PCMZ1: float = Field(
        description="Tyre overall yaw stiffness pressure dependency"
    )

    # ----------------------#
    # Contact Patch         #
    # ----------------------#

    Q_RA1: float = Field(
        description="Square root term in contact length equation"
    )
    Q_RA2: float = Field(
        description="Linear term in contact length equation"
    )
    Q_RB1: float = Field(
        description="Root term in contact width equation"
    )
    Q_RB2: float = Field(
        description="Linear term in contact width equation"
    )
    ELLIPS_SHIFT: float = Field(
        description="Scaling of distance between front and rear ellipsoid"
    )
    ELLIPS_LENGTH: float = Field(
        description="Semimajor axis of ellipsoid"
    )
    ELLIPS_HEIGHT: float = Field(
        description="Semiminor axis of ellipsoid"
    )
    ELLIPS_ORDER: float = Field(
        description="Order of ellipsoid"
    )
    ELLIPS_MAX_STEP: float = Field(
        description="Maximum height of road step"
    )
    ELLIPS_NWIDTH: float = Field(
        description="Number of parallel ellipsoids"
    )
    ELLIPS_NLENGTH: float = Field(
        description="Number of ellipsoids at sides of contact patch"
    )
    ELLIPS_NLENGTH: float = Field(
        description="Number of ellipsoids at sides of contact patch"
    )
    ENV_C1: float = Field(
        description="Effective height attenuation"
    )
    ENV_C2: float = Field(
        description="Effective plane angle attenuation"
    )

    # -------------------------#
    # INFLATION PRESSURE RANGE #
    # -------------------------#

    PRESMIN: float = Field(
        description="Minimum allowed inflation pressure"
    )
    PRESMAX: float = Field(
        description="Maximum allowed inflation pressure"
    )

    # ----------------------#
    # VERTICAL FORCE RANGE  #
    # ----------------------#

    FZMIN: float = Field(
        #default = read_in_values("FZMIN", tir_file),
        description="Minimum allowed wheel load"
    )
    FZMAX: float = Field(
        #default = read_in_values("FZMAX", tir_file),
        description="Maximum allowed wheel load"
    )

    # ----------------------#
    # LONG SLIP RANGE       #
    # ----------------------#

    KPUMIN: float = Field(
        #default = read_in_values("KPUMIN", tir_file),
        description="Minimum valid wheel slip"
    )
    KPUMAX: float = Field(
        #default = read_in_values("KPUMAX", tir_file),
        description="Maximum valid wheel slip"
    )

    # ----------------------#
    # SLIP ANGLE RANGE      #
    # ----------------------#

    ALPMIN: float = Field(
        #default = read_in_values("ALPMIN", tir_file),
        description="Minimum valid slip angle"
    )
    ALPMAX: float = Field(
        #default = read_in_values("ALPMAX", tir_file),
        description="Maximum valid slip angle"
    )

    # ------------------------#
    # INCLINATION ANGLE RANGE #
    # ------------------------#

    CAMMIN: float = Field(
        #default = read_in_values("CAMMIN", tir_file),
        description="Minimum valid camber angle"
    )
    CAMMAX: float = Field(
        #default = read_in_values("CAMMAX", tir_file),
        description="Maximum valid camber angle"
    )

    # ----------------------#
    # SCALING COEFFICIENTS  #
    # ----------------------#

    LFZO: float = Field(
        #default = read_in_values("LFZO", tir_file),
        description="Scale factor of nominal (rated) load"
    )
    LCX: float = Field(
        #default = read_in_values("LCX", tir_file),
        description="Scale factor of Fx shape factor"
    )
    LMUX: float = Field(
        #default = read_in_values("LMUX", tir_file),
        description="Scale factor of Fx peak friction coefficient"
    )
    LEX: float = Field(
        #default = read_in_values("LEX", tir_file),
        description="Scale factor of Fx curvature factor"
    )
    LKX: float = Field(
        #default = read_in_values("LKX", tir_file),
        description="Scale factor of slip stiffness"
    )
    LHX: float = Field(
        #default = read_in_values("LHX", tir_file),
        description="Scale factor of Fx horizontal shift"
    )
    LVX: float = Field(
        #default = read_in_values("LVX", tir_file),
        description="Scale factor of Fx vertical shift"
    )
    LCY: float = Field(
        #default = read_in_values("LCY", tir_file),
        description="Scale factor of Fy shape factor"
    )
    LMUY: float = Field(
        #default = read_in_values("LMUY", tir_file),
        description="Scale factor of Fy peak friction coefficient"
    )
    LEY: float = Field(
        #default = read_in_values("LEY", tir_file),
        description="Scale factor of Fy curvature factor"
    )
    LKY: float = Field(
        #default = read_in_values("LKY", tir_file),
        description="Scale factor of cornering stiffness"
    )
    LKYC: float = Field(
        #default = read_in_values("LKYC", tir_file),
        description="Scale factor of camber stiffness"
    )
    LKZC: float = Field(
        #default = read_in_values("LKZC", tir_file),
        description="Scale factor of camber moment stiffness"
    )
    LHY: float = Field(
        #default = read_in_values("LHY", tir_file),
        description="Scale factor of Fy horizontal shift"
    )
    LVY: float = Field(
        #default = read_in_values("LVY", tir_file),
        description="Scale factor of Fy vertical shift"
    )
    LTR: float = Field(
        #default = read_in_values("LTR", tir_file),
        description="Scale factor of Peak of pneumatic trail"
    )
    LRES: float = Field(
        #default = read_in_values("LRES", tir_file),
        description="Scale factor for offset of residual torque"
    )
    LXAL: float = Field(
        #default = read_in_values("LXAL", tir_file),
        description="Scale factor of alpha influence on Fx"
    )
    LYKA: float = Field(
        #default = read_in_values("LYKA", tir_file),
        description="Scale factor of alpha influence on Fx"
    )
    LVYKA: float = Field(
        #default = read_in_values("LVYKA", tir_file),
        description="Scale f actor of kappa induced Fy"
    )
    LS: float = Field(
        #default = read_in_values("LS", tir_file),
        description="Scale factor of Moment arm of Fx"
    )
    LMX: float = Field(
        #default = read_in_values("LMX", tir_file),
        description="Scale factor of overturning moment"
    )
    LVMX: float = Field(
        #default = read_in_values("LVMX", tir_file),
        description="Scale factor of Mx vertical shift"
    )
    LMY: float = Field(
        #default = read_in_values("LMY", tir_file),
        description="Scale factor of rolling resistance torque"
    )
    LMP: float = Field(
        #default = read_in_values("LMP", tir_file),
        description="Scale factor of parking moment"
    )
    
    # ---------------------------#
    # LONGITUDINAL COEFFICIENTS  #
    # ---------------------------#

    PCX1: float = Field(
        #default = read_in_values("PCX1", tir_file),
        description="Shape factor Cf x for longitudinal force"
    )
    PDX1: float = Field(
        #default = read_in_values("PDX1", tir_file),
        description="Longitudinal friction Mux at Fznom"
    )
    PDX2: float = Field(
        #default = read_in_values("PDX2", tir_file),
        description="Variation of friction Mux with load"
    )
    PDX3: float = Field(
        #default = read_in_values("PDX3", tir_file),
        description="Variation of friction Mux with camber"
    )
    PEX1: float = Field(
        #default = read_in_values("PEX1", tir_file),
        description="Longitudinal curvature Ef x at Fznom"
    )
    PEX2: float = Field(
        #default = read_in_values("PEX2", tir_file),
        description="Variation of curvature Ef x with load"
    )
    PEX3: float = Field(
        #default = read_in_values("PEX3", tir_file),
        description="Variation of curvature Ef x with load squared"
    )
    PEX4: float = Field(
        #default = read_in_values("PEX4", tir_file),
        description="Factor in curvature Ef x while driving "
    )
    PKX1: float = Field(
        #default = read_in_values("PKX1", tir_file),
        description="Longitudinal slip stiffness Kfx/Fz at Fznom"
    )
    PKX2: float = Field(
        #default = read_in_values("PKX2", tir_file),
        description="Variation of slip stiffness Kfx/Fz with load"
    )
    PKX3: float = Field(
        #default = read_in_values("PKX3", tir_file),
        description="Exponent in slip stiffness Kfx/Fz with load"
    )
    PHX1: float = Field(
        #default = read_in_values("PHX1", tir_file),
        description="Horizontal shift Shx at Fznom"
    )
    PHX2: float = Field(
        #default = read_in_values("PHX2", tir_file),
        description="Variation of shift Shx with load"
    )
    PVX1: float = Field(
        #default = read_in_values("PVX1", tir_file),
        description="Vertical shift Svx/Fz at Fznom "
    )
    PVX2: float = Field(
        #default = read_in_values("PVX2", tir_file),
        description="Variation of shift Svx/Fz with load"
    )
    RBX1: float = Field(
        #default = read_in_values("RBX1", tir_file),
        description="Slope factor for combined slip Fx reduction"
    )
    RBX2: float = Field(
        #default = read_in_values("RBX2", tir_file),
        description="Variation of slope Fx reduction with kappa"
    )
    RBX3: float = Field(
        #default = read_in_values("RBX3", tir_file),
        description="Influence of camber on stiffness for Fx combined"
    )
    RCX1: float = Field(
        #default = read_in_values("RCX1", tir_file),
        description="Shape factor for combined slip Fx reduction"
    )
    REX1: float = Field(
        #default = read_in_values("REX1", tir_file),
        description="Curvature factor of combined Fx"
    )
    REX2: float = Field(
        #default = read_in_values("REX2", tir_file),
        description="Curvature factor of combined Fx with load"
    )
    RHX1: float = Field(
        #default = read_in_values("RHX1", tir_file),
        description="Shift factor for combined slip Fx reduction"
    )
    PPX1: float = Field(
        #default = read_in_values("PPX1", tir_file),
        description="Linear pressure effect on slip stiffness"
    )
    PPX2: float = Field(
        #default = read_in_values("PPX2", tir_file),
        description="Quadratic pressure effect on slip stiffness"
    )
    PPX3: float = Field(
        #default = read_in_values("PPX3", tir_file),
        description="Linear pressure effect on longitudinal friction"
    )
    PPX4: float = Field(
        #default = read_in_values("PPX4", tir_file),
        description="Quadratic pressure effect on longitudinal friction"
    )

    # ---------------------------#
    # OVERTURNING COEFFICIENTS   #
    # ---------------------------#

    QSX1: float = Field(
        #default = read_in_values("QSX1", tir_file),
        description="Overturning moment offset"
    )
    QSX2: float = Field(
        #default = read_in_values("QSX2", tir_file),
        description="Camber induced overturning couple"
    )
    QSX3: float = Field(
        #default = read_in_values("QSX3", tir_file),
        description="Fy induced overturning couple"
    )
    QSX4: float = Field(
        #default = read_in_values("QSX4", tir_file),
        description="Mixed load, lateral force and camber on Mx"
    )
    QSX5: float = Field(
        #default = read_in_values("QSX5", tir_file),
        description="Load effect on Mx with lateral force and camber"
    )
    QSX6: float = Field(
        #default = read_in_values("QSX6", tir_file),
        description="B-factor of load with Mx"
    )
    QSX7: float = Field(
        #default = read_in_values("QSX7", tir_file),
        description="Camber with load on Mx"
    )
    QSX8: float = Field(
        #default = read_in_values("QSX8", tir_file),
        description="Lateral force with load on Mx"
    )
    QSX9: float = Field(
        #default = read_in_values("QSX9", tir_file),
        description="B-factor of lateral force with load on Mx"
    )
    QSX10: float = Field(
        #default = read_in_values("QSX10", tir_file),
        description="Vertical force with camber on Mx"
    )
    QSX11: float = Field(
        #default = read_in_values("QSX11", tir_file),
        description="B-factor of vertical force with camber on Mx"
    )
    QSX12: float = Field(
        #default = read_in_values("QSX12", tir_file),
        description="Camber squared induced overturning moment"
    )
    QSX13: float = Field(
        #default = read_in_values("QSX13", tir_file),
        description="Lateral force induced overturning moment"
    )
    QSX14: float = Field(
        #default = read_in_values("QSX14", tir_file),
        description="Lateral force induced overturning moment with camber"
    )
    PPMX1: float = Field(
        #default = read_in_values("PPMX1", tir_file),
        description="Influence of inflation pressure on overturning moment"
    )

    # ---------------------------#
    # LATERAL COEFFICIENTS       #
    # ---------------------------#

    PCY1: float = Field(
        #default = read_in_values("PCY1", tir_file),
        description="Shape factor Cfy for lateral forces "
    )
    PDY1: float = Field(
        #default = read_in_values("PDY1", tir_file),
        description="Lateral friction Muy"
    )
    PDY2: float = Field(
        #default = read_in_values("PDY2", tir_file),
        description="Variation of friction Muy with load"
    )
    PDY3: float = Field(
        #default = read_in_values("PDY3", tir_file),
        description="Variation of friction Muy with squared camber"
    )
    PEY1: float = Field(
        #default = read_in_values("PEY1", tir_file),
        description="Lateral curvature Efy at Fznom"
    )
    PEY2: float = Field(
        #default = read_in_values("PEY2", tir_file),
        description="Variation of curvature Efy with load"
    )
    PEY3: float = Field(
        #default = read_in_values("PEY3", tir_file),
        description="Zero order camber dependency of curvature Efy"
    )
    PEY4: float = Field(
        #default = read_in_values("PEY4", tir_file),
        description="Variation of curvature Efy with camber"
    )
    PEY5: float = Field(
        #default = read_in_values("PEY5", tir_file),
        description="Camber curv ature Efc"
    )
    PKY1: float = Field(
        #default = read_in_values("PKY1", tir_file),
        description="Maximum value of stiffness Kfy/Fznom "
    )
    PKY2: float = Field(
        #default = read_in_values("PKY2", tir_file),
        description="Load at which Kfy reaches maximum value"
    )
    PKY3: float = Field(
        #default = read_in_values("PKY3", tir_file),
        description="Variation of Kfy/Fznom with camber"
    )
    PKY4: float = Field(
        #default = read_in_values("PKY4", tir_file),
        description="Curvature of stiffness Kfy"
    )
    PKY5: float = Field(
        #default = read_in_values("PKY5", tir_file),
        description="Peak stiffness variation with camber squared"
    )
    PKY6: float = Field(
        #default = read_in_values("PKY6", tir_file),
        description="Camber stiffness factor"
    )
    PKY7: float = Field(
        #default = read_in_values("PKY7", tir_file),
        description="Load dependency of camber stiffness factor"
    )
    PHY1: float = Field(
        #default = read_in_values("PHY1", tir_file),
        description="Horizontal shift Shy at Fznom"
    )
    PHY2: float = Field(
        #default = read_in_values("PHY2", tir_file),
        description="Variation of shift Shy with load"
    )
    PVY1: float = Field(
        #default = read_in_values("PVY1", tir_file),
        description="Vertical shift in Svy/Fz at Fznom"
    )
    PVY2: float = Field(
        #default = read_in_values("PVY2", tir_file),
        description="Variation of shif t Svy/Fz with load"
    )
    PVY3: float = Field(
        #default = read_in_values("PVY3", tir_file),
        description="Variation of shift Svy/Fz with camber"
    )
    PVY4: float = Field(
        #default = read_in_values("PVY4", tir_file),
        description="Variation of shift Svy/Fz with camber and load"
    )
    RBY1: float = Field(
        #default = read_in_values("RBY1", tir_file),
        description="Slope factor for combined Fy reduction"
    )
    RBY2: float = Field(
        #default = read_in_values("RBY2", tir_file),
        description="Variation of slope Fy reduction with alpha"
    )
    RBY3: float = Field(
        #default = read_in_values("RBY3", tir_file),
        description="Shift term for alpha in slope Fy reduction"
    )
    RBY4: float = Field(
        #default = read_in_values("RBY4", tir_file),
        description="Influence of camber on stiffness of Fy combined"
    )
    RCY1: float = Field(
        #default = read_in_values("RCY1", tir_file),
        description="Shape factor for combined Fy reduction"
    )
    REY1: float = Field(
        #default = read_in_values("REY1", tir_file),
        description="Curvature factor of combined Fy"
    )
    REY2: float = Field(
        #default = read_in_values("REY2", tir_file),
        description="Curvature factor of combined Fy with load"
    )
    RHY1: float = Field(
        #default = read_in_values("RHY1", tir_file),
        description="Shift factor for combined Fy reduction"
    ) 
    RHY2: float = Field(
        #default = read_in_values("RHY2", tir_file),
        description="Shift factor for combined Fy reduction with load"
    )
    RVY1: float = Field(
        #default = read_in_values("RVY1", tir_file),
        description="Kappa induced side force Svyk/Muy*Fz at Fznom"
    )
    RVY2: float = Field(
        #default = read_in_values("RVY2", tir_file),
        description="Variation of Svyk/Muy*Fz with load"
    )
    RVY3: float = Field(
        #default = read_in_values("RVY3", tir_file),
        description="Variation of Svyk/Muy*Fz with camber"
    )
    RVY4: float = Field(
        #default = read_in_values("RVY4", tir_file),
        description="Variation of Svyk/Muy*Fz with alpha"
    )
    RVY5: float = Field(
        #default = read_in_values("RVY5", tir_file),
        description="Variation of Svyk/Muy*Fz with kappa"
    )
    RVY6: float = Field(
        #default = read_in_values("RVY6", tir_file),
        description="Variation of Svyk/Muy*Fz with atan(kappa)"
    )
    PPY1: float = Field(
        #default = read_in_values("PPY1", tir_file),
        description="Pressure effect on cornering stiffness magnitude"
    )
    PPY2: float = Field(
        #default = read_in_values("PPY2", tir_file),
        description="Pressure effect on location of cornering stiffness peak"
    )
    PPY3: float = Field(
        #default = read_in_values("PPY3", tir_file),
        description="Linear pressure effect on lateral friction"
    )
    PPY4: float = Field(
        #default = read_in_values("PPY4", tir_file),
        description="Quadratic pressure effect on lateral friction"
    )
    PPY5: float = Field(
        #default = read_in_values("PPY5", tir_file),
        description="Influence of inflation pressure on camber stiffness"
    )

    # ---------------------------#
    # ROLLING COEFFICIENTS       #
    # ---------------------------#

    QSY1: float = Field(
        #default = read_in_values("QSY1", tir_file),
        description="Rolling resistance torque coefficient"
    )
    QSY2: float = Field(
        #default = read_in_values("QSY2", tir_file),
        description="Rolling resistance torque depending on Fx"
    )
    QSY3: float = Field(
        #default = read_in_values("QSY3", tir_file),
        description="Rolling resistance torque depending on speed"
    )
    QSY4: float = Field(
        #default = read_in_values("QSY4", tir_file),
        description="Rolling resistance torque depending on speed ^4"
    )
    QSY5: float = Field(
        #default = read_in_values("QSY5", tir_file),
        description="Rolling resistance torque depending on camber squared"
    )
    QSY6: float = Field(
        #default = read_in_values("QSY6", tir_file),
        description="Rolling resistance torque depending on load and camber squared"
    )
    QSY7: float = Field(
        #default = read_in_values("QSY7", tir_file),
        description="Rolling resistance torque coefficient load dependency"
    )
    QSY8: float = Field(
        #default = read_in_values("QSY8", tir_file),
        description="Rolling resistance torque coefficient pressure dependency"
    )

    # ---------------------------#
    # ALIGNING COEFFICIENTS      #
    # ---------------------------#

    QBZ1: float = Field(
        #default = read_in_values("QBZ1", tir_file),
        description="Trail slope factor for trail Bpt at Fznom"
    )
    QBZ2: float = Field(
        #default = read_in_values("QBZ2", tir_file),
        description="Variation of slope Bpt with load"
    )
    QBZ3: float = Field(
        #default = read_in_values("QBZ3", tir_file),
        description="Variation of slope Bpt with load squared"
    )
    QBZ4: float = Field(
        #default = read_in_values("QBZ4", tir_file),
        description="Variation of slope Bpt with camber"
    )
    QBZ5: float = Field(
        #default = read_in_values("QBZ5", tir_file),
        description="Variation of slope Bpt with absolute camber"
    )
    QBZ9: float = Field(
        default = 0,
        description="Slope factor Br of residual torque Mzr"
    )
    QBZ10: float = Field(
        #default = read_in_values("QBZ10", tir_file),
        description="Slope factor Br of residual torque Mzr"
    )
    QCZ1: float = Field(
        #default = read_in_values("QCZ1", tir_file),
        description="Shape factor Cpt for pneumatic trail"
    )
    QDZ1: float = Field(
        #default = read_in_values("QDZ1", tir_file),
        description="Peak trail Dpt = Dpt*(Fz/Fznom*R0)"
    )
    QDZ2: float = Field(
        #default = read_in_values("QDZ2", tir_file),
        description="Variation of peak Dpt with load"
    )
    QDZ3: float = Field(
        #default = read_in_values("QDZ3", tir_file),
        description="Variation of peak Dpt with camber"
    )
    QDZ4: float = Field(
        #default = read_in_values("QDZ4", tir_file),
        description="Variation of peak Dpt with camber squared"
    )
    QDZ6: float = Field(
        #default = read_in_values("QDZ6", tir_file),
        description="Peak residual torque Dmr = Dmr/(Fz*R0)"
    )
    QDZ7: float = Field(
        #default = read_in_values("QDZ7", tir_file),
        description="Variation of peak factor Dmr with load"
    )
    QDZ8: float = Field(
        #default = read_in_values("QDZ8", tir_file),
        description="Variation of peak factor Dmr with camber"
    )
    QDZ9: float = Field(
        #default = read_in_values("QDZ9", tir_file),
        description="Variation of peak factor Dmr with camber and load"
    )
    QDZ10: float = Field(
        #default = read_in_values("QDZ10", tir_file),
        description="Slope factor Br of residual torque Mzr"
    )
    QDZ11: float = Field(
        #default = read_in_values("QDZ11", tir_file),
        description="Shape factor Cpt for pneumatic trail"
    )
    QCZ1: float = Field(
        #default = read_in_values("QCZ1", tir_file),
        description="Shape factor Cpt for pneumatic trail"
    )
    QDZ1: float = Field(
        #default = read_in_values("QDZ1", tir_file),
        description="Peak trail Dpt = Dpt*(Fz/Fznom*R0)"
    )
    QDZ2: float = Field(
        #default = read_in_values("QDZ2", tir_file),
        description="Variation of peak Dpt with load"
    )
    QDZ3: float = Field(
        #default = read_in_values("QDZ3", tir_file),
        description="Variation of peak Dpt with camber"
    )
    QDZ4: float = Field(
        #default = read_in_values("QDZ4", tir_file),
        description="Variation of peak Dpt with camber squared"
    )
    QDZ6: float = Field(
        #default = read_in_values("QDZ6", tir_file),
        description="Peak residual torque Dmr = Dmr/(Fz*R0)"
    )
    QDZ7: float = Field(
        #default = read_in_values("QDZ7", tir_file),
        description="Variation of peak factor Dmr with load"
    )
    QDZ8: float = Field(
        #default = read_in_values("QDZ8", tir_file),
        description="Variation of peak factor Dmr with camber"
    )
    QDZ9: float = Field(
        #default = read_in_values("QDZ9", tir_file),
        description="Variation of peak factor Dmr with camber and load"
    )
    QDZ10: float = Field(
        #default = read_in_values("QDZ10", tir_file),
        description="Variation of peak factor Dmr with camber squared"
    )
    QDZ11: float = Field(
        #default = read_in_values("QDZ11", tir_file),
        description="Variation of Dmr with camber squared and load"
    )
    QEZ1: float = Field(
        #default = read_in_values("QEZ1", tir_file),
        description="Trail curvature Ept at Fznom"
    )
    QEZ2: float = Field(
        #default = read_in_values("QEZ2", tir_file),
        description="Variation of curvature Ept with load"
    )
    QEZ3: float = Field(
        #default = read_in_values("QEZ3", tir_file),
        description="Variation of curvature Ept with load squared"
    )
    QEZ4: float = Field(
        #default = read_in_values("QEZ4", tir_file),
        description="Variation of curvature Ept with sign of Alpha-t"
    )
    QEZ5: float = Field(
        #default = read_in_values("QEZ5", tir_file),
        description="Variation of Ept with camber and sign Alpha-t"
    )
    QHZ1: float = Field(
        #default = read_in_values("QHZ1", tir_file),
        description="Trail horizontal shift Sht at Fznom"
    )
    QHZ2: float = Field(
        #default = read_in_values("QHZ2", tir_file),
        description="Variation of shift Sht with load"
    )
    QHZ3: float = Field(
        #default = read_in_values("QHZ3", tir_file),
        description="Variation of shift Sht with camber"
    )
    QHZ4: float = Field(
        #default = read_in_values("QHZ4", tir_file),
        description="Variation of shift Sht with camber and load"
    )
    SSZ1: float = Field(
        #default = read_in_values("SSZ1", tir_file),
        description="Nominal value of s/R0: effect of Fx on Mz"
    )
    SSZ2: float = Field(
        #default = read_in_values("SSZ2", tir_file),
        description="Variation of distance s/R0 with Fy/Fznom"
    )
    SSZ3: float = Field(
        #default = read_in_values("SSZ3", tir_file),
        description="Variation of distance s/R0 with camber"
    )
    SSZ4: float = Field(
        #default = read_in_values("SSZ4", tir_file),
        description="Variation of distance s/R0 with load and camber"
    )
    PPZ1: float = Field(
        #default = read_in_values("PPZ1", tir_file),
        description="Linear pressure effect on pneumatic trail"
    )
    PPZ2: float = Field(
        #default = read_in_values("PPZ2", tir_file),
        description="Influence of inflation pressure on residual aligning torque"
    )

    # ---------------------------#
    # TURNSLIP COEFFICIENTS      #
    # ---------------------------#
    
    PDXP1: float = Field(
        #default = read_in_values("PDXP1", tir_file),
        description="Peak Fx reduction due to spin parameter"
    )
    PDXP2: float = Field(
        #default = read_in_values("PDXP2", tir_file),
        description="Peak Fx reduction due to spin with vary ing load parameter"
    )
    PDXP3: float = Field(
        #default = read_in_values("PDXP3", tir_file),
        description="Peak Fx reduction due to spin with kappa parameter"
    )
    PKYP1: float = Field(
        #default = read_in_values("PKYP1", tir_file),
        description="Cornering stiffness reduction due to spin"
    )
    PDYP1: float = Field(
        #default = read_in_values("PDYP1", tir_file),
        description="Peak Fy reduction due to spin parameter"
    )
    PDYP2: float = Field(
        #default = read_in_values("PDYP2", tir_file),
        description="Peak Fy reduction due to spin with varying load parameter"
    )
    PDYP3: float = Field(
        #default = read_in_values("PDYP3", tir_file),
        description="Peak Fy reduction due to spin with alpha parameter"
    )
    PDYP4: float = Field(
        #default = read_in_values("PDYP4", tir_file),
        description="Peak Fy reduction due to square root of spin parameter"
    )
    PHYP1: float = Field(
        #default = read_in_values("PHYP1", tir_file),
        description="Fy -alpha curve lateral shift limitation"
    )
    PHYP2: float = Field(
        #default = read_in_values("PHYP2", tir_file),
        description="Fy -alpha curve maximum lateral shift parameter"
    )
    PHYP3: float = Field(
        #default = read_in_values("PHYP3", tir_file),
        description="Fy -alpha curve maximum lateral shift varying with load parameter"
    )
    PHYP4: float = Field(
        #default = read_in_values("PHYP4", tir_file),
        description="Fy -alpha curve maximum lateral shift parameter"
    )
    PECP1: float = Field(
        #default = read_in_values("PECP1", tir_file),
        description="Camber w.r.t. spin reduction factor parameter in camber stiffness"
    )
    PECP2: float = Field(
        #default = read_in_values("PECP2", tir_file),
        description="Camber w.r.t. spin reduction factor varying with load parameter in camber stiffness"
    )
    QDTP1: float = Field(
        #default = read_in_values("QDTP1", tir_file),
        description="Pneumatic trail reduction factor due to turn slip parameter"
    )
    QCRP1: float = Field(
        #default = read_in_values("QCRP1", tir_file),
        description="Turning moment at constant turning and zero forward speed parameter"
    )
    QCRP2: float = Field(
        #default = read_in_values("QCRP2", tir_file),
        description="Turn slip moment (at alpha=90deg) parameter for increase with spin"
    )
    QBRP1: float = Field(
        #default = read_in_values("QBRP1", tir_file),
        description="Residual (spin) torque reduction factor parameter due to side slip"
    )
    QDRP1: float = Field(
        #default = read_in_values("QDRP1", tir_file),
        description="Turn slip moment peak magnitude parameter"
    )

    # --------------#
    # Functions     #
    # --------------#

    def calc_fx0(self, longslip, fz, pressure, inclangl) -> 'Fx0':

        ''' Calculate the fx0.
        
        Parameters:
        - MF62tire (class): data on tires from tir file
        - longslip (float): longitudinal slip of the tire 
        - fz (float): forces acting in the z direction [N]
        - pressure (float): Tire Pressure [kg]
        - inclangl (float): incline angle [degrees]

        Returns:
        - float: fx0 '''

        # 4.E1, 4.E2a
        fzO = self.FNOMIN*self.LFZO
        dfz = (fz-fzO)/fzO

        # 4.#2b
        piO = self.NONPRES
        dpi = (pressure-piO)/piO

        # 4.E11
        cx = self.PCXI*self.LCX

        # 4.E13
        mux = self.LMUX*(self.PDX1 + self.PDX2)*(1+self.PPX3*dpi+self.PPX4*dpi**2)*(1-self.PDX3*inclangl**2)

        # 4.E12
        dx = mux*fz*self.ZETA1

        # 4.E17
        shx = self.LHX*(self.PHX1+self.PHX2*dfz)

        # 4.E8
        amu = 10 # FROM MATLAB CODE
        lmux = amu*self.LMUX/(1+(amu-1)*self.LMUX)

        # 4.E18
        sVx = self.ZETA1*lmux*fz*(self.PVX1+self.PVX2*dfz)

        # 4.E10
        kappax = longslip + shx
        kappaxSgn = np.sign(kappax)

        # 4.E14
        ex = self.LEX*(self.PEX1+self.PEX2*dfz+self.PEX3*dfz**2)*(1-self.PEX4*kappaxSgn)

        # 4.E15
        kxk = self.LKX*fz*(self.PKX1+self.PKX2)*(np.exp(self.PKX3*dfz))*(1+self.PPX1*dpi+self.PPX2*dpi**2)

        # 4.E16
        eps_Kxk = np.finfo(float).eps*np.maximum(1,np.abs(kxk))
        bx = kxk/(cx * dx + eps_Kxk)

        # (4.E9)
        Fx0 = dx*np.sin(cx*np.arctan(bx*kappax-ex*(bx*kappax-np.arctan(bx*kappax))))+sVx

        return Fx0
    
    def calc_fy0(self, slipangl, fz, pressure, inclangl) -> 'Fy0': 

        """
        Calculate the fy0.
        
        Parameters:
        - MF62tire (class): data on tires from tir file
        - longslip (float): longitudinal slip of the tire 
        - fz (float): forces acting in the z direction [N]
        - pressure (float): Tire Pressure [kg]
        - inclangl (float): incline angle [degrees]

        Returns:
        - float: fy0
        
        """

        # 4.E4
        gammaAst = np.sin(inclangl)
        gammaAst2 = gammaAst**2

        # 4.E1 and 4.E2a
        fzO = MF62tire.FNOMIN*MF62tire.LFZO
        dfz = (fz-fzO)/fzO

        # 4.E2B
        piO = MF62tire.NOMPRES
        dpi = (pressure-piO)/piO
        dpi2 = dpi**2

        # 4.E21
        cy = MF62tire.LCY*MF62tire.PCY1

        # 4.E23
        muy = (MF62tire.PDY1+MF62tire.PDY2*dfz)*(1+MF62tire.PPY3*dpi+MF62tire.PPY4*dpi2)

        # 4.E22
        dy = muy*fz*MF62tire.ZETA2

        # 4.E25
        kya = (MF62tire.PKY1*fzO*(1+MF62tire.PPY1*dpi)*(1-MF62tire.PKY3*np.abs(gammaAst))*np.sin(MF62tire.PKY4*np.arctan(fz/fzO/((MF62tire.PKY2+MF62tire.PKY5*gammaAst2)*(1+MF62tire.PPY2*dpi))))*MF62tire.LKY*MF62tire.ZETA3)

        # 4.E39
        signKya = np.sign(kya)
        signKya[signKya == 0] =1
        kya_ = kya + np.finfo(float).eps*signKya

        # 4.E28
        svyg = MF62tire.ZETA2*MF62tire.LKYC*MF62tire.LMUY*fz*(MF62tire.PVY3+MF62tire.PVY4*dfz)*gammaAst

        # 4.E30
        kygO = fz*(MF62tire.PKY6+MF62tire.PKY7*dfz)*(1+MF62tire.PPY5*dpi)*MF62tire.LKYC

        # 4.E29
        svy = MF62tire.ZETA2*MF62tire.LMUY*MF62tire.LVY*fz*(MF62tire.PVY1+MF62tire.PVY2)+svyg

        # 4.E27
        shy = MF62tire.LHY*(MF62tire.PHY1+MF62tire.PHY2*dfz)+(kygO*gammaAst-svyg)/kya_*MF62tire.ZETA0+MF62tire.ZETA4-1

        # 4.20
        alphay = slipangl+shy
        alphaySgn = np.sign(slipangl)

        # 4.E24
        ey = (MF62tire.PEY1+MF62tire.PEY2*dfz)*(1+MF62tire.PEY5*gammaAst**2-(MF62tire.PEY3+MF62tire.PEY4*gammaAst)*alphaySgn)*MF62tire.LEY

        # 4.E26
        signCy= np.sign(cy)
        signCy[signCy == 0] = 1
        by = kya/(cy*dy+np.finfo(float).eps*signCy)

        # 4.E19
        Fy0 = dy*np.sin(cy*np.arctan(by*alphay-ey*(by*alphay-np.arctan(by*alphay))))+svy

        return Fy0
    
    def calc_mz0(self, slipangl, fz, pressure, inclangl, vcx)-> 'mz0':

        """
        Calculate the mz0.
        
        Parameters:
        - MF62tire (class): data on tires from tir file
        - longslip (float): longitudinal slip of the tire 
        - fz (float): forces acting in the z direction [N]
        - pressure (float): Tire Pressure [kg]
        - inclangl (float): incline angle [degrees]
        - vcxm(float):

        Returns:
        - float: mz0
        
        """

        # 4.E1 and 4.E2a
        fzO = MF62tire.FNOMIN*MF62tire.LFZO
        dfz = (fz-fzO)/fzO

        # 4.E2B
        piO = MF62tire.NOMPRES
        dpi = (pressure-piO)/piO

        # 4.E2B
        piO = MF62tire.NOMPRES
        dpi = (pressure-piO)/piO
        dpi2 = dpi**2

        # 4.E21
        cy = MF62tire.LCY*MF62tire.PCY1
        
        # 4.E3
        vcy = -vcx*np.tan(slipangl)
        sgnVcx = np.sign(vcx)
        alphaAst = np.tan(slipangl)*sgnVcx

        # 4.E6a
        vc = np.sqrt(vcx**2+vcy**2)
        vc = vc+np.finfo(float).eps

        # 4.E6
        alphaCos = vcx/vc

        # 4.E4
        gammaAst = np.sin(inclangl)
        gammaAst2 = gammaAst**2
        gammaAstAbs = np.abs(gammaAst)

        # 4.E25
        kya = (MF62tire.PKY1*fzO*(1+MF62tire.PPY1*dpi)*(1-MF62tire.PKY3*np.abs(gammaAst))*np.sin(MF62tire.PKY4*np.arctan(fz/fzO/((MF62tire.PKY2+MF62tire.PKY5*gammaAst2)*(1+MF62tire.PPY2*dpi))))*MF62tire.LKY*MF62tire.ZETA3)

        # 4.E23
        muy = (MF62tire.PDY1+MF62tire.PDY2*dfz)*(1+MF62tire.PPY3*dpi+MF62tire.PPY4*dpi2)

        # 4.E22
        dy = muy*fz*MF62tire.ZETA2

        # 4.E26
        signCy= np.sign(cy)
        signCy[signCy == 0] = 1
        by = kya/(cy*dy+np.finfo(float).eps*signCy)

        # 4.E28
        svyg = MF62tire.ZETA2*MF62tire.LKYC*MF62tire.LMUY*fz*(MF62tire.PVY3+MF62tire.PVY4*dfz)*gammaAst

        # 4.E30
        kygO = fz*(MF62tire.PKY6+MF62tire.PKY7*dfz)*(1+MF62tire.PPY5*dpi)*MF62tire.LKYC

        # 4.E29
        svy = MF62tire.ZETA2*MF62tire.LMUY*MF62tire.LVY*fz*(MF62tire.PVY1+MF62tire.PVY2)+svyg

        # 4.E27
        shy = MF62tire.LHY*(MF62tire.PHY1+MF62tire.PHY2*dfz)+(kygO*gammaAst-svyg)/kya_*MF62tire.ZETA0+MF62tire.ZETA4-1

        # 4.E39
        signKya = np.sign(kya)
        signKya[signKya == 0] =1
        kya_ = kya + np.finfo(float).eps*signKya
        
        dfz2 = dfz**2
        rO = MF62tire.UNLOADED_RADIUS

        # 4.E35
        shf = shy+svy/kya

        # 4.E35
        sht = MF62tire.QHZ1 + MF62tire.QHZ2*dfz + (MF62tire.QHZ3 + MF62tire.QHZ4*dfz)*gammaAst

        # 4.E34
        alphat = alphaAst+sht

        # 4.E37
        alphar = alphaAst+shf

        # 4.E42
        dtO = fz*(rO/fzO)*(MF62tire.QDZ1+MF62tire.QDZ2*dfz)*(1-MF62tire.PPZ1*dpi)*MF62tire.LTR*sgnVcx

        # 4.E40
        bt = (MF62tire.QBZ1+MF62tire.QBZ2*dfz+MF62tire.QBZ3*dfz2)*(1+MF62tire.QBZ4*gammaAst+MF62tire.QBZ5*gammaAstAbs)*MF62tire.LKY/MF62tire.LMUY

        # 4.E41
        ct = MF62tire.QCZ1

        # 4.E43
        dt = dtO*(1+MF62tire.QDZ3*gammaAstAbs+MF62tire.QDZ4*gammaAst2*MF62tire.ZETA5)

        # 4.E44
        et = (MF62tire.QEZ1+MF62tire.QEZ2*dfz+MF62tire.QEZ3*dfz2)

        # 4.E45
        br = (MF62tire.QBZ9*MF62tire.LKY/MF62tire.LMUY+MF62tire.QBZ10*by*cy)*MF62tire.ZETA6

        # 4.E46
        cr = MF62tire.ZETA7

        # 4.E47
        dr = fz*rO*((MF62tire.QDZ6+MF62tire.QD27*dfz)*MF62tire.LRES*MF62tire.ZETA2 + ((MF62tire.QDZ8+MF62tire.QDZ9*dfz)*(1+MF62tire.PPZ2*dpi)+(MF62tire.QDZ10+MF62tire.QDZ11*dfz)*gammaAstAbs)*gammaAst*MF62tire.LKZC*MF62tire.ZETA0)*MF62tire.LMUY*sgnVcx*alphaCos+MF62tire.ZETA8-1

        # 4.E33
        tO = dt*np.cos(ct*np.arctan(bt*alphat-et*(bt*alphat-np.arctan(bt*alphat))))*alphaCos

        # 4.E32
        fy0 = self.calc_fy0(MF62tire, slipangl, fz, pressure, inclangl)
        mzO_ = -tO*fy0
        mzrO = dr*np.cos(cr*np.arctan(br*alphar))*alphaCos
        mz0 = mzO_ + mzrO

        return mz0

    @classmethod
    def from_tir_file(cls, file_path: Path) -> 'MF62tire':
        data = {}

        with file_path.open('r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                elif line.startswith(("$", "[", " ")):
                    continue
                else:
                    try:
                        key, value = [item.strip() for item in line.split('=', 1)]
                        value = value.split()[0].strip("'")
                        if key in MF62tire.__annotations__:
                            field_type = MF62tire.__annotations__[key]
                        if field_type == float:
                            value = float(value)
                        elif field_type == int:
                            value = int(value)
                        elif field_type == str:
                            value = str(value)
                        value = field_type(value)
                        data[key] = value
                    except ValueError as e:
                        print(f"Skiped {line} of tir file for {e}")

        return MF62tire(**data)
                    

if __name__ == "__main__":
    file_path = Path(__file__).parent / 'vehicle_configs' / 'TireData' / 'vehicle_configs/TireData/16x6_10_LCO_10 PSI (Inaccurate My Fx and Combined Load).tir'
    file_path = (
        Path(__file__).parent.parent.parent.parent.parent.parent
        / "vehicle_configs"
        / "TireData"
        / "16x6_10_LCO_10 PSI (Inaccurate My Fx and Combined Load).tir"
    )
    fz = 1300
    slipangl = 0
    inclangl = 0
    longslip = 0.1
    pressure = 68947
    vcx = 20

    
    tire1 = MF62tire.from_tir_file(file_path)
    tire1.calc_mz0(slipangl, fz, pressure, inclangl, vcx)

