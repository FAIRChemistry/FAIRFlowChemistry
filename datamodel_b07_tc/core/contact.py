import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Contact(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("contactINDEX"),
        xml="@id",
    )

    name: Optional[str] = Field(
        default=None,
        description="full name including given and family name.",
    )

    affiliation: Optional[str] = Field(
        default=None,
        description="organization the author is affiliated to.",
    )

    email: Optional[str] = Field(
        default=None,
        description="The e-mail address of the contact for the Dataset",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="aaa02c13eb4aa0bc5b011edd3375aa60ea3c8955"
    )
