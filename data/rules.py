'''
import pprint

d = open('guidelines2.csv').read()
rules = {}
for l in d.split('$$$'):
    words = l.split('###')
    if len(words) > 1:
        rules[words[0].strip().strip(',').zfill(3)] = {
            'directive': words[1].strip().strip(','),
           'text': words[2].strip().strip(',')
        }

pprint.pprint(rules)
'''
rules = {
    '001': {
        'title': 'HTTP URIs',
        'directive': 'MUST',
        'text': 'Use HTTP URIs so that the Linked Dataset URI can be resolved',
        'code':
'''def rule_001(uri):
    if re.match('^http:', uri):
        return True
    else:
        return False
'''
    },
    '002': {
        'title': 'Machine readable',
        'directive': 'MUST',
        'text': 'Provide at least one machine-readable representation in RDF at the Linked Dataset URI',
        'code':
'''def rule_002(uri):
    headers = {'accept': 'text/turtle,application/rdf+xml,application/ld+json,*;q=0'}
    r = requests.get(uri, headers=headers)
    if r.status_code == 200 and ('text/turtle' in r.headers['content-type'] or
                                 'application/rdf+xml' in r.headers['content-type'] or
                                 'application/ld+json' in r.headers['content-type']):
        return True
    else:
        return False
'''
    },
    '003': {
        'title': 'Dataset URI',
        'directive': 'MUST',
        'text': 'The _Dataset URI_ **_MUST _**contain the string \'dataset\', and an appropriate identifier **{datasetid}** describing the nature of the \'Dataset\'.\n\n_URI Pattern_\n**/dataset/{datasetid}**\n\n_Example_ \n**/dataset/schools**',
        'code':
'''def rule_003(dataset_uri):
    if re.match('dataset:', uri):
        return True
    else:
        return False
'''
    },
    '004': {
        'title': 'Modularised Dataset URI',
        'directive': 'SHOULD',
        'text': 'Optionally, it can also be hierarchically structured with an arbitrary number of path segments that are denoted with the identifier **{module} **below.\n\n_URI Pattern_\n**/dataset[/{module}]*/{datasetid}**\n\n_Example_ \n**/dataset/act/schools**'
    },
    '005': {
        'title': 'A Linked Dataset URI class',
        'directive': 'SHOULD',
        'text': 'A Linked Dataset URI is defined as a member of the class dcat:Dataset of the Data Catalog Vocabulary (DCAT)'
    },
    '006': {
        'title': 'Top-level module class',
        'directive': 'SHOULD',
        'text': 'For modularised datasets, the top-level module is declared as a member of the dcat:Catalog class with all datasets within this module referenced through a dcat:dataset property'
    },
    '007': {
        'title': 'Linked Dataset publisher',
        'directive': 'SHOULD',
        'text': 'A Linked Dataset has one or many publishers defined through the Dublin Core [6] dct:publisher property'
    },
    '008': {
        'title': 'Linked Dataset license',
        'directive': 'SHOULD',
        'text': 'A Linked Dataset defines its license with the Dublin Core dct:license property'
    },
    '009': {
        'title': 'Root URI',
        'directive': 'SHOULD',
        'text': 'The _Dataset ROOT URI_ (i.e. http://{domain}.data.gov.au/dataset) results in a list of all _Dataset URIs_ in its {domain}'
    },
    '010': {
        'title': 'Human readable representation',
        'directive': 'MUST',
        'text': 'Provide a human-readable representation in HTML at the _Dataset URI_',
        'code':
'''def rule_010(uri):
    headers = {'accept': 'text/html,*;q=0'}
    r = requests.get(uri, headers=headers)
    if r.status_code == 200 and 'text/html' in r.headers['content-type']:
        return True
    else:
        return False
'''
    },
    '011': {
        'title': 'Multiple representations',
        'directive': 'SHOULD',
        'text': 'If multiple representations exist, provide a means of discovering specific URIs for each of the available representations'
    },
    '012': {
        'title': 'License type',
        'directive': 'SHOULD',
        'text': 'The license for inspection or use of the Linked Dataset shall be provided using a common vocabulary'
    },
    '013': {
        'title': 'Metadata vocabulary',
        'directive': 'SHOULD',
        'text': 'The metadata for a Linked Dataset should be provided using a common vocabulary and contain the expected longevity and maintenance plans for the _Dataset URI_'
    },
    '014': {
        'title': 'Technical implementation invisibility',
        'directive': 'SHOULD NOT',
        'text': 'The current technical implementation of a data publication system should not be visible in or otherwise affect the URI for a Linked Dataset'
    },
    '015': {
        'title': 'Sub-domain use',
        'directive': 'MUST',
        'text': 'All Linked Datasets published under data.gov.au use a sub-domain of data.gov.au to identify all entities within the Linked Dataset',
        'code':
'''def rule_015(uri):
    subdomains = [
        'environment',
        'communication',
        # others
    ]
    # get {top-level-resource}
    # for link in {top-level-resource}:
    #   subdomain = re.search('http://([a-z]*)\..*', link)
    #   if subdomain.group(1) not in subdomains:
    #       return False
    #
    # return True
'''
    },
    '016': {
        'title': 'Base domain',
        'directive': 'MUST',
        'text': '**data.gov.au** is the base domain for Linked Datasets that are promoted for re-use'
    },
    '017': {
        'title': 'AGIFT subdomains',
        'directive': 'MUST',
        'text': 'The government function (e.g. \'education\', \'environment\', \'health\', \'defence\', \'location\') according to the top level of the Australian Governments\' Interactive Functions Thesaurus (AGIFT) is included in the domain name of the URI',
        'code':
'''def rule_017(uri):
    agift_subdomains = [
        "business",
        "communications",
        "communityservices",
        "culture",
        "defence",
        "education",
        "employment",
        "environment",
        "finance",
        "internationalrelations",
        "governance",
        "health",
        "immigration",
        "indigenous",
        "infrastructure",
        "justice",
        "maritime",
        "primaryindustry",
        "recreation",
        "resources",
        "science",
        "security",
        "tourism",
        "trade",
        "transport"
    ]
    subdomain = re.search('http://([a-z]*).data.gov.au.*', uri)
    if subdomain and subdomain.group(1) in agift_subdomains:
        return True
    else:
        return False
'''
    },
    '018': {
        'title': 'Agency name not used',
        'directive': 'MUST',
        'text': 'The name of the department or agency currently responsible for a dataset **_SHALL NOT_** be used in persistent URIs (unless it happens to match the function in AGIFT)',
        'code':
'''
# same rule as 017
def rule_018(uri):
    agift_subdomains = [
        "business",
        "communications",
        "communityservices",
        "culture",
        "defence",
        "education",
        "employment",
        "environment",
        "finance",
        "internationalrelations",
        "governance",
        "health",
        "immigration",
        "indigenous",
        "infrastructure",
        "justice",
        "maritime",
        "primaryindustry",
        "recreation",
        "resources",
        "science",
        "security",
        "tourism",
        "trade",
        "transport"
    ]
    subdomain = re.search('http://([a-z]*).data.gov.au.*', uri)
    if subdomain and subdomain.group(1) in agift_subdomains:
        return True
    else:
        return False
'''
    },
    '019': {
        'title': 'Sub-domain direct response',
        'directive': 'MUST',
        'text': 'The sub-domain supports a direct response (note: this may be implemented as a redirect to department/agency servers from the sub-domain)',
        'code':
'''
def rule_019(subdomain_uri):
    r = requests.get(subdomain_uri, allow_redirects=True)
    print r.status_code
    if r.status_code == 200:
        return True
    else:
        return False
'''
    },
    '020': {
        'title': 'Sub-domain maintenance',
        'directive': 'SHOULD',
        'text': 'The sub-domain are maintained in perpetuity'
    },
    '21a': {
        'title': 'Slash URI identifier',
        'directive': 'SHOULD',
        'text': 'For _Slash URIs_ the _Identifier URI_ **_SHOULD _**contain the token \'id\', a reference to its concept membership {type} and a local name {name} of the \'Thing\'.\n <p>**/id/{type}/{name} --> /id/school/2060**_ [Canberra Grammar]_'
    },
    '21b': {
        'title': 'Hash URI identifier',
        'directive': 'SHOULD',
        'text': 'For _Hash URIs_ the _Identifier URI_ **_SHOULD_** contain the token \'resource\' followed by an appropriate identifier that **_SHOULD _**be the same as the one used for the dataset, i.e. the {datasetid} and a fragment identifier {name} to name the \'Thing\' locally.\n\n**/resource/{datasetid}#{name} --> /resource/schools#2060**_ [Canberra Grammar_'
    },
    '22a': {
        'title': 'Slash URI pattern',
        'directive': 'SHOULD',
        'text': '"For _Slash URIs_ the URI pattern for a _Document URI_ **_SHOULD _**contain the token \'doc\', a reference to its concept membership {type} and a local name {name} of the \'Thing\'.\n\n **doc/{type}/{name} --> doc/school/2060 **_[Document about Canberra Grammar]_'
    },
    '22b': {
        'title': 'Hash URI document URI',
        'directive': 'SHOULD',
        'text': 'For _Hash URIs_ the _Document URI_ **_SHOULD _**contain the token \'resource\' followed by an appropriate identifier that **_SHOULD _**be the same as the one used for the dataset, i.e. the {datasetid}. The _Document URI **MAY **_contain multiple _Identifier URIs_ that can be distinguished from the document they are defined in by their fragment identifier.< br/> \n\n**/resource/{datasetid}#{name} --> /resource/schools#2060**_ [Document that contains information about Canberra Grammar (among potentially other resources)]_'
    },
    '23a': {
        'title': '',
        'directive': 'Hash URI pattern',
        'text': 'The use of a _Hash URI _pattern _is **RECOMMENDED**_ for _Ontology URIs_ for its simplicity'
    },
    '23b': {
        'title': '',
        'directive': 'Concept definition',
        'text': 'Definition of concepts and relations **_SHOULD _**be denoted by the \'def\' keyword followed by the ontology name {scheme}, followed by the concept or relationship name {concept}. If the {concept} name is omitted the whole ontology (vocabulary) should be returned.\n\n **/def/{scheme}#{concept} --> /def/school#phaseOfEducation**_ [The class definition of phaseOfEducation]_</p> \n\nIf instances of classes, i.e. the actual entities (_non-information resources_) are modelled as part of the ontology (for example, code lists, finite sets of entities) in a _Hash URI pattern_ the URIs used for the entities **_SHOULD _**still follow the _Identifier URI_ pattern.'
    },
    '23c': {
        'title': '',
        'directive': 'Class instances',
        'text': 'If instances of classes, i.e. the actual entities (_non-information resources_) are modelled as part of the ontology (for example, code lists, finite sets of entities) the URIs used for the entities **_SHOULD _**still follow the _Identifier URI_ pattern and not the _Ontology URI_ pattern described here'
    },
    '024': {
        'title': 'Child dataset resource consistency',
        'directive': 'MUST',
        'text': 'If a dataset is part of a module all resources within this dataset </em></strong>MUST</em></strong> use the same path segment'
    },
    '25a': {
        'title': 'Identifier URI Slash pattern',
        'directive': 'SHOULD',
        'text': '**/[{module}/]*/id/{type}/{name} --> /act/id/school/2060**_ [Canberra Grammar defined in the schools dataset of the act module]_'
    },
    '25b': {
        'title': 'Identifier URI Hash pattern',
        'directive': 'SHOULD',
        'text': '**/[{module}/]*/resource/{datasetid}#{name} --> /act/resource/schools#2060**_ [Canberra Grammar defined in the schools dataset of the act module]_'
    },
    '26a': {
        'title': 'Document URI Slash pattern',
        'directive': 'SHOULD',
        'text': '**/[{module}/]*/doc/{type}/{name} --> /act/doc/school/2060**_ [Document about Canberra Grammar defined in the school dataset of the act module]_'
    },
    '26b': {
        'title': 'Document URI Hash pattern',
        'directive': 'SHOULD',
        'text': '**/[{module}/]*/resource/{datasetid} --> /act/resource/schools**_ [Document in the act module that contains among other resources information about Canberra Grammar]_'
    },
    '027': {
        'title': 'Ontology URI',
        'directive': 'SHOULD',
        'text': '**/[{module}/]*/def/{scheme}#{concept} --> /act/def/school#phaseOfEducation** \n _[The class definition of phaseOfEducation in the context of the act module]_'
    },
    '28a': {
        'title': 'Resolving Identifier URIs Slash pattern',
        'directive': 'SHOULD',
        'text': 'For _Slash URIs_ a &ldquo;303 See Other&rdquo; status code **_SHOULD_** be issued for requests for** /id/{type}/{id} **with a response redirecting to ** /doc/{type}/{id} **. This indicates to the user that the requested resource is a _Non-Information Resource_, while redirecting the user to the document for the \'Thing\', i.e. the _Information Resource_. Content-negotiation can be used to decide on the specific representation that is returned to the user for the document'
    },
    '28b': {
        'title': 'Resolving Identifier URIs Hash pattern',
        'directive': 'SHOULD',
        'text': 'For _Hash Identifier URIs_ the storage location for **/resource/{datasetid}#{id}** **_SHOULD_** be **/resource/{datasetid}**. As the fragment part in the Hash URI **/resource/{datasetid}#{id}** is stripped off by the HTTP protocol, this is the default storage location and there is no need to setup a redirect.'
    },
    '029': {
        'title': 'RDF HTML file extensions',
        'directive': 'SHOULD',
        'text': 'If the RDF and HTML representations of the resource do not differ in terms of their information content, the use of the file extension is **_RECOMMENDED _**to distinguish the different representations, e.g. .html, .rdf, .owl'
    },
    '030': {
        'title': 'Format doubly stated',
        'directive': 'SHOULD NOT',
        'text': 'If file extensions are used to distinguish between different representations, the type **_MAY NOT_** be explicitly stated in any other part of the URI, e.g.** /doc/school/2060.rdf** rather than** /doc/rdf/school/2060.rdf**'
    },
    '031': {
        'title': 'Content negotiation',
        'directive': 'SHOULD',
        'text': 'If the RDF and HTML representations of the resource differ substantially, i.e. they are not two versions of the same document but different documents altogether, a &ldquo;303 See Other&rdquo; redirect in combination with a content-negotiation **_SHOULD _**be set up that points to two separate _Document URIs_. In this case the use of a token indicating the file type in the _Document URI_ is _**RECOMMENDED**_, e.g. ** /doc/school/2060 ** redirects to ** /doc/rdf/school/2060.rdf **for the RDF representation and to** /doc/html/school/2060.html **for the HTML representation'
    },
    '032': {
        'title': 'Date tokens',
        'directive': 'SHOULD',
        'text': 'To denote different versions of documents, a \'date\' token **_SHOULD _**be used for the _Document URIs_ to indicate that the information is valid on, or from, a particular date. For example, **/doc/html/2012/school/2060** can be used as a _Document URI_ for the school dataset that is current as of 2012'
    },
    '033': {
        'title': 'Ontologys\' schema and instance locations',
        'directive': 'SHOULD',
        'text': 'For ontologies using a _Hash URI _scheme that include both, schema-level (i.e. classes/properties) and instance-level information, the file should be stored in two locations,** /def/{scheme} **and **/resource/{type}** in order to allow proper resolving of _Document URIs_ and _Identifier URIs_ defined in the ontology'
    },
    '034': {
        'title': 'ASCII characters',
        'directive': 'SHOULD',
        'text': 'For _Linked Dataset URIs_, ASCII characters **_SHOULD _**be used, i.e. the numbers from 0-9, the uppercase and lowercase English letters from A to Z, and some special characters'
    },
    '035': {
        'title': 'Accented letters',
        'directive': 'SHOULD',
        'text': 'Accented letters, diacritical and special language characters **_SHOULD NOT_**be used in URIs'
    },
    '036': {
        'title': 'Spaces in URIs',
        'directive': 'NOT RECOMMENDED',
        'text': 'Spaces in URIs are **_NOT RECOMMENDED_**'
    },
    '037': {
        'title': 'URIs are case-sensitive',
        'directive': 'NOT RECOMMENDED',
        'text': 'URIs are case-sensitive apart from the domain name. However, using upper/lower case as a differentiating factor in URIs is **_NOT RECOMMENDED_**'
    },
    '038': {
        'title': 'English preferred',
        'directive': 'SHOULD',
        'text': 'English **_SHOULD _**be exclusively used for naming resources, unless the real-world thing is commonly known in English by its native name (e.g. aboriginal name)'
    },
    '39a': {
        'title': 'Dataset URI lowercase',
        'directive': 'MUST',
        'text': 'Lower case **_MUST_** be used for the entire URI path up to the {datasetid} part. No particular recommendations are made for the {datasetid} part, which can use any casing as deemed appropriate for the domain'
    },
    '39b': {
        'title': 'Dataset URI Things plural',
        'directive': 'SHOULD',
        'text': 'Datasets denote a collection of real-world \'Things\' and thus **_SHOULD _**use the plural for the {datasetid}, e.g. **/dataset/schools**'
    },
    '40a': {
        'title': 'Identifier URI Existing identifiers',
        'directive': 'MUST',
        'text': 'Existing identifiers **_MUST _**always be reused when applicable (even if they are not compliant with the rules on the use of special characters, whitespaces, ... as stated above)'
    },
    '40b': {
        'title': 'Identifier URI Lowercase',
        'directive': 'MUST',
        'text': 'Lower case **_MUST_** be used for the entire URI path up to the {name} part. No particular recommendations are made for the {name} part, which can use any casing as deemed appropriate for the domain'
    },
    '40c': {
        'title': 'Identifier URI singular name',
        'directive': 'SHOULD',
        'text': 'A singular name **_SHOULD _**always be used for naming one particular physical or abstract real-world thing, except if the word to be used for the thing is only available as plural (e.g. series, species)'
    },
    '40d': {
        'title': 'Identifier URI plural for sets',
        'directive': 'SHOULD',
        'text': 'The plural **_SHOULD _**always be used for naming a set/list of real-world \'Things\', e.g. **/id/school/independentSchools** to identify a list of all independent schools in a dataset'
    },
    '40e': {
        'title': 'Identifier URI Acronyms',
        'directive': 'SHOULD',
        'text': 'Acronyms **_SHOULD _**all be in upper cases or all in lower cases'
    },
    '40f': {
        'title': 'Identifier URI de-identified scheme',
        'directive': 'SHOULD',
        'text': 'A de-identified scheme **_SHOULD _**be used for persons, i.e. do not include the name of the person in the URI'
    }
}