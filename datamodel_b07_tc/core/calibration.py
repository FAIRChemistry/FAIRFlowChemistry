import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import Enum

from .data import Data


@forge_signature
class Calibration(sdRDM.DataModel):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("calibrationINDEX"),
        xml="@id",
    )

    peak_area: List[Data] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Recorded peak areas of the individual calibration solutions.",
    )

    concentration: List[Data] = Field(
        default_factory=ListPlus,
        multiple=True,
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
        default="15c1628100dadc5d2ce53ff72a02f247fae78748"
    )

    def add_to_peak_area(
        self,
        values: List[float] = ListPlus(),
        unit: Optional[Enum] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Data' to attribute peak_area

        Args:
            id (str): Unique identifier of the 'Data' object. Defaults to 'None'.
            values (): values.. Defaults to ListPlus()
            unit (): unit of the values.. Defaults to None
        """

        params = {
            "values": values,
            "unit": unit,
        }

        if id is not None:
            params["id"] = id

        self.peak_area.append(Data(**params))

    def add_to_concentration(
        self,
        values: List[float] = ListPlus(),
        unit: Optional[Enum] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Data' to attribute concentration

        Args:
            id (str): Unique identifier of the 'Data' object. Defaults to 'None'.
            values (): values.. Defaults to ListPlus()
            unit (): unit of the values.. Defaults to None
        """

        params = {
            "values": values,
            "unit": unit,
        }

        if id is not None:
            params["id"] = id

        self.concentration.append(Data(**params))
