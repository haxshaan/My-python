def remove_smallest(numbers):
    new = numbers

    # use index of min value

    min_index = []

    if len(new) != 0:
        for i, j in enumerate(new):
            if j == min(new):
                min_index.append(i)
        new.remove(new[min(min_index)])
        return new
