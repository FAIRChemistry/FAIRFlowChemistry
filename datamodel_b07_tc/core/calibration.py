import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
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
        description="Recorded peak areas of the individual calibration solutions.",
        default_factory=Data,
    )

    concentrations: Optional[Data] = Field(
        description="concentrations of the individual calibration solutions.",
        default_factory=Data,
    )

    regression_coefficients: List[float] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Polynomial coefficients in order of increasing degree.",
    )

    degree: Optional[int] = Field(
        default=1,
        description="Degree of regression model.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="e71182674108fd2e5c98cc34924822982a11ad53"
    )
