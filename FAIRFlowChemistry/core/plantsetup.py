import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from uuid import uuid4
from pydantic_xml import attr, element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .componenttype import ComponentType
from .component import Component


@forge_signature
class PlantSetup(sdRDM.DataModel):
    """"""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    component: List[Component] = element(
        description="bla.",
        default_factory=ListPlus,
        tag="component",
        json_schema_extra=dict(multiple=True),
    )

    input: List[str] = element(
        description="bla.",
        default_factory=ListPlus,
        tag="input",
        json_schema_extra=dict(multiple=True),
    )

    output: List[str] = element(
        description="bla.",
        default_factory=ListPlus,
        tag="output",
        json_schema_extra=dict(multiple=True),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/FAIRFlowChemistry"
    )
    _commit: Optional[str] = PrivateAttr(
        default="661158ab273ced2873569935234d707a9dc65a53"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self

    def add_to_component(
        self,
        component_type: Optional[ComponentType] = None,
        id: Optional[str] = None,
        component_class: Optional[str] = None,
        component_class_uri: Optional[str] = None,
        component_name: Optional[str] = None,
        generic_attribute: List[str] = ListPlus(),
        connections: List[str] = ListPlus(),
        id: Optional[str] = None,
    ) -> Component:
        """
        This method adds an object of type 'Component' to attribute component

        Args:
            id (str): Unique identifier of the 'Component' object. Defaults to 'None'.
            component_type (): equipment or piping component.. Defaults to None
            id (): id used to unambiguously identify the component.. Defaults to None
            component_class (): class of the component.. Defaults to None
            component_class_uri (): uri of the component.. Defaults to None
            component_name (): name of the component used to link between the abstract component and its shape.. Defaults to None
            generic_attribute (): a generic attribute as defined by DEXPI.. Defaults to ListPlus()
            connections (): other component this component is connected to via pipes, wires or similar.. Defaults to ListPlus()
        """
        params = {
            "component_type": component_type,
            "id": id,
            "component_class": component_class,
            "component_class_uri": component_class_uri,
            "component_name": component_name,
            "generic_attribute": generic_attribute,
            "connections": connections,
        }
        if id is not None:
            params["id"] = id
        self.component.append(Component(**params))
        return self.component[-1]
