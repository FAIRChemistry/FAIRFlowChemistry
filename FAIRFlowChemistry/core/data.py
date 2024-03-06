import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.base.datatypes import Unit
from datetime import datetime as Datetime
from .quantity import Quantity


@forge_signature
class Data(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/FAIRChemistry/FAIRFlowChemistry@c41a0c1e08586e8cb4deff5d7a6e8b76d1e12ca7#Data"
    },
):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    quantity: Optional[Quantity] = element(
        description="quantity of a value.",
        default=None,
        tag="quantity",
        json_schema_extra=dict(),
    )

    values: List[Union[float, str, Datetime]] = wrapped(
        "values",
        element(
            description="values.",
            default_factory=ListPlus,
            tag="float",
            json_schema_extra=dict(multiple=True),
        ),
    )

    unit: Optional[Unit] = element(
        description="unit of the values.",
        default=None,
        tag="unit",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="c41a0c1e08586e8cb4deff5d7a6e8b76d1e12ca7"
    )
