import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from .calibration import Calibration
from .data import Data


@forge_signature
class SpeciesData(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/FAIRChemistry/FAIRFlowChemistry@1bb5f3b4519dae01439e0005d07224bae46e1d13#SpeciesData"
    },
):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    species: Optional[str] = element(
        description="name of the species.",
        default=None,
        tag="species",
        json_schema_extra=dict(),
    )

    chemical_formula: Optional[str] = element(
        description="chemical formula of the species.",
        default=None,
        tag="chemical_formula",
        json_schema_extra=dict(),
    )

    calibration: Optional[Calibration] = element(
        description="calibration measurement.",
        default_factory=Calibration,
        tag="calibration",
        json_schema_extra=dict(),
    )

    correction_factor: Optional[float] = element(
        description="correction factors of the individual species.",
        default=None,
        tag="correction_factor",
        json_schema_extra=dict(),
    )

    electron_transfer: Optional[float] = element(
        description="Number of transfered electrons of the individual species.",
        default=None,
        tag="electron_transfer",
        json_schema_extra=dict(),
    )

    faraday_efficiency: Optional[Data] = element(
        description="Faraday efficiencies of the individual species.",
        default_factory=Data,
        tag="faraday_efficiency",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="1bb5f3b4519dae01439e0005d07224bae46e1d13"
    )
