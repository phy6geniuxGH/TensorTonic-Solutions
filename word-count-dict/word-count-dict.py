from collections import Counter
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    all_sentences = [item for sublist in sentences for item in sublist]
    c = Counter(all_sentences)

    return c