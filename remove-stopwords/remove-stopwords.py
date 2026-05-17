def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    output = []
    for i in tokens:
        if i in stopwords:
            pass
        else:
           output.append(i)
    return output