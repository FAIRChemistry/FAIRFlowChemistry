import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .stoichiometry import Stoichiometry
from .reactantrole import ReactantRole


@forge_signature
class Chemical(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("chemicalINDEX"),
        xml="@id",
    )

    name: List[str] = Field(
        description="IUPAC name of the compound.",
        default_factory=ListPlus,
        multiple=True,
    )

    formula: Optional[str] = Field(
        default=None,
        description="molecular formula of the compound.",
    )

    pureness: Optional[float] = Field(
        default=None,
        description="pureness of the compound in percent.",
    )

    supplier: Optional[str] = Field(
        default=None,
        description="name of the supplier of the compound.",
    )

    stoichiometry: Optional[Stoichiometry] = Field(
        description=(
            "stoichiometric information like equivalents, mass, amount of substance,"
            " volume"
        ),
        default_factory=Stoichiometry,
    )

    state_of_matter: Optional[str] = Field(
        default=None,
        description="s for solid, l for liquid and g for gaseous",
    )

    reactant_role: Optional[ReactantRole] = Field(
        default=None,
        description=(
            "Role that a reactand plays in a chemical reaction or  in a process."
        ),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="ef81b78015477a06bc88e5dd78879b337a8d9c2e"
    )