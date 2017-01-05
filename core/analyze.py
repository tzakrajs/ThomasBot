def word_frequency(text):
    words = text.split()
    counts = {}
    # map out word counts into dict
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    # reduce dictionary into list of lists for speed
    ranked_word_counts = []
    for word, count in counts.items():
        ranked_word_counts.append((word, count))
    ranked_word_counts.sort(key=lambda x: x[1])
    return {'ranked_word_counts': ranked_word_counts,
            'counts': counts}
