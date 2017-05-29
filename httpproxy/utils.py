import re
from django.utils.http import urlquote_plus, urlunquote

def encode_partial_urls(url, key='(?s)(http).*(\d{4}?)'):
    """
    Encodes url, especially for the ontologyserver
    From:
        ontologies/SNOMEDCT/classes/http://purl.bioontology.org/ontology/SNOME
    To:
        ontologies/SNOMEDCT/classes/http%3A%2F%2Fpurl.bioontology.org%2Fontology%2FSNOME
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
