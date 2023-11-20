import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator
from .data import Data


@forge_signature
class Calibration(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("calibrationINDEX"),
        xml="@id",
    )

    peak_areas: Optional[Data] = Field(
        default=Data(),
        description="Recorded peak areas of the individual calibration solutions.",
    )

    concentrations: Optional[Data] = Field(
        default=Data(),
        description="concentrations of the individual calibration solutions.",
    )

    slope: Optional[Data] = Field(
        default=Data(),
        description="slopes of the (linear) calibration functions.",
    )

    intercept: Optional[Data] = Field(
        default=Data(),
        description="intercept of the (linear) calibration functions.",
    )

    coefficient_of_determination: Optional[Data] = Field(
        default=Data(),
        description="coefficients of the (linear) calibration functions.",
    )
