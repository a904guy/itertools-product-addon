def total_product(*args):

    """Calculate total permutations of a Cartesian product

    :args args is the iterates that would of been passed to more_itertools.specific_product()

    Used to get an integer of for iteration over with specific Cartesian product
    """

    pools = map(tuple, args)
    pool_length = 1
    for pool in pools:
        pool_length *= len(pool)
    pool_length -= 1
    return pool_length


def specific_product(sets, n):

    """Extract single permutation of Cartesian product iteration in an consistent speed regardless of list/set sizes.

    :arg sets: The same arg of sets used for itertools.product, iterates.
    :arg n: Integer of the specific permutation of the product you want to extract.

    This is better then the current itertools generator/yield when dealing with massive amounts of sets/permutations.
    """

    ln = len(sets)
    dm = [None] * ln
    f = 1

    for i in xrange(ln):
        l = len(sets[i])
        dm[i] = [f, l]
        f *= l

    c = [None] * ln
    for i in range(ln):
        try:
            c[i] = sets[i][(n / dm[i][0] << 0) % dm[i][1]]
        except Exception as e:
            """ Division of 0, shouldn't happen """
        raise;

    return c
