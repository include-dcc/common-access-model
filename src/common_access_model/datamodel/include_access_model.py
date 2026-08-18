# Auto generated from common_access_model.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-08T15:56:12
# Schema: common-access-model
#
# id: https://includedcc.org/common-access-model
# description: LinkML Schema for the Common Access Model
# license: MIT

from dataclasses import dataclass
from typing import Any, ClassVar, Optional, Union

from jsonasobj2 import as_dict
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, empty_list
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from rdflib import URIRef

metamodel_version = "1.7.0"
version = None

# Namespaces
DUO = CurieNamespace("DUO", "http://purl.obolibrary.org/obo/DUO_")
HP = CurieNamespace("HP", "http://purl.obolibrary.org/obo/HP_")
MONDO = CurieNamespace("MONDO", "http://purl.obolibrary.org/obo/MONDO_")
NCIT = CurieNamespace("NCIT", "http://purl.obolibrary.org/obo/NCIT_")
PATO = CurieNamespace("PATO", "http://purl.obolibrary.org/obo/PATO_")
CAM = CurieNamespace("cam", "https://includedcc.org/common-access-model/")
CDC_RACE_ETH = CurieNamespace("cdc_race_eth", "urn:oid:2.16.840.1.113883.6.238/")
HL7_NULL = CurieNamespace(
    "hl7_null", "http://terminology.hl7.org/CodeSystem/v3-NullFlavor/"
)
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace(
    "ig2_biospecimen_availability",
    "https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/",
)
IG2DAC = CurieNamespace(
    "ig2dac",
    "https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/",
)
IG2DAT = CurieNamespace(
    "ig2dat",
    "https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/",
)
IG_DOB_METHOD = CurieNamespace(
    "ig_dob_method",
    "https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/",
)
IGCONDTYPE = CurieNamespace(
    "igcondtype", "https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/"
)
LINKML = CurieNamespace("linkml", "https://w3id.org/linkml/")
MESH = CurieNamespace("mesh", "http://id.nlm.nih.gov/mesh/")
SCHEMA = CurieNamespace("schema", "http://schema.org/")
SNOMED_CT = CurieNamespace("snomed_ct", "http://snomed.info/id/")
DEFAULT_ = CAM


# Types


# Class references
class AccessPolicyAccessPolicyId(extended_str):
    pass


class StudyStudyId(extended_str):
    pass


class StudyMetadataStudyId(StudyStudyId):
    pass


class VirtualBiorepositoryVbrId(extended_str):
    pass


class DOIDoId(extended_str):
    pass


class SubjectSubjectId(extended_str):
    pass


class DemographicsSubjectId(SubjectSubjectId):
    pass


class IncludeParticipantSubjectId(DemographicsSubjectId):
    pass


class FamilyFamilyId(extended_str):
    pass


class FamilyRelationshipFamilyRelationshipId(extended_str):
    pass


class SubjectAssertionAssertionId(extended_str):
    pass


class ConceptConceptCurie(URIorCURIE):
    pass


class SampleSampleId(extended_str):
    pass


class BiospecimenCollectionBiospecimenCollectionId(extended_str):
    pass


class AliquotAliquotId(extended_str):
    pass


class EncounterEncounterId(extended_str):
    pass


class EncounterDefinitionEncounterDefinitionId(extended_str):
    pass


class ActivityDefinitionActivityDefinitionId(extended_str):
    pass


class FileFileId(extended_str):
    pass


class DatasetDatasetId(extended_str):
    pass


@dataclass(repr=False)
class Record(YAMLRoot):
    """
    One row / entity within the database
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Record"]
    class_class_curie: ClassVar[str] = "cam:Record"
    class_name: ClassVar[str] = "Record"
    class_model_uri: ClassVar[URIRef] = CAM.Record

    external_id: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    access_policy_id: Optional[Union[str, AccessPolicyAccessPolicyId]] = None
    study_id: Optional[Union[str, StudyStudyId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.external_id, list):
            self.external_id = (
                [self.external_id] if self.external_id is not None else []
            )
        self.external_id = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.external_id
        ]

        if self.access_policy_id is not None and not isinstance(
            self.access_policy_id, AccessPolicyAccessPolicyId
        ):
            self.access_policy_id = AccessPolicyAccessPolicyId(self.access_policy_id)

        if self.study_id is not None and not isinstance(self.study_id, StudyStudyId):
            self.study_id = StudyStudyId(self.study_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AccessPolicy(YAMLRoot):
    """
    The access policy that describes the controls around use of data
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["AccessPolicy"]
    class_class_curie: ClassVar[str] = "cam:AccessPolicy"
    class_name: ClassVar[str] = "AccessPolicy"
    class_model_uri: ClassVar[URIRef] = CAM.AccessPolicy

    access_policy_id: Union[str, AccessPolicyAccessPolicyId] = None
    data_use_permission: Union[str, "EnumDataUsePermission"] = None
    data_use_accession: Optional[Union[str, URIorCURIE]] = None
    data_use_modifier: Optional[Union[str, "EnumDataUseModifier"]] = None
    disease_limitation: Optional[str] = None
    access_description: Optional[str] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_policy_id):
            self.MissingRequiredField("access_policy_id")
        if not isinstance(self.access_policy_id, AccessPolicyAccessPolicyId):
            self.access_policy_id = AccessPolicyAccessPolicyId(self.access_policy_id)

        if self.data_use_accession is not None and not isinstance(
            self.data_use_accession, URIorCURIE
        ):
            self.data_use_accession = URIorCURIE(self.data_use_accession)

        if self.disease_limitation is not None and not isinstance(
            self.disease_limitation, str
        ):
            self.disease_limitation = str(self.disease_limitation)

        if self.access_description is not None and not isinstance(
            self.access_description, str
        ):
            self.access_description = str(self.access_description)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(Record):
    """
    Study Metadata
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Study"]
    class_class_curie: ClassVar[str] = "cam:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = CAM.Study

    study_id: Union[str, StudyStudyId] = None
    study_title: str = None
    study_code: str = None
    program: Union[Union[str, "EnumProgram"], list[Union[str, "EnumProgram"]]] = None
    principal_investigator: Union[
        Union[dict, "Investigator"], list[Union[dict, "Investigator"]]
    ] = None
    contact: Union[Union[dict, "Investigator"], list[Union[dict, "Investigator"]]] = (
        None
    )
    study_description: str = None
    parent_study: Optional[Union[str, StudyStudyId]] = None
    study_short_name: Optional[str] = None
    funding_source: Optional[Union[str, list[str]]] = empty_list()
    website: Optional[Union[str, URI]] = None
    publication: Optional[
        Union[Union[dict, "Publication"], list[Union[dict, "Publication"]]]
    ] = empty_list()
    acknowledgments: Optional[str] = None
    citation_statement: Optional[str] = None
    do_id: Optional[Union[str, DOIDoId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyStudyId):
            self.study_id = StudyStudyId(self.study_id)

        if self._is_empty(self.study_title):
            self.MissingRequiredField("study_title")
        if not isinstance(self.study_title, str):
            self.study_title = str(self.study_title)

        if self._is_empty(self.study_code):
            self.MissingRequiredField("study_code")
        if not isinstance(self.study_code, str):
            self.study_code = str(self.study_code)

        if self._is_empty(self.program):
            self.MissingRequiredField("program")
        if not isinstance(self.program, list):
            self.program = [self.program] if self.program is not None else []
        self.program = [
            v if isinstance(v, EnumProgram) else EnumProgram(v) for v in self.program
        ]

        if self._is_empty(self.principal_investigator):
            self.MissingRequiredField("principal_investigator")
        if not isinstance(self.principal_investigator, list):
            self.principal_investigator = (
                [self.principal_investigator]
                if self.principal_investigator is not None
                else []
            )
        self.principal_investigator = [
            v if isinstance(v, Investigator) else Investigator(**as_dict(v))
            for v in self.principal_investigator
        ]

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [
            v if isinstance(v, Investigator) else Investigator(**as_dict(v))
            for v in self.contact
        ]

        if self._is_empty(self.study_description):
            self.MissingRequiredField("study_description")
        if not isinstance(self.study_description, str):
            self.study_description = str(self.study_description)

        if self.parent_study is not None and not isinstance(
            self.parent_study, StudyStudyId
        ):
            self.parent_study = StudyStudyId(self.parent_study)

        if self.study_short_name is not None and not isinstance(
            self.study_short_name, str
        ):
            self.study_short_name = str(self.study_short_name)

        if not isinstance(self.funding_source, list):
            self.funding_source = (
                [self.funding_source] if self.funding_source is not None else []
            )
        self.funding_source = [
            v if isinstance(v, str) else str(v) for v in self.funding_source
        ]

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if not isinstance(self.publication, list):
            self.publication = (
                [self.publication] if self.publication is not None else []
            )
        self.publication = [
            v if isinstance(v, Publication) else Publication(**as_dict(v))
            for v in self.publication
        ]

        if self.acknowledgments is not None and not isinstance(
            self.acknowledgments, str
        ):
            self.acknowledgments = str(self.acknowledgments)

        if self.citation_statement is not None and not isinstance(
            self.citation_statement, str
        ):
            self.citation_statement = str(self.citation_statement)

        if self.do_id is not None and not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyMetadata(Record):
    """
    Additional features about studies that may not apply to all studies
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["StudyMetadata"]
    class_class_curie: ClassVar[str] = "cam:StudyMetadata"
    class_name: ClassVar[str] = "StudyMetadata"
    class_model_uri: ClassVar[URIRef] = CAM.StudyMetadata

    study_id: Union[str, StudyMetadataStudyId] = None
    participant_lifespan_stage: Union[
        Union[str, "EnumParticipantLifespanStage"],
        list[Union[str, "EnumParticipantLifespanStage"]],
    ] = None
    study_design: Union[
        Union[str, "EnumStudyDesign"], list[Union[str, "EnumStudyDesign"]]
    ] = None
    clinical_data_source_type: Union[
        Union[str, "EnumClinicalDataSourceType"],
        list[Union[str, "EnumClinicalDataSourceType"]],
    ] = None
    data_category: Union[
        Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]
    ] = None
    research_domain: Union[
        Union[str, "EnumResearchDomain"], list[Union[str, "EnumResearchDomain"]]
    ] = None
    expected_number_of_participants: int = None
    actual_number_of_participants: int = None
    selection_criteria: Optional[str] = None
    vbr_id: Optional[Union[str, VirtualBiorepositoryVbrId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyMetadataStudyId):
            self.study_id = StudyMetadataStudyId(self.study_id)

        if self._is_empty(self.participant_lifespan_stage):
            self.MissingRequiredField("participant_lifespan_stage")
        if not isinstance(self.participant_lifespan_stage, list):
            self.participant_lifespan_stage = (
                [self.participant_lifespan_stage]
                if self.participant_lifespan_stage is not None
                else []
            )
        self.participant_lifespan_stage = [
            v
            if isinstance(v, EnumParticipantLifespanStage)
            else EnumParticipantLifespanStage(v)
            for v in self.participant_lifespan_stage
        ]

        if self._is_empty(self.study_design):
            self.MissingRequiredField("study_design")
        if not isinstance(self.study_design, list):
            self.study_design = (
                [self.study_design] if self.study_design is not None else []
            )
        self.study_design = [
            v if isinstance(v, EnumStudyDesign) else EnumStudyDesign(v)
            for v in self.study_design
        ]

        if self._is_empty(self.clinical_data_source_type):
            self.MissingRequiredField("clinical_data_source_type")
        if not isinstance(self.clinical_data_source_type, list):
            self.clinical_data_source_type = (
                [self.clinical_data_source_type]
                if self.clinical_data_source_type is not None
                else []
            )
        self.clinical_data_source_type = [
            v
            if isinstance(v, EnumClinicalDataSourceType)
            else EnumClinicalDataSourceType(v)
            for v in self.clinical_data_source_type
        ]

        if self._is_empty(self.data_category):
            self.MissingRequiredField("data_category")
        if not isinstance(self.data_category, list):
            self.data_category = (
                [self.data_category] if self.data_category is not None else []
            )
        self.data_category = [
            v if isinstance(v, EnumDataCategory) else EnumDataCategory(v)
            for v in self.data_category
        ]

        if self._is_empty(self.research_domain):
            self.MissingRequiredField("research_domain")
        if not isinstance(self.research_domain, list):
            self.research_domain = (
                [self.research_domain] if self.research_domain is not None else []
            )
        self.research_domain = [
            v if isinstance(v, EnumResearchDomain) else EnumResearchDomain(v)
            for v in self.research_domain
        ]

        if self._is_empty(self.expected_number_of_participants):
            self.MissingRequiredField("expected_number_of_participants")
        if not isinstance(self.expected_number_of_participants, int):
            self.expected_number_of_participants = int(
                self.expected_number_of_participants
            )

        if self._is_empty(self.actual_number_of_participants):
            self.MissingRequiredField("actual_number_of_participants")
        if not isinstance(self.actual_number_of_participants, int):
            self.actual_number_of_participants = int(self.actual_number_of_participants)

        if self.selection_criteria is not None and not isinstance(
            self.selection_criteria, str
        ):
            self.selection_criteria = str(self.selection_criteria)

        if self.vbr_id is not None and not isinstance(
            self.vbr_id, VirtualBiorepositoryVbrId
        ):
            self.vbr_id = VirtualBiorepositoryVbrId(self.vbr_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VirtualBiorepository(Record):
    """
    An organization that can provide access to specimen for further analysis.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["VirtualBiorepository"]
    class_class_curie: ClassVar[str] = "cam:VirtualBiorepository"
    class_name: ClassVar[str] = "VirtualBiorepository"
    class_model_uri: ClassVar[URIRef] = CAM.VirtualBiorepository

    vbr_id: Union[str, VirtualBiorepositoryVbrId] = None
    contact: Union[Union[dict, "Investigator"], list[Union[dict, "Investigator"]]] = (
        None
    )
    name: Optional[str] = None
    institution: Optional[str] = None
    website: Optional[Union[str, URI]] = None
    vbr_readme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vbr_id):
            self.MissingRequiredField("vbr_id")
        if not isinstance(self.vbr_id, VirtualBiorepositoryVbrId):
            self.vbr_id = VirtualBiorepositoryVbrId(self.vbr_id)

        if self._is_empty(self.contact):
            self.MissingRequiredField("contact")
        if not isinstance(self.contact, list):
            self.contact = [self.contact] if self.contact is not None else []
        self.contact = [
            v if isinstance(v, Investigator) else Investigator(**as_dict(v))
            for v in self.contact
        ]

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        if self.vbr_readme is not None and not isinstance(self.vbr_readme, str):
            self.vbr_readme = str(self.vbr_readme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DOI(Record):
    """
    A DOI is a permanent reference with metadata about a digital object.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["DOI"]
    class_class_curie: ClassVar[str] = "cam:DOI"
    class_name: ClassVar[str] = "DOI"
    class_model_uri: ClassVar[URIRef] = CAM.DOI

    do_id: Union[str, DOIDoId] = None
    bibliographic_reference: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.do_id):
            self.MissingRequiredField("do_id")
        if not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

        if self.bibliographic_reference is not None and not isinstance(
            self.bibliographic_reference, str
        ):
            self.bibliographic_reference = str(self.bibliographic_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Investigator(Record):
    """
    An individual who made contributions to the collection, analysis, or sharing of data.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Investigator"]
    class_class_curie: ClassVar[str] = "cam:Investigator"
    class_name: ClassVar[str] = "Investigator"
    class_model_uri: ClassVar[URIRef] = CAM.Investigator

    name: Optional[str] = None
    institution: Optional[str] = None
    investigator_title: Optional[str] = None
    email: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.investigator_title is not None and not isinstance(
            self.investigator_title, str
        ):
            self.investigator_title = str(self.investigator_title)

        if self.email is not None and not isinstance(self.email, str):
            self.email = str(self.email)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Publication(Record):
    """
    Information about a specific publication.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Publication"]
    class_class_curie: ClassVar[str] = "cam:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = CAM.Publication

    bibliographic_reference: Optional[str] = None
    website: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bibliographic_reference is not None and not isinstance(
            self.bibliographic_reference, str
        ):
            self.bibliographic_reference = str(self.bibliographic_reference)

        if self.website is not None and not isinstance(self.website, URI):
            self.website = URI(self.website)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subject(Record):
    """
    This entity is the subject about which data or references are recorded. This includes the idea of a human
    participant in a study, a cell line, an animal model, or any other similar entity.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Subject"]
    class_class_curie: ClassVar[str] = "cam:Subject"
    class_name: ClassVar[str] = "Subject"
    class_model_uri: ClassVar[URIRef] = CAM.Subject

    subject_id: Union[str, SubjectSubjectId] = None
    subject_type: Union[str, "EnumSubjectType"] = None
    organism_type: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self._is_empty(self.subject_type):
            self.MissingRequiredField("subject_type")
        if not isinstance(self.subject_type, EnumSubjectType):
            self.subject_type = EnumSubjectType(self.subject_type)

        if self.organism_type is not None and not isinstance(
            self.organism_type, URIorCURIE
        ):
            self.organism_type = URIorCURIE(self.organism_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Demographics(Record):
    """
    Basic participant demographics summary
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Demographics"]
    class_class_curie: ClassVar[str] = "cam:Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = CAM.Demographics

    subject_id: Union[str, DemographicsSubjectId] = None
    sex: Union[str, "EnumSex"] = None
    race: Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    age_at_last_vital_status: Optional[int] = None
    vital_status: Optional[Union[str, "EnumVitalStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, DemographicsSubjectId):
            self.subject_id = DemographicsSubjectId(self.subject_id)

        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, EnumSex):
            self.sex = EnumSex(self.sex)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, list):
            self.race = [self.race] if self.race is not None else []
        self.race = [v if isinstance(v, EnumRace) else EnumRace(v) for v in self.race]

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EnumEthnicity):
            self.ethnicity = EnumEthnicity(self.ethnicity)

        if self.age_at_last_vital_status is not None and not isinstance(
            self.age_at_last_vital_status, int
        ):
            self.age_at_last_vital_status = int(self.age_at_last_vital_status)

        if self.vital_status is not None and not isinstance(
            self.vital_status, EnumVitalStatus
        ):
            self.vital_status = EnumVitalStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IncludeParticipant(Demographics):
    """
    Information specific to INCLUDE participants
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["IncludeParticipant"]
    class_class_curie: ClassVar[str] = "cam:IncludeParticipant"
    class_name: ClassVar[str] = "IncludeParticipant"
    class_model_uri: ClassVar[URIRef] = CAM.IncludeParticipant

    subject_id: Union[str, IncludeParticipantSubjectId] = None
    sex: Union[str, "EnumSex"] = None
    race: Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]] = None
    ethnicity: Union[str, "EnumEthnicity"] = None
    down_syndrome_status: Union[str, "EnumDownSyndromeStatus"] = None
    age_at_first_engagement: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, IncludeParticipantSubjectId):
            self.subject_id = IncludeParticipantSubjectId(self.subject_id)

        if self._is_empty(self.down_syndrome_status):
            self.MissingRequiredField("down_syndrome_status")
        if not isinstance(self.down_syndrome_status, EnumDownSyndromeStatus):
            self.down_syndrome_status = EnumDownSyndromeStatus(
                self.down_syndrome_status
            )

        if self.age_at_first_engagement is not None and not isinstance(
            self.age_at_first_engagement, int
        ):
            self.age_at_first_engagement = int(self.age_at_first_engagement)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Family(Record):
    """
    A group of individuals of some relation who are grouped together in a study.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Family"]
    class_class_curie: ClassVar[str] = "cam:Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = CAM.Family

    family_id: Union[str, FamilyFamilyId] = None
    family_type: Optional[Union[str, "EnumFamilyType"]] = None
    family_description: Optional[str] = None
    consanguinity: Optional[Union[str, "EnumConsanguinityAssertion"]] = None
    family_study_focus: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_id):
            self.MissingRequiredField("family_id")
        if not isinstance(self.family_id, FamilyFamilyId):
            self.family_id = FamilyFamilyId(self.family_id)

        if self.family_type is not None and not isinstance(
            self.family_type, EnumFamilyType
        ):
            self.family_type = EnumFamilyType(self.family_type)

        if self.family_description is not None and not isinstance(
            self.family_description, str
        ):
            self.family_description = str(self.family_description)

        if self.consanguinity is not None and not isinstance(
            self.consanguinity, EnumConsanguinityAssertion
        ):
            self.consanguinity = EnumConsanguinityAssertion(self.consanguinity)

        if self.family_study_focus is not None and not isinstance(
            self.family_study_focus, URIorCURIE
        ):
            self.family_study_focus = URIorCURIE(self.family_study_focus)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyRelationship(Record):
    """
    A relationship between two Subjects. Directed as follows <family_member_id> <relationship> <subject_id> <Mother's
    id> <KIN:027 "isBiologicalMotherOf"> <subject_id>
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["FamilyRelationship"]
    class_class_curie: ClassVar[str] = "cam:FamilyRelationship"
    class_name: ClassVar[str] = "FamilyRelationship"
    class_model_uri: ClassVar[URIRef] = CAM.FamilyRelationship

    family_relationship_id: Union[str, FamilyRelationshipFamilyRelationshipId] = None
    family_member_id: Union[str, SubjectSubjectId] = None
    relationship: Union[str, URIorCURIE] = None
    subject_id: Union[str, SubjectSubjectId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_relationship_id):
            self.MissingRequiredField("family_relationship_id")
        if not isinstance(
            self.family_relationship_id, FamilyRelationshipFamilyRelationshipId
        ):
            self.family_relationship_id = FamilyRelationshipFamilyRelationshipId(
                self.family_relationship_id
            )

        if self._is_empty(self.family_member_id):
            self.MissingRequiredField("family_member_id")
        if not isinstance(self.family_member_id, SubjectSubjectId):
            self.family_member_id = SubjectSubjectId(self.family_member_id)

        if self._is_empty(self.relationship):
            self.MissingRequiredField("relationship")
        if not isinstance(self.relationship, URIorCURIE):
            self.relationship = URIorCURIE(self.relationship)

        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyMember(Record):
    """
    Designates a Subject as a member of a family with a specified role.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["FamilyMember"]
    class_class_curie: ClassVar[str] = "cam:FamilyMember"
    class_name: ClassVar[str] = "FamilyMember"
    class_model_uri: ClassVar[URIRef] = CAM.FamilyMember

    family_id: Union[str, FamilyFamilyId] = None
    subject_id: Union[str, SubjectSubjectId] = None
    family_role: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.family_id):
            self.MissingRequiredField("family_id")
        if not isinstance(self.family_id, FamilyFamilyId):
            self.family_id = FamilyFamilyId(self.family_id)

        if self._is_empty(self.subject_id):
            self.MissingRequiredField("subject_id")
        if not isinstance(self.subject_id, SubjectSubjectId):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self.family_role is not None and not isinstance(
            self.family_role, URIorCURIE
        ):
            self.family_role = URIorCURIE(self.family_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubjectAssertion(Record):
    """
    Assertion about a particular Subject. May include Conditions, Measurements, etc.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["SubjectAssertion"]
    class_class_curie: ClassVar[str] = "cam:SubjectAssertion"
    class_name: ClassVar[str] = "SubjectAssertion"
    class_model_uri: ClassVar[URIRef] = CAM.SubjectAssertion

    assertion_id: Union[str, SubjectAssertionAssertionId] = None
    subject_id: Optional[Union[str, SubjectSubjectId]] = None
    encounter_id: Optional[Union[str, EncounterEncounterId]] = None
    assertion_provenance: Optional[Union[str, "EnumAssertionProvenance"]] = None
    age_at_assertion: Optional[int] = None
    age_at_event: Optional[int] = None
    age_at_resolution: Optional[int] = None
    concept: Optional[
        Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]
    ] = empty_list()
    concept_source: Optional[str] = None
    value_concept: Optional[
        Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]
    ] = empty_list()
    value_number: Optional[float] = None
    value_source: Optional[str] = None
    value_unit: Optional[Union[str, ConceptConceptCurie]] = None
    value_unit_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.assertion_id):
            self.MissingRequiredField("assertion_id")
        if not isinstance(self.assertion_id, SubjectAssertionAssertionId):
            self.assertion_id = SubjectAssertionAssertionId(self.assertion_id)

        if self.subject_id is not None and not isinstance(
            self.subject_id, SubjectSubjectId
        ):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self.encounter_id is not None and not isinstance(
            self.encounter_id, EncounterEncounterId
        ):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        if self.assertion_provenance is not None and not isinstance(
            self.assertion_provenance, EnumAssertionProvenance
        ):
            self.assertion_provenance = EnumAssertionProvenance(
                self.assertion_provenance
            )

        if self.age_at_assertion is not None and not isinstance(
            self.age_at_assertion, int
        ):
            self.age_at_assertion = int(self.age_at_assertion)

        if self.age_at_event is not None and not isinstance(self.age_at_event, int):
            self.age_at_event = int(self.age_at_event)

        if self.age_at_resolution is not None and not isinstance(
            self.age_at_resolution, int
        ):
            self.age_at_resolution = int(self.age_at_resolution)

        if not isinstance(self.concept, list):
            self.concept = [self.concept] if self.concept is not None else []
        self.concept = [
            v if isinstance(v, ConceptConceptCurie) else ConceptConceptCurie(v)
            for v in self.concept
        ]

        if self.concept_source is not None and not isinstance(self.concept_source, str):
            self.concept_source = str(self.concept_source)

        if not isinstance(self.value_concept, list):
            self.value_concept = (
                [self.value_concept] if self.value_concept is not None else []
            )
        self.value_concept = [
            v if isinstance(v, ConceptConceptCurie) else ConceptConceptCurie(v)
            for v in self.value_concept
        ]

        if self.value_number is not None and not isinstance(self.value_number, float):
            self.value_number = float(self.value_number)

        if self.value_source is not None and not isinstance(self.value_source, str):
            self.value_source = str(self.value_source)

        if self.value_unit is not None and not isinstance(
            self.value_unit, ConceptConceptCurie
        ):
            self.value_unit = ConceptConceptCurie(self.value_unit)

        if self.value_unit_source is not None and not isinstance(
            self.value_unit_source, str
        ):
            self.value_unit_source = str(self.value_unit_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(YAMLRoot):
    """
    A standardized concept with display information.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Concept"]
    class_class_curie: ClassVar[str] = "cam:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = CAM.Concept

    concept_curie: Union[str, ConceptConceptCurie] = None
    display: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.concept_curie):
            self.MissingRequiredField("concept_curie")
        if not isinstance(self.concept_curie, ConceptConceptCurie):
            self.concept_curie = ConceptConceptCurie(self.concept_curie)

        if self.display is not None and not isinstance(self.display, str):
            self.display = str(self.display)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(Record):
    """
    A functionally equivalent specimen taken from a participant or processed from such a sample.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Sample"]
    class_class_curie: ClassVar[str] = "cam:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = CAM.Sample

    sample_id: Union[str, SampleSampleId] = None
    sample_type: Union[str, URIorCURIE] = None
    biospecimen_collection_id: Optional[
        Union[str, BiospecimenCollectionBiospecimenCollectionId]
    ] = None
    parent_sample_id: Optional[Union[str, SampleSampleId]] = None
    processing: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    availability_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    storage_method: Optional[
        Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]
    ] = empty_list()
    quantity_number: Optional[float] = None
    quantity_unit: Optional[Union[str, ConceptConceptCurie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleSampleId):
            self.sample_id = SampleSampleId(self.sample_id)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, URIorCURIE):
            self.sample_type = URIorCURIE(self.sample_type)

        if self.biospecimen_collection_id is not None and not isinstance(
            self.biospecimen_collection_id, BiospecimenCollectionBiospecimenCollectionId
        ):
            self.biospecimen_collection_id = (
                BiospecimenCollectionBiospecimenCollectionId(
                    self.biospecimen_collection_id
                )
            )

        if self.parent_sample_id is not None and not isinstance(
            self.parent_sample_id, SampleSampleId
        ):
            self.parent_sample_id = SampleSampleId(self.parent_sample_id)

        if not isinstance(self.processing, list):
            self.processing = [self.processing] if self.processing is not None else []
        self.processing = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.processing
        ]

        if self.availability_status is not None and not isinstance(
            self.availability_status, EnumAvailabilityStatus
        ):
            self.availability_status = EnumAvailabilityStatus(self.availability_status)

        if not isinstance(self.storage_method, list):
            self.storage_method = (
                [self.storage_method] if self.storage_method is not None else []
            )
        self.storage_method = [
            v if isinstance(v, URIorCURIE) else URIorCURIE(v)
            for v in self.storage_method
        ]

        if self.quantity_number is not None and not isinstance(
            self.quantity_number, float
        ):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_unit is not None and not isinstance(
            self.quantity_unit, ConceptConceptCurie
        ):
            self.quantity_unit = ConceptConceptCurie(self.quantity_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiospecimenCollection(Record):
    """
    A biospecimen collection event which yields one or more Samples.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["BiospecimenCollection"]
    class_class_curie: ClassVar[str] = "cam:BiospecimenCollection"
    class_name: ClassVar[str] = "BiospecimenCollection"
    class_model_uri: ClassVar[URIRef] = CAM.BiospecimenCollection

    biospecimen_collection_id: Union[
        str, BiospecimenCollectionBiospecimenCollectionId
    ] = None
    age_at_collection: Optional[float] = None
    method: Optional[Union[str, "EnumSampleCollectionMethod"]] = None
    site: Optional[Union[str, "EnumSite"]] = None
    spatial_qualifier: Optional[Union[str, "EnumSpatialQualifiers"]] = None
    laterality: Optional[Union[str, "EnumLaterality"]] = None
    encounter_id: Optional[Union[str, EncounterEncounterId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.biospecimen_collection_id):
            self.MissingRequiredField("biospecimen_collection_id")
        if not isinstance(
            self.biospecimen_collection_id, BiospecimenCollectionBiospecimenCollectionId
        ):
            self.biospecimen_collection_id = (
                BiospecimenCollectionBiospecimenCollectionId(
                    self.biospecimen_collection_id
                )
            )

        if self.age_at_collection is not None and not isinstance(
            self.age_at_collection, float
        ):
            self.age_at_collection = float(self.age_at_collection)

        if self.encounter_id is not None and not isinstance(
            self.encounter_id, EncounterEncounterId
        ):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Aliquot(Record):
    """
    A specific tube or amount of a biospecimen associated with a Sample.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Aliquot"]
    class_class_curie: ClassVar[str] = "cam:Aliquot"
    class_name: ClassVar[str] = "Aliquot"
    class_model_uri: ClassVar[URIRef] = CAM.Aliquot

    aliquot_id: Union[str, AliquotAliquotId] = None
    sample_id: Optional[Union[str, SampleSampleId]] = None
    availability_status: Optional[Union[str, "EnumAvailabilityStatus"]] = None
    quantity_number: Optional[float] = None
    quantity_unit: Optional[Union[str, ConceptConceptCurie]] = None
    concentration_number: Optional[float] = None
    concentration_unit: Optional[Union[str, ConceptConceptCurie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aliquot_id):
            self.MissingRequiredField("aliquot_id")
        if not isinstance(self.aliquot_id, AliquotAliquotId):
            self.aliquot_id = AliquotAliquotId(self.aliquot_id)

        if self.sample_id is not None and not isinstance(
            self.sample_id, SampleSampleId
        ):
            self.sample_id = SampleSampleId(self.sample_id)

        if self.availability_status is not None and not isinstance(
            self.availability_status, EnumAvailabilityStatus
        ):
            self.availability_status = EnumAvailabilityStatus(self.availability_status)

        if self.quantity_number is not None and not isinstance(
            self.quantity_number, float
        ):
            self.quantity_number = float(self.quantity_number)

        if self.quantity_unit is not None and not isinstance(
            self.quantity_unit, ConceptConceptCurie
        ):
            self.quantity_unit = ConceptConceptCurie(self.quantity_unit)

        if self.concentration_number is not None and not isinstance(
            self.concentration_number, float
        ):
            self.concentration_number = float(self.concentration_number)

        if self.concentration_unit is not None and not isinstance(
            self.concentration_unit, ConceptConceptCurie
        ):
            self.concentration_unit = ConceptConceptCurie(self.concentration_unit)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Encounter(Record):
    """
    An event at which data was collected about a participant, an intervention was made, or information about a
    participant was recorded.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Encounter"]
    class_class_curie: ClassVar[str] = "cam:Encounter"
    class_name: ClassVar[str] = "Encounter"
    class_model_uri: ClassVar[URIRef] = CAM.Encounter

    encounter_id: Union[str, EncounterEncounterId] = None
    subject_id: Optional[Union[str, SubjectSubjectId]] = None
    encounter_definition_id: Optional[
        Union[str, EncounterDefinitionEncounterDefinitionId]
    ] = None
    age_at_event: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.encounter_id):
            self.MissingRequiredField("encounter_id")
        if not isinstance(self.encounter_id, EncounterEncounterId):
            self.encounter_id = EncounterEncounterId(self.encounter_id)

        if self.subject_id is not None and not isinstance(
            self.subject_id, SubjectSubjectId
        ):
            self.subject_id = SubjectSubjectId(self.subject_id)

        if self.encounter_definition_id is not None and not isinstance(
            self.encounter_definition_id, EncounterDefinitionEncounterDefinitionId
        ):
            self.encounter_definition_id = EncounterDefinitionEncounterDefinitionId(
                self.encounter_definition_id
            )

        if self.age_at_event is not None and not isinstance(self.age_at_event, int):
            self.age_at_event = int(self.age_at_event)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EncounterDefinition(Record):
    """
    A definition of an encounter type in this study, ie, an event at which data was collected about a participant, an
    intervention was made, or information about a participant was recorded. This may be something planned by a study
    or a type of data collection.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["EncounterDefinition"]
    class_class_curie: ClassVar[str] = "cam:EncounterDefinition"
    class_name: ClassVar[str] = "EncounterDefinition"
    class_model_uri: ClassVar[URIRef] = CAM.EncounterDefinition

    encounter_definition_id: Union[str, EncounterDefinitionEncounterDefinitionId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    activity_definition_id: Optional[
        Union[
            Union[str, ActivityDefinitionActivityDefinitionId],
            list[Union[str, ActivityDefinitionActivityDefinitionId]],
        ]
    ] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.encounter_definition_id):
            self.MissingRequiredField("encounter_definition_id")
        if not isinstance(
            self.encounter_definition_id, EncounterDefinitionEncounterDefinitionId
        ):
            self.encounter_definition_id = EncounterDefinitionEncounterDefinitionId(
                self.encounter_definition_id
            )

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.activity_definition_id, list):
            self.activity_definition_id = (
                [self.activity_definition_id]
                if self.activity_definition_id is not None
                else []
            )
        self.activity_definition_id = [
            v
            if isinstance(v, ActivityDefinitionActivityDefinitionId)
            else ActivityDefinitionActivityDefinitionId(v)
            for v in self.activity_definition_id
        ]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityDefinition(Record):
    """
    A definition of an activity in this study, eg, a biospecimen collection, intervention, survey, or assessment.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["ActivityDefinition"]
    class_class_curie: ClassVar[str] = "cam:ActivityDefinition"
    class_name: ClassVar[str] = "ActivityDefinition"
    class_model_uri: ClassVar[URIRef] = CAM.ActivityDefinition

    activity_definition_id: Union[str, ActivityDefinitionActivityDefinitionId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.activity_definition_id):
            self.MissingRequiredField("activity_definition_id")
        if not isinstance(
            self.activity_definition_id, ActivityDefinitionActivityDefinitionId
        ):
            self.activity_definition_id = ActivityDefinitionActivityDefinitionId(
                self.activity_definition_id
            )

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(Record):
    """
    File
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["File"]
    class_class_curie: ClassVar[str] = "cam:File"
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = CAM.File

    file_id: Union[str, FileFileId] = None
    subject_id: Optional[
        Union[Union[str, SubjectSubjectId], list[Union[str, SubjectSubjectId]]]
    ] = empty_list()
    sample_id: Optional[
        Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]
    ] = empty_list()
    filename: Optional[str] = None
    format: Optional[Union[str, "EnumEDAMFormats"]] = None
    data_category: Optional[Union[str, "EnumDataCategory"]] = None
    data_type: Optional[Union[str, "EnumEDAMDataTypes"]] = None
    size: Optional[int] = None
    staging_url: Optional[Union[str, URIorCURIE]] = None
    release_url: Optional[Union[str, URIorCURIE]] = None
    drs_uri: Optional[Union[str, URIorCURIE]] = None
    hash: Optional[Union[dict, "FileHash"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, FileFileId):
            self.file_id = FileFileId(self.file_id)

        if not isinstance(self.subject_id, list):
            self.subject_id = [self.subject_id] if self.subject_id is not None else []
        self.subject_id = [
            v if isinstance(v, SubjectSubjectId) else SubjectSubjectId(v)
            for v in self.subject_id
        ]

        if not isinstance(self.sample_id, list):
            self.sample_id = [self.sample_id] if self.sample_id is not None else []
        self.sample_id = [
            v if isinstance(v, SampleSampleId) else SampleSampleId(v)
            for v in self.sample_id
        ]

        if self.filename is not None and not isinstance(self.filename, str):
            self.filename = str(self.filename)

        if self.data_category is not None and not isinstance(
            self.data_category, EnumDataCategory
        ):
            self.data_category = EnumDataCategory(self.data_category)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.staging_url is not None and not isinstance(
            self.staging_url, URIorCURIE
        ):
            self.staging_url = URIorCURIE(self.staging_url)

        if self.release_url is not None and not isinstance(
            self.release_url, URIorCURIE
        ):
            self.release_url = URIorCURIE(self.release_url)

        if self.drs_uri is not None and not isinstance(self.drs_uri, URIorCURIE):
            self.drs_uri = URIorCURIE(self.drs_uri)

        if self.hash is not None and not isinstance(self.hash, FileHash):
            self.hash = FileHash(**as_dict(self.hash))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FileHash(YAMLRoot):
    """
    Type and value of a file content hash.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["FileHash"]
    class_class_curie: ClassVar[str] = "cam:FileHash"
    class_name: ClassVar[str] = "FileHash"
    class_model_uri: ClassVar[URIRef] = CAM.FileHash

    hash_type: Optional[Union[str, "EnumFileHashType"]] = None
    hash_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.hash_type is not None and not isinstance(
            self.hash_type, EnumFileHashType
        ):
            self.hash_type = EnumFileHashType(self.hash_type)

        if self.hash_value is not None and not isinstance(self.hash_value, str):
            self.hash_value = str(self.hash_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    Set of files grouped together for release.
    """

    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["Dataset"]
    class_class_curie: ClassVar[str] = "cam:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = CAM.Dataset

    dataset_id: Union[str, DatasetDatasetId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    do_id: Optional[Union[str, DOIDoId]] = None
    file_id: Optional[Union[Union[str, FileFileId], list[Union[str, FileFileId]]]] = (
        empty_list()
    )
    publication: Optional[
        Union[Union[dict, Publication], list[Union[dict, Publication]]]
    ] = empty_list()
    data_collection_start: Optional[str] = None
    data_collection_end: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dataset_id):
            self.MissingRequiredField("dataset_id")
        if not isinstance(self.dataset_id, DatasetDatasetId):
            self.dataset_id = DatasetDatasetId(self.dataset_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.do_id is not None and not isinstance(self.do_id, DOIDoId):
            self.do_id = DOIDoId(self.do_id)

        if not isinstance(self.file_id, list):
            self.file_id = [self.file_id] if self.file_id is not None else []
        self.file_id = [
            v if isinstance(v, FileFileId) else FileFileId(v) for v in self.file_id
        ]

        if not isinstance(self.publication, list):
            self.publication = (
                [self.publication] if self.publication is not None else []
            )
        self.publication = [
            v if isinstance(v, Publication) else Publication(**as_dict(v))
            for v in self.publication
        ]

        if self.data_collection_start is not None and not isinstance(
            self.data_collection_start, str
        ):
            self.data_collection_start = str(self.data_collection_start)

        if self.data_collection_end is not None and not isinstance(
            self.data_collection_end, str
        ):
            self.data_collection_end = str(self.data_collection_end)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataUsePermission(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """

    _defn = EnumDefinition(
        name="EnumDataUsePermission",
        description="Data Use Ontology (DUO) terms for data use permissions.",
    )


class EnumDataUseModifier(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """

    _defn = EnumDefinition(
        name="EnumDataUseModifier",
        description="Data Use Ontology (DUO) terms for data use modifiers.",
    )


class EnumProgram(EnumDefinitionImpl):
    """
    Funding programs relevant to inform operations.
    """

    include = PermissibleValue(text="include", title="INCLUDE")
    kf = PermissibleValue(text="kf", title="KF")
    other = PermissibleValue(text="other", title="Other")

    _defn = EnumDefinition(
        name="EnumProgram",
        description="Funding programs relevant to inform operations.",
    )


class EnumResearchDomain(EnumDefinitionImpl):
    """
    Domains of Research used to find studies.
    """

    behavior_and_behavior_mechanisms = PermissibleValue(
        text="behavior_and_behavior_mechanisms",
        title="Behavior and Behavior Mechanisms",
        meaning=MESH["D001520"],
    )
    congenital_heart_defects = PermissibleValue(
        text="congenital_heart_defects",
        title="Congenital Heart Defects",
        meaning=MESH["D006330"],
    )
    immune_system_diseases = PermissibleValue(
        text="immune_system_diseases",
        title="Immune System Diseases",
        meaning=MESH["D007154"],
    )
    hematologic_diseases = PermissibleValue(
        text="hematologic_diseases",
        title="Hematologic Diseases",
        meaning=MESH["D006402"],
    )
    neurodevelopment = PermissibleValue(
        text="neurodevelopment", title="Neurodevelopment", meaning=MESH["D065886"]
    )
    sleep_wake_disorders = PermissibleValue(
        text="sleep_wake_disorders",
        title="Sleep Wake Disorders",
        meaning=MESH["D012893"],
    )
    all_co_occurring_conditions = PermissibleValue(
        text="all_co_occurring_conditions",
        title="All Co-occurring Conditions",
        meaning=MESH["D013568"],
    )
    physical_fitness = PermissibleValue(
        text="physical_fitness", title="Physical Fitness", meaning=MESH["D010809"]
    )
    other = PermissibleValue(text="other", title="Other")

    _defn = EnumDefinition(
        name="EnumResearchDomain",
        description="Domains of Research used to find studies.",
    )


class EnumParticipantLifespanStage(EnumDefinitionImpl):
    """
    Stages of life during which participants may be recruited.
    """

    fetal = PermissibleValue(text="fetal", title="Fetal", description="Before birth")
    neonatal = PermissibleValue(
        text="neonatal", title="Neonatal", description="0-28 days old"
    )
    pediatric = PermissibleValue(
        text="pediatric", title="Pediatric", description="Birth-17 years old"
    )
    adult = PermissibleValue(text="adult", title="Adult", description="18+ years old")

    _defn = EnumDefinition(
        name="EnumParticipantLifespanStage",
        description="Stages of life during which participants may be recruited.",
    )


class EnumStudyDesign(EnumDefinitionImpl):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """

    case_control = PermissibleValue(text="case_control", title="Case-Control")
    case_set = PermissibleValue(text="case_set", title="Case Set")
    control_set = PermissibleValue(text="control_set", title="Control Set")
    clinical_trial = PermissibleValue(text="clinical_trial", title="Clinical Trial")
    cross_sectional = PermissibleValue(text="cross_sectional", title="Cross-Sectional")
    family_twins_trios = PermissibleValue(
        text="family_twins_trios", title="Family/Twins/Trios"
    )
    interventional = PermissibleValue(text="interventional", title="Interventional")
    longitudinal = PermissibleValue(text="longitudinal", title="Longitudinal")
    trial_readiness_study = PermissibleValue(
        text="trial_readiness_study", title="Trial Readiness Study"
    )
    tumor_vs_matched_normal = PermissibleValue(
        text="tumor_vs_matched_normal", title="Tumor vs Matched Normal"
    )

    _defn = EnumDefinition(
        name="EnumStudyDesign",
        description="Approaches for collecting data, investigating interventions, and/or analyzing data.",
    )


class EnumClinicalDataSourceType(EnumDefinitionImpl):
    """
    Approaches to ascertain clinical information about a participant.
    """

    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained directly from medical record",
    )
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator",
    )
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver",
    )
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank",
    )
    unknown = PermissibleValue(text="unknown", title="Unknown")

    _defn = EnumDefinition(
        name="EnumClinicalDataSourceType",
        description="Approaches to ascertain clinical information about a participant.",
    )


class EnumDataCategory(EnumDefinitionImpl):
    """
    Categories of data which may be collected about participants.
    """

    unharmonized_demographic_clinical_data = PermissibleValue(
        text="unharmonized_demographic_clinical_data",
        title="Unharmonized Demographic/Clinical Data",
    )
    harmonized_demographic_clinical_data = PermissibleValue(
        text="harmonized_demographic_clinical_data",
        title="Harmonized Demographic/Clinical Data",
    )
    genomics = PermissibleValue(text="genomics", title="Genomics")
    transcriptomics = PermissibleValue(text="transcriptomics", title="Transcriptomics")
    epigenomics = PermissibleValue(text="epigenomics", title="Epigenomics")
    proteomics = PermissibleValue(text="proteomics", title="Proteomics")
    metabolomics = PermissibleValue(text="metabolomics", title="Metabolomics")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral", title="Cognitive/Behavioral"
    )
    immune_profiling = PermissibleValue(
        text="immune_profiling", title="Immune Profiling"
    )
    imaging = PermissibleValue(text="imaging", title="Imaging")
    microbiome = PermissibleValue(text="microbiome", title="Microbiome")
    fitness = PermissibleValue(text="fitness", title="Fitness")
    physical_activity = PermissibleValue(
        text="physical_activity", title="Physical Activity"
    )
    other = PermissibleValue(text="other", title="Other")
    sleep_study = PermissibleValue(text="sleep_study", title="Sleep Study")

    _defn = EnumDefinition(
        name="EnumDataCategory",
        description="Categories of data which may be collected about participants.",
    )


class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of Subject entities
    """

    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.",
    )
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explicitly consented, eg, the subject of a reported family history.""",
    )
    cell_line = PermissibleValue(text="cell_line", description="Cell Line")
    animal_model = PermissibleValue(text="animal_model", description="Animal model")
    group = PermissibleValue(
        text="group", description="A group of individuals or entities."
    )
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!",
    )

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of Subject entities",
    )


class EnumDownSyndromeStatus(EnumDefinitionImpl):
    """
    Down syndrome / chromosome 21 status
    """

    d21 = PermissibleValue(
        text="d21",
        title="D21",
        description="Disomy 21 (euploid)",
        meaning=PATO["0001393"],
    )
    t21 = PermissibleValue(
        text="t21",
        title="T21",
        description="Trisomy 21 (Down syndrome)",
        meaning=MONDO["0008608"],
    )

    _defn = EnumDefinition(
        name="EnumDownSyndromeStatus",
        description="Down syndrome / chromosome 21 status",
    )


class EnumSex(EnumDefinitionImpl):
    """
    Subject Sex
    """

    female = PermissibleValue(text="female", title="Female", meaning=NCIT["C16576"])
    male = PermissibleValue(text="male", title="Male", meaning=NCIT["C20197"])
    other = PermissibleValue(text="other", title="Other", meaning=NCIT["C17649"])
    unknown = PermissibleValue(text="unknown", title="Unknown", meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumSex",
        description="Subject Sex",
    )


class EnumRace(EnumDefinitionImpl):
    """
    Participant Race
    """

    american_indian_or_alaska_native = PermissibleValue(
        text="american_indian_or_alaska_native",
        title="American Indian or Alaska Native",
        meaning=NCIT["C41259"],
    )
    asian = PermissibleValue(text="asian", title="Asian", meaning=NCIT["C41260"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=NCIT["C16352"],
    )
    more_than_one_race = PermissibleValue(
        text="more_than_one_race", title="More than one race", meaning=NCIT["C67109"]
    )
    native_hawaiian_or_other_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_other_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=NCIT["C41219"],
    )
    other = PermissibleValue(text="other", title="Other", meaning=NCIT["C17649"])
    white = PermissibleValue(text="white", title="White", meaning=NCIT["C41261"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"],
    )
    unknown = PermissibleValue(text="unknown", title="Unknown", meaning=NCIT["C17998"])
    east_asian = PermissibleValue(
        text="east_asian",
        title="East Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C161419"],
    )
    latin_american = PermissibleValue(
        text="latin_american",
        title="Latin American",
        description="UK only; do not use for US data",
        meaning=NCIT["C126531"],
    )
    middle_eastern_or_north_african = PermissibleValue(
        text="middle_eastern_or_north_african",
        title="Middle Eastern or North African",
        description="UK only; do not use for US data",
        meaning=NCIT["C43866"],
    )
    south_asian = PermissibleValue(
        text="south_asian",
        title="South Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C41263"],
    )

    _defn = EnumDefinition(
        name="EnumRace",
        description="Participant Race",
    )


class EnumEthnicity(EnumDefinitionImpl):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """

    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino", title="Hispanic or Latino", meaning=NCIT["C17459"]
    )
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        title="Not Hispanic or Latino",
        meaning=NCIT["C41222"],
    )
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"],
    )
    unknown = PermissibleValue(text="unknown", title="Unknown", meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="Participant ethnicity, specific to Hispanic or Latino.",
    )


class EnumVitalStatus(EnumDefinitionImpl):
    """
    Descriptions of a Subject's vital status
    """

    dead = PermissibleValue(text="dead", title="Dead", meaning=NCIT["C28554"])
    alive = PermissibleValue(text="alive", title="Alive", meaning=NCIT["C37987"])

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Descriptions of a Subject's vital status",
    )


class EnumNull(EnumDefinitionImpl):
    """
    Base enumeration providing null options.
    """

    unknown = PermissibleValue(text="unknown", title="Unknown", meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumNull",
        description="Base enumeration providing null options.",
    )


class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """

    control_only = PermissibleValue(
        text="control_only", title="Control-only", description="Control Only"
    )
    duo = PermissibleValue(text="duo", title="Duo", description="Duo")
    proband_only = PermissibleValue(
        text="proband_only", title="Proband-only", description="Proband Only"
    )
    trio = PermissibleValue(
        text="trio", title="Trio", description="Trio (2 parents and affected child)"
    )
    trio_plus = PermissibleValue(
        text="trio_plus", title="Trio+", description="2 Parents and 2 or more children"
    )

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Enumerations describing research family type",
    )


class EnumConsanguinityAssertion(EnumDefinitionImpl):
    """
    Asserts known or suspected consanguinity in this study family
    """

    not_suspected = PermissibleValue(
        text="not_suspected",
        title="not-suspected",
        description="Not suspected",
        meaning=SNOMED_CT["428263003"],
    )
    suspected = PermissibleValue(
        text="suspected",
        title="suspected",
        description="Suspected",
        meaning=SNOMED_CT["415684004"],
    )
    known_present = PermissibleValue(
        text="known_present",
        title="known-present",
        description="Known Present",
        meaning=SNOMED_CT["410515003"],
    )
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        description="Unknown",
        meaning=SNOMED_CT["261665006"],
    )

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
    )


class EnumAssertionProvenance(EnumDefinitionImpl):
    """
    Possible data sources for assertions.
    """

    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained from a medical record",
    )
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator",
    )
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver",
    )
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank",
    )

    _defn = EnumDefinition(
        name="EnumAssertionProvenance",
        description="Possible data sources for assertions.",
    )


class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the biospecimen available for use?
    """

    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"],
    )
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"],
    )

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the biospecimen available for use?",
    )


class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """

    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.",
    )


class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is
    recommended.
    """

    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.""",
    )


class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """

    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="Any spatial/location qualifiers.",
    )


class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """

    _defn = EnumDefinition(
        name="EnumLaterality",
        description="Laterality information for the site",
    )


class EnumEDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """

    _defn = EnumDefinition(
        name="EnumEDAMFormats",
        description="Data formats from the EDAM ontology.",
    )


class EnumEDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """

    _defn = EnumDefinition(
        name="EnumEDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )


class EnumFileHashType(EnumDefinitionImpl):
    """
    Types of file hashes supported.
    """

    md5 = PermissibleValue(text="md5", title="MD5")
    etag = PermissibleValue(text="etag", title="ETag")
    sha1 = PermissibleValue(text="sha1", title="SHA-1")

    _defn = EnumDefinition(
        name="EnumFileHashType",
        description="Types of file hashes supported.",
    )


# Slots
class slots:
    pass


slots.study_id = Slot(
    uri=CAM.study_id,
    name="study_id",
    curie=CAM.curie("study_id"),
    model_uri=CAM.study_id,
    domain=None,
    range=Optional[Union[str, StudyStudyId]],
)

slots.access_policy_id = Slot(
    uri=CAM.access_policy_id,
    name="access_policy_id",
    curie=CAM.curie("access_policy_id"),
    model_uri=CAM.access_policy_id,
    domain=None,
    range=Optional[Union[str, AccessPolicyAccessPolicyId]],
)

slots.data_use_accession = Slot(
    uri=CAM.data_use_accession,
    name="data_use_accession",
    curie=CAM.curie("data_use_accession"),
    model_uri=CAM.data_use_accession,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.data_use_permission = Slot(
    uri=CAM.data_use_permission,
    name="data_use_permission",
    curie=CAM.curie("data_use_permission"),
    model_uri=CAM.data_use_permission,
    domain=None,
    range=Union[str, "EnumDataUsePermission"],
)

slots.data_use_modifier = Slot(
    uri=CAM.data_use_modifier,
    name="data_use_modifier",
    curie=CAM.curie("data_use_modifier"),
    model_uri=CAM.data_use_modifier,
    domain=None,
    range=Optional[Union[str, "EnumDataUseModifier"]],
)

slots.disease_limitation = Slot(
    uri=CAM.disease_limitation,
    name="disease_limitation",
    curie=CAM.curie("disease_limitation"),
    model_uri=CAM.disease_limitation,
    domain=None,
    range=Optional[str],
)

slots.access_description = Slot(
    uri=CAM.access_description,
    name="access_description",
    curie=CAM.curie("access_description"),
    model_uri=CAM.access_description,
    domain=None,
    range=Optional[str],
)

slots.do_id = Slot(
    uri=CAM.do_id,
    name="do_id",
    curie=CAM.curie("do_id"),
    model_uri=CAM.do_id,
    domain=None,
    range=Optional[Union[str, DOIDoId]],
)

slots.subject_id = Slot(
    uri=CAM.subject_id,
    name="subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.subject_id,
    domain=None,
    range=Optional[Union[str, SubjectSubjectId]],
)

slots.assertion_id = Slot(
    uri=CAM.assertion_id,
    name="assertion_id",
    curie=CAM.curie("assertion_id"),
    model_uri=CAM.assertion_id,
    domain=None,
    range=Optional[Union[str, SubjectAssertionAssertionId]],
)

slots.external_id = Slot(
    uri=CAM.external_id,
    name="external_id",
    curie=CAM.curie("external_id"),
    model_uri=CAM.external_id,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.parent_study = Slot(
    uri=CAM.parent_study,
    name="parent_study",
    curie=CAM.curie("parent_study"),
    model_uri=CAM.parent_study,
    domain=None,
    range=Optional[Union[str, StudyStudyId]],
)

slots.funding_source = Slot(
    uri=CAM.funding_source,
    name="funding_source",
    curie=CAM.curie("funding_source"),
    model_uri=CAM.funding_source,
    domain=None,
    range=Optional[Union[str, list[str]]],
)

slots.principal_investigator = Slot(
    uri=CAM.principal_investigator,
    name="principal_investigator",
    curie=CAM.curie("principal_investigator"),
    model_uri=CAM.principal_investigator,
    domain=None,
    range=Union[Union[dict, Investigator], list[Union[dict, Investigator]]],
)

slots.study_title = Slot(
    uri=CAM.study_title,
    name="study_title",
    curie=CAM.curie("study_title"),
    model_uri=CAM.study_title,
    domain=None,
    range=str,
)

slots.study_code = Slot(
    uri=CAM.study_code,
    name="study_code",
    curie=CAM.curie("study_code"),
    model_uri=CAM.study_code,
    domain=None,
    range=str,
)

slots.study_short_name = Slot(
    uri=CAM.study_short_name,
    name="study_short_name",
    curie=CAM.curie("study_short_name"),
    model_uri=CAM.study_short_name,
    domain=None,
    range=Optional[str],
)

slots.investigator_title = Slot(
    uri=CAM.investigator_title,
    name="investigator_title",
    curie=CAM.curie("investigator_title"),
    model_uri=CAM.investigator_title,
    domain=None,
    range=Optional[str],
)

slots.name = Slot(
    uri=CAM.name,
    name="name",
    curie=CAM.curie("name"),
    model_uri=CAM.name,
    domain=None,
    range=Optional[str],
)

slots.email = Slot(
    uri=CAM.email,
    name="email",
    curie=CAM.curie("email"),
    model_uri=CAM.email,
    domain=None,
    range=Optional[str],
)

slots.institution = Slot(
    uri=CAM.institution,
    name="institution",
    curie=CAM.curie("institution"),
    model_uri=CAM.institution,
    domain=None,
    range=Optional[str],
)

slots.program = Slot(
    uri=CAM.program,
    name="program",
    curie=CAM.curie("program"),
    model_uri=CAM.program,
    domain=None,
    range=Union[Union[str, "EnumProgram"], list[Union[str, "EnumProgram"]]],
)

slots.study_description = Slot(
    uri=CAM.study_description,
    name="study_description",
    curie=CAM.curie("study_description"),
    model_uri=CAM.study_description,
    domain=None,
    range=str,
)

slots.website = Slot(
    uri=CAM.website,
    name="website",
    curie=CAM.curie("website"),
    model_uri=CAM.website,
    domain=None,
    range=Optional[Union[str, URI]],
)

slots.contact = Slot(
    uri=CAM.contact,
    name="contact",
    curie=CAM.curie("contact"),
    model_uri=CAM.contact,
    domain=None,
    range=Union[Union[dict, Investigator], list[Union[dict, Investigator]]],
)

slots.vbr_id = Slot(
    uri=CAM.vbr_id,
    name="vbr_id",
    curie=CAM.curie("vbr_id"),
    model_uri=CAM.vbr_id,
    domain=None,
    range=Optional[Union[str, VirtualBiorepositoryVbrId]],
)

slots.vbr_readme = Slot(
    uri=CAM.vbr_readme,
    name="vbr_readme",
    curie=CAM.curie("vbr_readme"),
    model_uri=CAM.vbr_readme,
    domain=None,
    range=Optional[str],
)

slots.research_domain = Slot(
    uri=CAM.research_domain,
    name="research_domain",
    curie=CAM.curie("research_domain"),
    model_uri=CAM.research_domain,
    domain=None,
    range=Union[
        Union[str, "EnumResearchDomain"], list[Union[str, "EnumResearchDomain"]]
    ],
)

slots.participant_lifespan_stage = Slot(
    uri=CAM.participant_lifespan_stage,
    name="participant_lifespan_stage",
    curie=CAM.curie("participant_lifespan_stage"),
    model_uri=CAM.participant_lifespan_stage,
    domain=None,
    range=Union[
        Union[str, "EnumParticipantLifespanStage"],
        list[Union[str, "EnumParticipantLifespanStage"]],
    ],
)

slots.selection_criteria = Slot(
    uri=CAM.selection_criteria,
    name="selection_criteria",
    curie=CAM.curie("selection_criteria"),
    model_uri=CAM.selection_criteria,
    domain=None,
    range=Optional[str],
)

slots.study_design = Slot(
    uri=CAM.study_design,
    name="study_design",
    curie=CAM.curie("study_design"),
    model_uri=CAM.study_design,
    domain=None,
    range=Union[Union[str, "EnumStudyDesign"], list[Union[str, "EnumStudyDesign"]]],
)

slots.data_category = Slot(
    uri=CAM.data_category,
    name="data_category",
    curie=CAM.curie("data_category"),
    model_uri=CAM.data_category,
    domain=None,
    range=Optional[Union[str, "EnumDataCategory"]],
)

slots.clinical_data_source_type = Slot(
    uri=CAM.clinical_data_source_type,
    name="clinical_data_source_type",
    curie=CAM.curie("clinical_data_source_type"),
    model_uri=CAM.clinical_data_source_type,
    domain=None,
    range=Union[
        Union[str, "EnumClinicalDataSourceType"],
        list[Union[str, "EnumClinicalDataSourceType"]],
    ],
)

slots.publication = Slot(
    uri=CAM.publication,
    name="publication",
    curie=CAM.curie("publication"),
    model_uri=CAM.publication,
    domain=None,
    range=Optional[Union[Union[dict, Publication], list[Union[dict, Publication]]]],
)

slots.expected_number_of_participants = Slot(
    uri=CAM.expected_number_of_participants,
    name="expected_number_of_participants",
    curie=CAM.curie("expected_number_of_participants"),
    model_uri=CAM.expected_number_of_participants,
    domain=None,
    range=int,
)

slots.actual_number_of_participants = Slot(
    uri=CAM.actual_number_of_participants,
    name="actual_number_of_participants",
    curie=CAM.curie("actual_number_of_participants"),
    model_uri=CAM.actual_number_of_participants,
    domain=None,
    range=int,
)

slots.acknowledgments = Slot(
    uri=CAM.acknowledgments,
    name="acknowledgments",
    curie=CAM.curie("acknowledgments"),
    model_uri=CAM.acknowledgments,
    domain=None,
    range=Optional[str],
)

slots.citation_statement = Slot(
    uri=CAM.citation_statement,
    name="citation_statement",
    curie=CAM.curie("citation_statement"),
    model_uri=CAM.citation_statement,
    domain=None,
    range=Optional[str],
)

slots.bibliographic_reference = Slot(
    uri=CAM.bibliographic_reference,
    name="bibliographic_reference",
    curie=CAM.curie("bibliographic_reference"),
    model_uri=CAM.bibliographic_reference,
    domain=None,
    range=Optional[str],
)

slots.organism_type = Slot(
    uri=CAM.organism_type,
    name="organism_type",
    curie=CAM.curie("organism_type"),
    model_uri=CAM.organism_type,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.subject_type = Slot(
    uri=CAM.subject_type,
    name="subject_type",
    curie=CAM.curie("subject_type"),
    model_uri=CAM.subject_type,
    domain=None,
    range=Union[str, "EnumSubjectType"],
)

slots.sex = Slot(
    uri=CAM.sex,
    name="sex",
    curie=CAM.curie("sex"),
    model_uri=CAM.sex,
    domain=None,
    range=Union[str, "EnumSex"],
)

slots.race = Slot(
    uri=CAM.race,
    name="race",
    curie=CAM.curie("race"),
    model_uri=CAM.race,
    domain=None,
    range=Union[Union[str, "EnumRace"], list[Union[str, "EnumRace"]]],
)

slots.ethnicity = Slot(
    uri=CAM.ethnicity,
    name="ethnicity",
    curie=CAM.curie("ethnicity"),
    model_uri=CAM.ethnicity,
    domain=None,
    range=Union[str, "EnumEthnicity"],
)

slots.down_syndrome_status = Slot(
    uri=CAM.down_syndrome_status,
    name="down_syndrome_status",
    curie=CAM.curie("down_syndrome_status"),
    model_uri=CAM.down_syndrome_status,
    domain=None,
    range=Union[str, "EnumDownSyndromeStatus"],
)

slots.age_at_first_engagement = Slot(
    uri=CAM.age_at_first_engagement,
    name="age_at_first_engagement",
    curie=CAM.curie("age_at_first_engagement"),
    model_uri=CAM.age_at_first_engagement,
    domain=None,
    range=Optional[int],
)

slots.vital_status = Slot(
    uri=CAM.vital_status,
    name="vital_status",
    curie=CAM.curie("vital_status"),
    model_uri=CAM.vital_status,
    domain=None,
    range=Optional[Union[str, "EnumVitalStatus"]],
)

slots.age_at_last_vital_status = Slot(
    uri=CAM.age_at_last_vital_status,
    name="age_at_last_vital_status",
    curie=CAM.curie("age_at_last_vital_status"),
    model_uri=CAM.age_at_last_vital_status,
    domain=None,
    range=Optional[int],
)

slots.family_id = Slot(
    uri=CAM.family_id,
    name="family_id",
    curie=CAM.curie("family_id"),
    model_uri=CAM.family_id,
    domain=None,
    range=Optional[Union[str, FamilyFamilyId]],
)

slots.family_type = Slot(
    uri=CAM.family_type,
    name="family_type",
    curie=CAM.curie("family_type"),
    model_uri=CAM.family_type,
    domain=None,
    range=Optional[Union[str, "EnumFamilyType"]],
)

slots.family_description = Slot(
    uri=CAM.family_description,
    name="family_description",
    curie=CAM.curie("family_description"),
    model_uri=CAM.family_description,
    domain=None,
    range=Optional[str],
)

slots.consanguinity = Slot(
    uri=CAM.consanguinity,
    name="consanguinity",
    curie=CAM.curie("consanguinity"),
    model_uri=CAM.consanguinity,
    domain=None,
    range=Optional[Union[str, "EnumConsanguinityAssertion"]],
)

slots.family_study_focus = Slot(
    uri=CAM.family_study_focus,
    name="family_study_focus",
    curie=CAM.curie("family_study_focus"),
    model_uri=CAM.family_study_focus,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.family_relationship_id = Slot(
    uri=CAM.family_relationship_id,
    name="family_relationship_id",
    curie=CAM.curie("family_relationship_id"),
    model_uri=CAM.family_relationship_id,
    domain=None,
    range=Optional[Union[str, FamilyRelationshipFamilyRelationshipId]],
)

slots.family_member_id = Slot(
    uri=CAM.family_member_id,
    name="family_member_id",
    curie=CAM.curie("family_member_id"),
    model_uri=CAM.family_member_id,
    domain=None,
    range=Union[str, SubjectSubjectId],
)

slots.relationship = Slot(
    uri=CAM.relationship,
    name="relationship",
    curie=CAM.curie("relationship"),
    model_uri=CAM.relationship,
    domain=None,
    range=Union[str, URIorCURIE],
)

slots.family_role = Slot(
    uri=CAM.family_role,
    name="family_role",
    curie=CAM.curie("family_role"),
    model_uri=CAM.family_role,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.assertion_provenance = Slot(
    uri=CAM.assertion_provenance,
    name="assertion_provenance",
    curie=CAM.curie("assertion_provenance"),
    model_uri=CAM.assertion_provenance,
    domain=None,
    range=Optional[Union[str, "EnumAssertionProvenance"]],
)

slots.age_at_assertion = Slot(
    uri=CAM.age_at_assertion,
    name="age_at_assertion",
    curie=CAM.curie("age_at_assertion"),
    model_uri=CAM.age_at_assertion,
    domain=None,
    range=Optional[int],
)

slots.age_at_event = Slot(
    uri=CAM.age_at_event,
    name="age_at_event",
    curie=CAM.curie("age_at_event"),
    model_uri=CAM.age_at_event,
    domain=None,
    range=Optional[int],
)

slots.age_at_resolution = Slot(
    uri=CAM.age_at_resolution,
    name="age_at_resolution",
    curie=CAM.curie("age_at_resolution"),
    model_uri=CAM.age_at_resolution,
    domain=None,
    range=Optional[int],
)

slots.concept = Slot(
    uri=CAM.concept,
    name="concept",
    curie=CAM.curie("concept"),
    model_uri=CAM.concept,
    domain=None,
    range=Optional[
        Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]
    ],
)

slots.concept_curie = Slot(
    uri=CAM.concept_curie,
    name="concept_curie",
    curie=CAM.curie("concept_curie"),
    model_uri=CAM.concept_curie,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.display = Slot(
    uri=CAM.display,
    name="display",
    curie=CAM.curie("display"),
    model_uri=CAM.display,
    domain=None,
    range=Optional[str],
)

slots.concept_source = Slot(
    uri=CAM.concept_source,
    name="concept_source",
    curie=CAM.curie("concept_source"),
    model_uri=CAM.concept_source,
    domain=None,
    range=Optional[str],
)

slots.value_concept = Slot(
    uri=CAM.value_concept,
    name="value_concept",
    curie=CAM.curie("value_concept"),
    model_uri=CAM.value_concept,
    domain=None,
    range=Optional[
        Union[Union[str, ConceptConceptCurie], list[Union[str, ConceptConceptCurie]]]
    ],
)

slots.value_number = Slot(
    uri=CAM.value_number,
    name="value_number",
    curie=CAM.curie("value_number"),
    model_uri=CAM.value_number,
    domain=None,
    range=Optional[float],
)

slots.value_source = Slot(
    uri=CAM.value_source,
    name="value_source",
    curie=CAM.curie("value_source"),
    model_uri=CAM.value_source,
    domain=None,
    range=Optional[str],
)

slots.value_unit = Slot(
    uri=CAM.value_unit,
    name="value_unit",
    curie=CAM.curie("value_unit"),
    model_uri=CAM.value_unit,
    domain=None,
    range=Optional[Union[str, ConceptConceptCurie]],
)

slots.value_unit_source = Slot(
    uri=CAM.value_unit_source,
    name="value_unit_source",
    curie=CAM.curie("value_unit_source"),
    model_uri=CAM.value_unit_source,
    domain=None,
    range=Optional[str],
)

slots.sample_id = Slot(
    uri=CAM.sample_id,
    name="sample_id",
    curie=CAM.curie("sample_id"),
    model_uri=CAM.sample_id,
    domain=None,
    range=Optional[Union[str, SampleSampleId]],
)

slots.parent_sample_id = Slot(
    uri=CAM.parent_sample_id,
    name="parent_sample_id",
    curie=CAM.curie("parent_sample_id"),
    model_uri=CAM.parent_sample_id,
    domain=None,
    range=Optional[Union[str, SampleSampleId]],
)

slots.biospecimen_collection_id = Slot(
    uri=CAM.biospecimen_collection_id,
    name="biospecimen_collection_id",
    curie=CAM.curie("biospecimen_collection_id"),
    model_uri=CAM.biospecimen_collection_id,
    domain=None,
    range=Optional[Union[str, BiospecimenCollectionBiospecimenCollectionId]],
)

slots.aliquot_id = Slot(
    uri=CAM.aliquot_id,
    name="aliquot_id",
    curie=CAM.curie("aliquot_id"),
    model_uri=CAM.aliquot_id,
    domain=None,
    range=Optional[Union[str, AliquotAliquotId]],
)

slots.sample_type = Slot(
    uri=CAM.sample_type,
    name="sample_type",
    curie=CAM.curie("sample_type"),
    model_uri=CAM.sample_type,
    domain=None,
    range=Union[str, URIorCURIE],
)

slots.processing = Slot(
    uri=CAM.processing,
    name="processing",
    curie=CAM.curie("processing"),
    model_uri=CAM.processing,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.availability_status = Slot(
    uri=CAM.availability_status,
    name="availability_status",
    curie=CAM.curie("availability_status"),
    model_uri=CAM.availability_status,
    domain=None,
    range=Optional[Union[str, "EnumAvailabilityStatus"]],
)

slots.storage_method = Slot(
    uri=CAM.storage_method,
    name="storage_method",
    curie=CAM.curie("storage_method"),
    model_uri=CAM.storage_method,
    domain=None,
    range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]],
)

slots.quantity_number = Slot(
    uri=CAM.quantity_number,
    name="quantity_number",
    curie=CAM.curie("quantity_number"),
    model_uri=CAM.quantity_number,
    domain=None,
    range=Optional[float],
)

slots.quantity_unit = Slot(
    uri=CAM.quantity_unit,
    name="quantity_unit",
    curie=CAM.curie("quantity_unit"),
    model_uri=CAM.quantity_unit,
    domain=None,
    range=Optional[Union[str, ConceptConceptCurie]],
)

slots.concentration_number = Slot(
    uri=CAM.concentration_number,
    name="concentration_number",
    curie=CAM.curie("concentration_number"),
    model_uri=CAM.concentration_number,
    domain=None,
    range=Optional[float],
)

slots.concentration_unit = Slot(
    uri=CAM.concentration_unit,
    name="concentration_unit",
    curie=CAM.curie("concentration_unit"),
    model_uri=CAM.concentration_unit,
    domain=None,
    range=Optional[Union[str, ConceptConceptCurie]],
)

slots.age_at_collection = Slot(
    uri=CAM.age_at_collection,
    name="age_at_collection",
    curie=CAM.curie("age_at_collection"),
    model_uri=CAM.age_at_collection,
    domain=None,
    range=Optional[float],
)

slots.method = Slot(
    uri=CAM.method,
    name="method",
    curie=CAM.curie("method"),
    model_uri=CAM.method,
    domain=None,
    range=Optional[Union[str, "EnumSampleCollectionMethod"]],
)

slots.site = Slot(
    uri=CAM.site,
    name="site",
    curie=CAM.curie("site"),
    model_uri=CAM.site,
    domain=None,
    range=Optional[Union[str, "EnumSite"]],
)

slots.spatial_qualifier = Slot(
    uri=CAM.spatial_qualifier,
    name="spatial_qualifier",
    curie=CAM.curie("spatial_qualifier"),
    model_uri=CAM.spatial_qualifier,
    domain=None,
    range=Optional[Union[str, "EnumSpatialQualifiers"]],
)

slots.laterality = Slot(
    uri=CAM.laterality,
    name="laterality",
    curie=CAM.curie("laterality"),
    model_uri=CAM.laterality,
    domain=None,
    range=Optional[Union[str, "EnumLaterality"]],
)

slots.encounter_id = Slot(
    uri=CAM.encounter_id,
    name="encounter_id",
    curie=CAM.curie("encounter_id"),
    model_uri=CAM.encounter_id,
    domain=None,
    range=Optional[Union[str, EncounterEncounterId]],
)

slots.description = Slot(
    uri=CAM.description,
    name="description",
    curie=CAM.curie("description"),
    model_uri=CAM.description,
    domain=None,
    range=Optional[str],
)

slots.encounter_definition_id = Slot(
    uri=CAM.encounter_definition_id,
    name="encounter_definition_id",
    curie=CAM.curie("encounter_definition_id"),
    model_uri=CAM.encounter_definition_id,
    domain=None,
    range=Optional[Union[str, EncounterDefinitionEncounterDefinitionId]],
)

slots.activity_definition_id = Slot(
    uri=CAM.activity_definition_id,
    name="activity_definition_id",
    curie=CAM.curie("activity_definition_id"),
    model_uri=CAM.activity_definition_id,
    domain=None,
    range=Optional[Union[str, ActivityDefinitionActivityDefinitionId]],
)

slots.file_id = Slot(
    uri=CAM.file_id,
    name="file_id",
    curie=CAM.curie("file_id"),
    model_uri=CAM.file_id,
    domain=None,
    range=Optional[Union[str, FileFileId]],
)

slots.filename = Slot(
    uri=CAM.filename,
    name="filename",
    curie=CAM.curie("filename"),
    model_uri=CAM.filename,
    domain=None,
    range=Optional[str],
)

slots.format = Slot(
    uri=CAM.format,
    name="format",
    curie=CAM.curie("format"),
    model_uri=CAM.format,
    domain=None,
    range=Optional[Union[str, "EnumEDAMFormats"]],
)

slots.data_type = Slot(
    uri=CAM.data_type,
    name="data_type",
    curie=CAM.curie("data_type"),
    model_uri=CAM.data_type,
    domain=None,
    range=Optional[Union[str, "EnumEDAMDataTypes"]],
)

slots.size = Slot(
    uri=CAM.size,
    name="size",
    curie=CAM.curie("size"),
    model_uri=CAM.size,
    domain=None,
    range=Optional[int],
)

slots.staging_url = Slot(
    uri=CAM.staging_url,
    name="staging_url",
    curie=CAM.curie("staging_url"),
    model_uri=CAM.staging_url,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.release_url = Slot(
    uri=CAM.release_url,
    name="release_url",
    curie=CAM.curie("release_url"),
    model_uri=CAM.release_url,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.drs_uri = Slot(
    uri=CAM.drs_uri,
    name="drs_uri",
    curie=CAM.curie("drs_uri"),
    model_uri=CAM.drs_uri,
    domain=None,
    range=Optional[Union[str, URIorCURIE]],
)

slots.hash = Slot(
    uri=CAM.hash,
    name="hash",
    curie=CAM.curie("hash"),
    model_uri=CAM.hash,
    domain=None,
    range=Optional[Union[dict, FileHash]],
)

slots.hash_type = Slot(
    uri=CAM.hash_type,
    name="hash_type",
    curie=CAM.curie("hash_type"),
    model_uri=CAM.hash_type,
    domain=None,
    range=Optional[Union[str, "EnumFileHashType"]],
)

slots.hash_value = Slot(
    uri=CAM.hash_value,
    name="hash_value",
    curie=CAM.curie("hash_value"),
    model_uri=CAM.hash_value,
    domain=None,
    range=Optional[str],
)

slots.dataset_id = Slot(
    uri=CAM.dataset_id,
    name="dataset_id",
    curie=CAM.curie("dataset_id"),
    model_uri=CAM.dataset_id,
    domain=None,
    range=Optional[Union[str, DatasetDatasetId]],
)

slots.data_collection_start = Slot(
    uri=CAM.data_collection_start,
    name="data_collection_start",
    curie=CAM.curie("data_collection_start"),
    model_uri=CAM.data_collection_start,
    domain=None,
    range=Optional[str],
)

slots.data_collection_end = Slot(
    uri=CAM.data_collection_end,
    name="data_collection_end",
    curie=CAM.curie("data_collection_end"),
    model_uri=CAM.data_collection_end,
    domain=None,
    range=Optional[str],
)

slots.AccessPolicy_access_policy_id = Slot(
    uri=CAM.access_policy_id,
    name="AccessPolicy_access_policy_id",
    curie=CAM.curie("access_policy_id"),
    model_uri=CAM.AccessPolicy_access_policy_id,
    domain=AccessPolicy,
    range=Union[str, AccessPolicyAccessPolicyId],
)

slots.Study_study_id = Slot(
    uri=CAM.study_id,
    name="Study_study_id",
    curie=CAM.curie("study_id"),
    model_uri=CAM.Study_study_id,
    domain=Study,
    range=Union[str, StudyStudyId],
)

slots.StudyMetadata_study_id = Slot(
    uri=CAM.study_id,
    name="StudyMetadata_study_id",
    curie=CAM.curie("study_id"),
    model_uri=CAM.StudyMetadata_study_id,
    domain=StudyMetadata,
    range=Union[str, StudyMetadataStudyId],
)

slots.StudyMetadata_data_category = Slot(
    uri=CAM.data_category,
    name="StudyMetadata_data_category",
    curie=CAM.curie("data_category"),
    model_uri=CAM.StudyMetadata_data_category,
    domain=StudyMetadata,
    range=Union[Union[str, "EnumDataCategory"], list[Union[str, "EnumDataCategory"]]],
)

slots.VirtualBiorepository_vbr_id = Slot(
    uri=CAM.vbr_id,
    name="VirtualBiorepository_vbr_id",
    curie=CAM.curie("vbr_id"),
    model_uri=CAM.VirtualBiorepository_vbr_id,
    domain=VirtualBiorepository,
    range=Union[str, VirtualBiorepositoryVbrId],
)

slots.DOI_do_id = Slot(
    uri=CAM.do_id,
    name="DOI_do_id",
    curie=CAM.curie("do_id"),
    model_uri=CAM.DOI_do_id,
    domain=DOI,
    range=Union[str, DOIDoId],
)

slots.Subject_subject_id = Slot(
    uri=CAM.subject_id,
    name="Subject_subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.Subject_subject_id,
    domain=Subject,
    range=Union[str, SubjectSubjectId],
)

slots.Demographics_subject_id = Slot(
    uri=CAM.subject_id,
    name="Demographics_subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.Demographics_subject_id,
    domain=Demographics,
    range=Union[str, DemographicsSubjectId],
)

slots.Family_family_id = Slot(
    uri=CAM.family_id,
    name="Family_family_id",
    curie=CAM.curie("family_id"),
    model_uri=CAM.Family_family_id,
    domain=Family,
    range=Union[str, FamilyFamilyId],
)

slots.FamilyRelationship_family_relationship_id = Slot(
    uri=CAM.family_relationship_id,
    name="FamilyRelationship_family_relationship_id",
    curie=CAM.curie("family_relationship_id"),
    model_uri=CAM.FamilyRelationship_family_relationship_id,
    domain=FamilyRelationship,
    range=Union[str, FamilyRelationshipFamilyRelationshipId],
)

slots.FamilyRelationship_subject_id = Slot(
    uri=CAM.subject_id,
    name="FamilyRelationship_subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.FamilyRelationship_subject_id,
    domain=FamilyRelationship,
    range=Union[str, SubjectSubjectId],
)

slots.FamilyMember_family_id = Slot(
    uri=CAM.family_id,
    name="FamilyMember_family_id",
    curie=CAM.curie("family_id"),
    model_uri=CAM.FamilyMember_family_id,
    domain=FamilyMember,
    range=Union[str, FamilyFamilyId],
)

slots.FamilyMember_subject_id = Slot(
    uri=CAM.subject_id,
    name="FamilyMember_subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.FamilyMember_subject_id,
    domain=FamilyMember,
    range=Union[str, SubjectSubjectId],
)

slots.SubjectAssertion_assertion_id = Slot(
    uri=CAM.assertion_id,
    name="SubjectAssertion_assertion_id",
    curie=CAM.curie("assertion_id"),
    model_uri=CAM.SubjectAssertion_assertion_id,
    domain=SubjectAssertion,
    range=Union[str, SubjectAssertionAssertionId],
)

slots.Concept_concept_curie = Slot(
    uri=CAM.concept_curie,
    name="Concept_concept_curie",
    curie=CAM.curie("concept_curie"),
    model_uri=CAM.Concept_concept_curie,
    domain=Concept,
    range=Union[str, ConceptConceptCurie],
)

slots.Sample_sample_id = Slot(
    uri=CAM.sample_id,
    name="Sample_sample_id",
    curie=CAM.curie("sample_id"),
    model_uri=CAM.Sample_sample_id,
    domain=Sample,
    range=Union[str, SampleSampleId],
)

slots.Sample_biospecimen_collection_id = Slot(
    uri=CAM.biospecimen_collection_id,
    name="Sample_biospecimen_collection_id",
    curie=CAM.curie("biospecimen_collection_id"),
    model_uri=CAM.Sample_biospecimen_collection_id,
    domain=Sample,
    range=Optional[Union[str, BiospecimenCollectionBiospecimenCollectionId]],
)

slots.BiospecimenCollection_biospecimen_collection_id = Slot(
    uri=CAM.biospecimen_collection_id,
    name="BiospecimenCollection_biospecimen_collection_id",
    curie=CAM.curie("biospecimen_collection_id"),
    model_uri=CAM.BiospecimenCollection_biospecimen_collection_id,
    domain=BiospecimenCollection,
    range=Union[str, BiospecimenCollectionBiospecimenCollectionId],
)

slots.Aliquot_aliquot_id = Slot(
    uri=CAM.aliquot_id,
    name="Aliquot_aliquot_id",
    curie=CAM.curie("aliquot_id"),
    model_uri=CAM.Aliquot_aliquot_id,
    domain=Aliquot,
    range=Union[str, AliquotAliquotId],
)

slots.Encounter_encounter_id = Slot(
    uri=CAM.encounter_id,
    name="Encounter_encounter_id",
    curie=CAM.curie("encounter_id"),
    model_uri=CAM.Encounter_encounter_id,
    domain=Encounter,
    range=Union[str, EncounterEncounterId],
)

slots.EncounterDefinition_encounter_definition_id = Slot(
    uri=CAM.encounter_definition_id,
    name="EncounterDefinition_encounter_definition_id",
    curie=CAM.curie("encounter_definition_id"),
    model_uri=CAM.EncounterDefinition_encounter_definition_id,
    domain=EncounterDefinition,
    range=Union[str, EncounterDefinitionEncounterDefinitionId],
)

slots.EncounterDefinition_activity_definition_id = Slot(
    uri=CAM.activity_definition_id,
    name="EncounterDefinition_activity_definition_id",
    curie=CAM.curie("activity_definition_id"),
    model_uri=CAM.EncounterDefinition_activity_definition_id,
    domain=EncounterDefinition,
    range=Optional[
        Union[
            Union[str, ActivityDefinitionActivityDefinitionId],
            list[Union[str, ActivityDefinitionActivityDefinitionId]],
        ]
    ],
)

slots.ActivityDefinition_activity_definition_id = Slot(
    uri=CAM.activity_definition_id,
    name="ActivityDefinition_activity_definition_id",
    curie=CAM.curie("activity_definition_id"),
    model_uri=CAM.ActivityDefinition_activity_definition_id,
    domain=ActivityDefinition,
    range=Union[str, ActivityDefinitionActivityDefinitionId],
)

slots.File_file_id = Slot(
    uri=CAM.file_id,
    name="File_file_id",
    curie=CAM.curie("file_id"),
    model_uri=CAM.File_file_id,
    domain=File,
    range=Union[str, FileFileId],
)

slots.File_subject_id = Slot(
    uri=CAM.subject_id,
    name="File_subject_id",
    curie=CAM.curie("subject_id"),
    model_uri=CAM.File_subject_id,
    domain=File,
    range=Optional[
        Union[Union[str, SubjectSubjectId], list[Union[str, SubjectSubjectId]]]
    ],
)

slots.File_sample_id = Slot(
    uri=CAM.sample_id,
    name="File_sample_id",
    curie=CAM.curie("sample_id"),
    model_uri=CAM.File_sample_id,
    domain=File,
    range=Optional[Union[Union[str, SampleSampleId], list[Union[str, SampleSampleId]]]],
)

slots.Dataset_dataset_id = Slot(
    uri=CAM.dataset_id,
    name="Dataset_dataset_id",
    curie=CAM.curie("dataset_id"),
    model_uri=CAM.Dataset_dataset_id,
    domain=Dataset,
    range=Union[str, DatasetDatasetId],
)

slots.Dataset_file_id = Slot(
    uri=CAM.file_id,
    name="Dataset_file_id",
    curie=CAM.curie("file_id"),
    model_uri=CAM.Dataset_file_id,
    domain=Dataset,
    range=Optional[Union[Union[str, FileFileId], list[Union[str, FileFileId]]]],
)
