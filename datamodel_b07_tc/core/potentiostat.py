
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .metadata import Metadata
from .measurement import Measurement
from .device import Device


@forge_signature
class Potentiostat(Device):

    """"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("potentiostatINDEX"),
        xml="@id",
    )

    measurement: Optional[Measurement] = Field(
        default=None,
        description="Measuring Data.",
    )

    metadata: Optional[Metadata] = Field(
        default=None,
        description="Metadata of the Potentiostat.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0c60f2b0a6c35d66c401c995ad1e9a5a8c126b0f"
    )