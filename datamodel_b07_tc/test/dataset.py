import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .speciesdata import SpeciesData
from .measurement import Measurement
from .experiment import Experiment
from .generalinformation import GeneralInformation
from .plantsetup import PlantSetup


@forge_signature
class Dataset(sdRDM.DataModel):
    """"""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("datasetINDEX"),
        xml="@id",
    )

    general_information: Optional[GeneralInformation] = Field(
        default=GeneralInformation(),
        description="general data about the data model.",
    )

    experiments: List[Experiment] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="information about the individual experiment.",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/datamodel_b07_tc.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="b85d0314fec4cf3ed24720facf3bb92a91badc0b"
    )

    def add_to_experiments(
        self,
        plant_setup: Optional[PlantSetup] = None,
        measurements: List[Measurement] = ListPlus(),
        species_data: List[SpeciesData] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Experiment' to attribute experiments

        Args:
            id (str): Unique identifier of the 'Experiment' object. Defaults to 'None'.
            plant_setup (): the individual plant setup that is used in this one experiment.. Defaults to None
            measurements (): different measurements that are made within the scope of one experiment.. Defaults to ListPlus()
            species_data (): all provided and calculated data about a specific species.. Defaults to ListPlus()
        """
        params = {
            "plant_setup": plant_setup,
            "measurements": measurements,
            "species_data": species_data,
        }
        if id is not None:
            params["id"] = id
        self.experiments.append(Experiment(**params))
        return self.experiments[-1]

    def enumerate(self, object, verbose=False):
        object_list = getattr(self, object)
        object_dict = {index: object for index, object in enumerate(object_list)}
        if verbose:
            for index, object in object_dict.items():
                print(f"{index}: {object.id}")
        return object_dict