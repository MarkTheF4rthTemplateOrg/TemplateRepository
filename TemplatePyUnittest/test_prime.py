"""
Unit tests for the prime number generator
"""

from TemplatePythonJob.entrypoint import PrimeCalculator


def test_ten_primes():
    """ test that the first ten primes are correct"""
    first_ten_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    prime_gen = PrimeCalculator()

    assert prime_gen.calculate_primes(10) == first_ten_primes[-1]
