from algoliasearch_django import algolia_engine




def get_client():
    return algolia_engine.client

def get_index(name='Product'):
    client = get_client()
    index = client.init_index(name=name)
    return index


def perfom_search(query=None, **kwargs):
    index = get_index()
    params = {}
    tags = ""
    if "tags" in kwargs:
        tags = kwargs.pop('tags') or []
        if len(tags) > 0:
            params['tagFilters'] = tags
    results = index.search(query, params)
    return results

