import logging

from .exceptions import InvalidArgumentError, NoDataFoundError
from .api import RestAdapter
from .models import Variant, VariantCollection, AlleleCollection, Gene, GeneCollection
from .api import AlleleEndPoint, GeneEndPoint, VariantEndpoint
from .config import APIConfig
from .enums import QueryParameters, IncludeReferenceVariants, IncludeRetiredAlleles, IncludeRetiredReferenceSequences, Function, EvidenceLevel, ReferenceBaseSequence, ReferenceCollection, ReferenceLocationType, VariantBaseSequence, Position, ReferenceSequence, ExcludeSubAlleles
class PharmVarApi:
    """
    PharmVarApi is a class that provides methods to interact with the PharmVar API.
    It uses a RestAdapter object to make HTTP requests to the PharmVar API server.
    The class provides methods to get variants, alleles and genes from the PharmVar database.
    """    
    # Initialize the PharmVarApi object with a RestAdapter object
    def __init__(self, api_key: str, hostname: str = APIConfig.DEFAULT_HOST, version: str = APIConfig.DEFAULT_VERSION, logger: logging.Logger = APIConfig.DEFAULT_LOGGER):
        self._rest_adapter = RestAdapter(hostname, api_key, version, logger)

    ###### Variant methods ######

    def get_all_variants(self,
                         include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                         include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                         position: int | None = Position.DEFAULT.value,
                         reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                         reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                         reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                         reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                         variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                         ) -> VariantCollection:
        """
        Get all variants from the PharmVar database.
        return: VariantCollection object containing all variants
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = VariantEndpoint.ALL.value
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return VariantCollection(data=result.data)

    def get_variants_by_gene(self,
                            gene_symbol: str,
                            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                            position: int | None = Position.DEFAULT.value,
                            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                            ) -> VariantCollection:
        """
        Get all variants for a given gene symbol.
        :param gene_symbol: The gene symbol to search for
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the gene
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }

        endpoint = VariantEndpoint.GENE.value.format(symbol = gene_symbol)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)

    def get_variants_by_allele(self, identifier: str,
                                include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                                include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
                                include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                                position: int | None = Position.DEFAULT.value,
                                reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                                reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                                reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                                reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                                variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                               ) -> VariantCollection:
        """
        Get all variants for a given identifier.
        :param identifier: can be either a PharmVar ID or an allele name. Required
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the identifier.
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = VariantEndpoint.ALLELE.value.format(identifier = identifier)
        try:
            result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        except NoDataFoundError as e:
            return VariantCollection(data=[])
        return VariantCollection(data = result.data)
    
    def get_variants_by_rsid(self, rs_id: str,
                            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
                            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
                            position: int | None = Position.DEFAULT.value,
                            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
                            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
                            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
                            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
                            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
                            ) -> VariantCollection:
        """
        Get all variants for a given rsID.
        :param rs_id: The rsId of the variant
        :param include_reference_variants: Include reference variants like A>A or C>C. Default is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False.
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.). Default is GRCh38.
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: VariantCollection object containing all variants for the rsID
        """
        params = {
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = VariantEndpoint.RSID.value.format(rsId = rs_id)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)
    
    def get_variants_by_spdi(self, spdi: str) -> VariantCollection:
        """
        Get all variants for a given SPDI.
        :param spdi: the SPDI designation of a variant: Reference Sequence:Position:Deletion:Insertion
        :return: VariantCollection object containing all variants for the SPDI
        """
        endpoint = VariantEndpoint.SPDI.value.format(spdi = spdi)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint)
        return VariantCollection(data = result.data)
    
    def get_variant_impact(self, *, rs_id: str = None, spdi: str = None) -> str:
        """
        Get the impact of a variant for a given rsID or SPDI.
        :param rs_id: The rsId of the variant
        :param spdi: the SPDI designation of a variant: Reference Sequence:Position:Deletion:Insertion
        :return: VariantCollection object containing the impact of the variant for the rsID
        """
        if rs_id is not None and spdi is not None:
            raise InvalidArgumentError("Either rs_id or spdi must be provided, not both.")
        if rs_id is not None:
            endpoint = VariantEndpoint.RSID_IMPACT.value.format(rsId = rs_id)
        elif spdi is not None:
            endpoint = VariantEndpoint.SPDI_IMPACT.value.format(spdi = spdi)
        else:
            raise InvalidArgumentError("Either rs_id or spdi must be provided.")

        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = {})
        # Save in Variant instance with rs_id or spdi and impact
        variant = Variant(impact = result.data, rsId = rs_id,
                        referenceSequence = spdi.split(":")[0] if spdi else None,
                        position = spdi.split(":")[1] if spdi else None
                        )
        return variant.impact
    
    def get_variant_frequency(self, *, rs_id: str = None, spdi: str = None) -> float:
        """
        Get the frequency of a variant for a given rsID or SPDI.
        :param rs_id: The rsId of the variant
        :param spdi: the SPDI designation of a variant: Reference Sequence:Position:Deletion:Insertion
        :return: float representing the frequency of the variant for the rsID
        """
        if rs_id is not None and spdi is not None:
            raise InvalidArgumentError("Either rs_id or spdi must be provided, not both.")
        if rs_id is not None:
            endpoint = VariantEndpoint.RSID_FREQUENCY.value.format(rsId = rs_id)
        elif spdi is not None:
            endpoint = VariantEndpoint.SPDI_FREQUENCY.value.format(spdi = spdi)
        else:
            raise InvalidArgumentError("Either rs_id or spdi must be provided.")

        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint)
        frequency = result.data[0]["frequency"] if result.data else None
        return frequency

        ###### Allele methods ######

    def get_all_alleles(
            self,
            exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
            function: str | None = Function.DEFAULT.value,
            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
            min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
            position: int | None = Position.DEFAULT.value,
            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
        ) -> AlleleCollection:
            """
            Get all alleles from the PharmVar database with optional filtering parameters.

            Parameters:
                exclude_sub_alleles (bool): Exclude sub-allele definitions from results. Default is False.
                function (Function): Filter results by function (decreased function, function not assigned, increased function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
                include_reference_variants (bool): Include reference variants like A>A or C>C. Default is False.
                include_retired_alleles (bool): Include retired allele definitions from previous versions. Default is False.
                include_retired_reference_sequences (bool): Include variants from retired reference sequences. Default is False.
                min_evidence_level (EvidenceLevel): Filter by minimum evidence level (Definitive, Limited, Moderate).
                position (int): Filter results by variant position.
                reference_base_sequence (ReferenceBase): Filter by reference base sequence (A, C, G, T).
                reference_collection (ReferenceCollection): Filter by reference collection (GRCh37, GRCh38, etc.).
                reference_location_type (ReferenceLocationType): Filter by reference starting location.
                reference_sequence (str): Filter by reference sequence (e.g., "NG_008376.4").
                variant_base_sequence (ReferenceBase): Filter by observed variant base sequence (A, C, G, T).

            Returns:
                AlleleCollection: Collection of alleles matching the specified criteria
            """
            params = {
                QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
                QueryParameters.FUNCTION.value: function,
                QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
                QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
                QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
                QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
                QueryParameters.POSITION.value: position,
                QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
                QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
                QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
                QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
                QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
            }
            endpoint = AlleleEndPoint.ALL.value
            result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
            return AlleleCollection(data=result.data)

    def get_all_active_alleles(
            self
        ) -> AlleleCollection:
            """
            Get all active alleles from the PharmVar database.
            Returns:
                AlleleCollection: Collection of all active alleles
            """
            endpoint = AlleleEndPoint.ACTIVE.value
            result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint)
            return AlleleCollection(data = result.data)
    
    def get_allele_by_identifier(
            self, identifier: str,
            exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
            function: str | None = Function.DEFAULT.value,
            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
            min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
            position: int | None = Position.DEFAULT.value,
            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
        ) -> AlleleCollection:
        """
        Get an allele by its identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = AlleleEndPoint.IDENTIFIER.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return AlleleCollection(data = result.data)

    def get_allele_name(
            self,
            identifier: str,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value
    ) -> str:
        """
        Get the allele name for a given identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name)
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: The allele name
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles
        }
        endpoint = AlleleEndPoint.ALLELE_NAME.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return result.data
    
    def get_allele_evidence_level(
            self,
            identifier: str,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value
    ) -> str:
        """
        Get the evidence level for a given allele identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: The evidence level of the allele
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles
        }
        endpoint = AlleleEndPoint.EVIDENCE_LEVEL.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return result.data
    
    def get_allele_function(
            self,
            identifier: str,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value
    ) -> str:
        """
        Get the CPIC clinical function of an allele for a given identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: The function of the allele
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles
        }
        endpoint = AlleleEndPoint.function.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return result.data
    def get_allele_pv_id(
            self,
            identifier: str,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value
    ) -> str:
        """
        Get the PV ID for a given allele identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: The PV ID of the allele
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles
        }
        endpoint = AlleleEndPoint.PV_ID.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return result.data
    
    def get_allele_references(
            self,
            identifier: str,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value
    ) -> list:
        """
        Get the references for a given allele identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: List of references for the allele
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles
        }
        endpoint = AlleleEndPoint.REFERENCES.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return result.data

    def get_allele_variants(
            self,
            identifier: str,
            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value, 
            position: int | None = Position.DEFAULT.value,
            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> VariantCollection:
        """
        Get the variants for a given allele identifier (PV_ID or allele name).
        :param identifier: The identifier of the allele (PV_ID or allele name). Make sure to use the full allele name, e.g., "CYP2D6*4.001".
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default is False.
        :return: VariantCollection object containing all variants for the allele
        """
        params = {
            QueryParameters.IDENTIFIER.value: identifier,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = AlleleEndPoint.VARIANTS.value.format(identifier = identifier)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return VariantCollection(data = result.data)

    ##### Gene methods #####

    def get_info_all_genes(
            self,
            exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
            function: str | None = Function.DEFAULT.value,
            include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
            include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
            include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
            min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
            position: int | None = Position.DEFAULT.value,
            reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
            reference_collection: str | None = ReferenceCollection.DEFAULT.value,
            reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
            reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
            variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> GeneCollection:
        """
        Returns information for all genes in the PharmVar database.
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased
        function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: GeneCollection object containing all genes with the respective alleles.
        """
        params = {
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }

        endpoint = GeneEndPoint.GENES.value
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return GeneCollection(data = result.data)

    def get_gene_by_entrez_id(
        self,
        entrez_id: str,
        exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
        function: str | None = Function.DEFAULT.value,
        include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
        include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
        include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
        min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
        position: int | None = Position.DEFAULT.value,
        reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
        reference_collection: str | None = ReferenceCollection.DEFAULT.value,
        reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
        reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
        variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> Gene:
        """
        Get a gene by its Entrez ID.
        :param entrez_id: The Entrez ID of the gene
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased
        function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: Gene object containing the gene information and associated alleles.
        """
        params = {
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        
        endpoint = GeneEndPoint.ENTREZ_ID.value.format(entrezId = entrez_id)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return Gene(**result.data)
    
    def get_gene_by_gene_symbol(
        self,
        gene_symbol: str,
        exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
        function: str | None = Function.DEFAULT.value,
        include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
        include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
        include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
        min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
        position: int | None = Position.DEFAULT.value,
        reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
        reference_collection: str | None = ReferenceCollection.DEFAULT.value,
        reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
        reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
        variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> Gene:
        """
        Get a gene by its gene symbol.
        :param gene_symbol: The gene symbol of the gene
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased
        function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: Gene object containing the gene information and associated alleles.
        """
        
        params = {
            QueryParameters.GENE_SYMBOL.value: gene_symbol,
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = GeneEndPoint.SYMBOL.value.format(symbol = gene_symbol)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return Gene(**result.data)

    def get_gene_by_hgnc_id(
        self,
        hgnc_id: str,
        exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
        function: str | None = Function.DEFAULT.value,
        include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
        include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
        include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
        min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
        position: int | None = Position.DEFAULT.value,
        reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
        reference_collection: str | None = ReferenceCollection.DEFAULT.value,
        reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
        reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
        variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> Gene:
    
        """
        Get a gene by its HGNC ID.
        :param hgnc_id: The HGNC ID of the gene
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased
        function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: Gene object containing the gene information and associated alleles.
        """
        
        params = {
            QueryParameters.HGNC.value: hgnc_id,
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        
        endpoint = GeneEndPoint.HGNC.value.format(hgncId = hgnc_id)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return Gene(**result.data)
    
    def get_gene_by_pharmgkb_id(
        self,
        pharmgkb_id: str,
        exclude_sub_alleles: bool = ExcludeSubAlleles.DEFAULT.value,
        function: str | None = Function.DEFAULT.value,
        include_reference_variants: bool = IncludeReferenceVariants.DEFAULT.value,
        include_retired_alleles: bool = IncludeRetiredAlleles.DEFAULT.value,
        include_retired_reference_sequences: bool = IncludeRetiredReferenceSequences.DEFAULT.value,
        min_evidence_level: str | None = EvidenceLevel.DEFAULT.value,
        position: int | None = Position.DEFAULT.value,
        reference_base_sequence: str | None = ReferenceBaseSequence.DEFAULT.value,
        reference_collection: str | None = ReferenceCollection.DEFAULT.value,
        reference_location_type: str | None = ReferenceLocationType.DEFAULT.value,
        reference_sequence: str | None = ReferenceSequence.DEFAULT.value,
        variant_base_sequence: str | None = VariantBaseSequence.DEFAULT.value
    ) -> Gene:
        """
        Get a gene by its PharmGKB ID.
        :param pharmgkb_id: The PharmGKB ID of the gene
        :param exclude_sub_alleles: Exclude sub-allele definitions from results.
        :param function: Filter results by function (decreased function, function not assigned, increased
        function, normal function, possibly decreased, severely decreased, uncertain function, unknown function).
        :param include_reference_variants: Include reference variants like A>A or C>C. Default
        is False.
        :param include_retired_alleles: Include retired allele definitions from previous versions. Default
        is False.
        :param include_retired_reference_sequences: Include variants from retired reference sequences. Default is False
        :param min_evidence_level: Filter by minimum evidence level (Definitive, Limited, Moderate).
        :param position: Filter results by variant position.
        :param reference_base_sequence: Filter by reference base sequence (A, C, G, T).
        :param reference_collection: Filter by reference collection (GRCh37, GRCh38, etc.).
        :param reference_location_type: Filter by reference starting location.
        :param reference_sequence: Filter by reference sequence (e.g., "NG_008376.4").
        :param variant_base_sequence: Filter by observed variant base sequence (A, C, G, T).
        :return: Gene object containing the gene information and associated alleles.
        """
        
        params = {
            QueryParameters.PHARMGKB.value: pharmgkb_id,
            QueryParameters.EXCLUDE_SUB_ALLELES.value: exclude_sub_alleles,
            QueryParameters.FUNCTION.value: function,
            QueryParameters.INCLUDE_REFERENCE_VARIANTS.value: include_reference_variants,
            QueryParameters.INCLUDE_RETIRED_ALLELES.value: include_retired_alleles,
            QueryParameters.INCLUDE_RETIRED_REFERENCE_SEQUENCES.value: include_retired_reference_sequences,
            QueryParameters.MIN_EVIDENCE_LEVEL.value: min_evidence_level,
            QueryParameters.POSITION.value: position,
            QueryParameters.REFERENCE_BASE_SEQUENCE.value: reference_base_sequence,
            QueryParameters.REFERENCE_COLLECTION.value: reference_collection,
            QueryParameters.REFERENCE_LOCATION_TYPE.value: reference_location_type,
            QueryParameters.REFERENCE_SEQUENCE.value: reference_sequence,
            QueryParameters.VARIANT_BASE_SEQUENCE.value: variant_base_sequence
        }
        endpoint = GeneEndPoint.PHARMGKB.value.format(pharmgkbId = pharmgkb_id)
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint, params = params)
        return Gene(**result.data)
    
    def get_gene_list(self) -> list[str]:
        """
        Get a list of all gene symbols in the PharmVar database.
        :return: List of gene symbols
        """
        endpoint = GeneEndPoint.LIST.value
        result = self._rest_adapter._do(http_method = "GET", endpoint = endpoint)
        return result.data