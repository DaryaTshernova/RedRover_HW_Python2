def pillars(num_pill, dist, width):
    l = (dist * (num_pill - 1) + width / 100 * (num_pill - 2)) * 100
    return (round(l) if l > 0 else 0)