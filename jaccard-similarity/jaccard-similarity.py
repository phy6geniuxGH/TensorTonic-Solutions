def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    return 0.0 if len(set(set_a) | set(set_b)) == 0 else len(set(set_a) & set(set_b)) / len(set(set_a) | set(set_b)) 