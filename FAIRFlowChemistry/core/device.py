import sdRDM

from typing import Optional
from pydantic import Field
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Device(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("deviceINDEX"),
        xml="@id",
    )

    manufacturer: Optional[str] = Field(
        default=None,
        description="name of the manufacturer of the device.",
    )

    device_type: Optional[str] = Field(
        default=None,
        description="type given by the manufacturer of the device.",
    )

    series: Optional[str] = Field(
        default=None,
        description="the series of the device.",
    )

    on_off: Optional[bool] = Field(
        default=None,
        description="operational mode of the flow module. True is on and False is off.",
    )