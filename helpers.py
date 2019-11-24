def min_with_indices(arr):
    minimum = min(arr)
    indices = []
    for i, value in enumerate(arr):
        if value == minimum:
            indices.append(i)
    return indices