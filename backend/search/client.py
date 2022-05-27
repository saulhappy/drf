from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


def get_index(index_name="_Product"):
    client = get_client()
    index = client.init_index(index_name)
    return index


def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    if "tags" in kwargs:
        tags = kwargs.pop("tags") or None
        if tags:
            params["tagFilters"] = tags
    index_filters = [f"{k}: {v}" for k, v in kwargs.items() if v]
    if index_filters:
        params["facetFilters"] = index_filters
    results = index.search(query, params)
    return results
