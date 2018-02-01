
from httpproxy.utils import encode_partial_urls

def test_encode_partial_urls():
    assert '/ontologies/SNOMEDCT/classes/http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FSNOMEDCT%2FC0460402/children' \
        == encode_partial_urls('/ontologies/SNOMEDCT/classes/http%3A//purl.bioontology.org/ontology/SNOMEDCT/C0460402/children'), 'SNOMED ontologytree'

    assert '/ontologies/DOID/classes/http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FDOID_4/children' \
        == encode_partial_urls('/ontologies/DOID/classes/http%3A//purl.obolibrary.org%2Fobo%2FDOID_4/children'), 'DOID_4 ontologytree'
