try:
    from unittest import mock
except ImportError:
    import mock

try:
    import itertools
    from itertools import combinations_with_replacement
except ImportError:
    import itertools

    def combinations_with_replacement(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        for indices in itertools.product(range(n), repeat=r):
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)

    itertools.combinations_with_replacement = combinations_with_replacement

__all__ = ['mock', 'itertools']
