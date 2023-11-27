import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class RelatedPublication(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("relatedpublicationINDEX"),
        xml="@id",
    )

    citation: Optional[str] = Field(
        default=None,
        description="The full bibliographic citation for this related publication.",
    )

    id_type: Optional[str] = Field(
        default=None,
        description=(
            "The type of digital identifier used for this publication (e.g., Digital"
            " Object Identifier (DOI))."
        ),
    )

    id_number: Optional[str] = Field(
        default=None,
        description="'The identifier for the selected ID type.'",
    )

    url: Optional[str] = Field(
        default=None,
        description=(
            "'Link to the publication web page (e.g., journal article page, archive"
            " record page, or other)."
        ),
    )