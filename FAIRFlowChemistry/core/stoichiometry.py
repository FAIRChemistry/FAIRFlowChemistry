import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Stoichiometry(sdRDM.DataModel):
    """Stoichiometric information about the compound."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("stoichiometryINDEX"),
        xml="@id",
    )

    equivalents: Optional[float] = Field(
        default=None,
        description="used equivalents in relation to the reference compound",
    )

    amount_of_substance: Optional[float] = Field(
        default=None,
        description="amount of substance n in mmol",
    )

    mass: Optional[float] = Field(
        default=None,
        description="used mass of the compound in g",
    )

    volume: Optional[float] = Field(
        default=None,
        description="volume of the compound",
    )

    density: Optional[float] = Field(
        default=None,
        description="density of the compound at standard temperature and pressure.",
    )

    molar_mass: Optional[float] = Field(
        default=None,
        description="molar mass of the compound in g per mol",
    )

    mass_concentration: Optional[float] = Field(
        default=None,
        description="mass concentration in percent.",
    )

    molar_concentration: Optional[float] = Field(
        default=None,
        description="molar concentration in mol per l.",
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="ef81b78015477a06bc88e5dd78879b337a8d9c2e"
    )