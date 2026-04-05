def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top3 = recommended[:k]
    prec_k = len(list(set(top3) & set(relevant)))/k
    recall_k = len(list(set(top3) & set(relevant)))/len(relevant)

    return [prec_k,recall_k]