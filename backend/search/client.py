from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client

def get_index(index_name="cfe_Product"):
    client = get_client()
    index = client.init_index(index_name)
    return index