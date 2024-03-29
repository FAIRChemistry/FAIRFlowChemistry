import sdRDM

import numpy as np
from typing import List, Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from .data import Data


@forge_signature
class Calibration(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/FAIRChemistry/FAIRFlowChemistry@3206d61a7ef1fb8aaa8971863b6ab25925c3e134#Calibration"
    },
):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    peak_areas: Optional[Data] = element(
        description="Recorded peak areas of the individual calibration solutions.",
        default_factory=Data,
        tag="peak_areas",
        json_schema_extra=dict(),
    )

    concentrations: Optional[Data] = element(
        description="concentrations of the individual calibration solutions.",
        default_factory=Data,
        tag="concentrations",
        json_schema_extra=dict(),
    )

    regression_coefficients: List[float] = wrapped(
        "regression_coefficients",
        element(
            description="Polynomial coefficients in order of increasing degree.",
            default_factory=ListPlus,
            tag="float",
            json_schema_extra=dict(multiple=True),
        ),
    )

    degree: Optional[int] = element(
        description="Degree of regression model.",
        default=1,
        tag="degree",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="3206d61a7ef1fb8aaa8971863b6ab25925c3e134"
    )

    def calibrate(self):
        """
        Calibrate the regression model on seen data
        """

        self.regression_coefficients = np.polynomial.polynomial.polyfit(
            self.peak_areas.values, self.concentrations.values, self.degree
        ).tolist()

    def predict(self, x: list) -> np.ndarray:
        """
        Predict with regression model

        Args:
            x (1D list): New locations for which predictions should be made

        Returns:
           (1D numpy array): Predicted data at new locations
        """

        return np.polynomial.Polynomial(self.regression_coefficients)(np.array(x))
