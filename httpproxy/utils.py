import re
from django.utils.http import urlquote_plus, urlunquote

def encode_partial_urls(url, key='(?s)(http).*(?=((\\/).*))'):
    """
    Encodes url, especially for the ontologyserver
    From:
        /ontologies/SNOMEDCT/classes/http%3A//purl.bioontology.org/ontology/SNOMEDCT/C0460402/children
    To:
        '/ontologies/SNOMEDCT/classes/http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FSNOMEDCT%2FC0460402/children
    @param url <string>
    @param key <regexp>
    @return <string>
    """

    # take the clean parts of the URL
    tmp = re.split(key, url)
    (start, end) = (tmp[0], tmp[-1])
    # find the url to be encoded and unquote it:

    payload = urlunquote(re.search(key, url).group(0))
    # encode the string
    encoded_string = urlquote_plus(payload)

    return start + encoded_string + end
