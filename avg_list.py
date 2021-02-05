def avg_list(l):
    if len(l) == 0:
        raise ValueError("Empty list!")
    
    return sum(l) / len(l)
