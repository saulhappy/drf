from algoliasearch_django import algolia_engine


def get_client():
    return algolia_engine.client


client = get_client()
