import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .species import Species
from .data import Data


@forge_signature
class Calibration(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("calibrationINDEX"),
        xml="@id",
    )

    species: Optional[Species] = Field(
        default=None,
        description="Species for which the calibration was performed.",
    )

    peak_area: Optional[Data] = Field(
        default=None,
        description="Recorded peak areas of the individual calibration solutions.",
    )

    concentration: Optional[Data] = Field(
        default=None,
        description="concentrations of the individual calibration solutions.",
    )

    slope: Optional[Data] = Field(
        default=None,
        description="slopes of the (linear) calibration functions.",
    )

    intercept: Optional[Data] = Field(
        default=None,
        description="intercept of the (linear) calibration functions.",
    )

    coefficient_of_determination: Optional[Data] = Field(
        default=None,
        description="coefficients of the (linear) calibration functions.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8e4370241518412c2367c002d43b1b3cd021ab9e"
    )
