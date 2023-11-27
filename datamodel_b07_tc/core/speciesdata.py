import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .species import Species
from .data import Data
from .calibration import Calibration
from .chemicalformula import ChemicalFormula


@forge_signature
class SpeciesData(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("speciesdataINDEX"),
        xml="@id",
    )

    species: Optional[Species] = Field(
        default=None,
        description="name of the species.",
    )

    chemical_formula: Optional[ChemicalFormula] = Field(
        default=None,
        description="chemical formula of the species.",
    )

    calibration: Optional[Calibration] = Field(
        description="calibration measurement.",
        default_factory=Calibration,
    )

    correction_factor: Optional[float] = Field(
        default=None,
        description="correction factors of the individual species.",
    )

    faraday_coefficient: Optional[float] = Field(
        default=None,
        description="Faraday coefficients of the individual species.",
    )

    faraday_efficiency: Optional[Data] = Field(
        description="Faraday efficiencies of the individual species.",
        default_factory=Data,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="070599e978c8238372001dca8e14ed973e5f44bb"
    )
