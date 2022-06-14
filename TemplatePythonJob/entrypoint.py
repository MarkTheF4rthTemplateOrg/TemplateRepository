"""
This script is intended to test base implementations and should be deleted as soon as infrastructure is established
When run, this script will calculate a given amount of prime numbers, beginning at 2 for an input of 0
"""

import argparse
import copy
import logging.config

import yaml

with open('logging_conf.yaml') as conf_file:
    config = yaml.safe_load(conf_file.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)


class PrimeCalculator:
    """
    Responsible for handling calls to prime calculation
    """
    def calculate_primes(self, n, i=2, primes=()):
        """
        recursively tests if each number is a prime
        n: the number of primes left to calculate
        i: the number we have reached
        primes: the primes we have already found
        """

        # base case: we have calculated the last prime
        if n == 0:
            return i - 1

        for prime in primes:
            if i % prime != 0:
                continue

            return self.calculate_primes(n, i + 1, primes)

        # no divisions have succeeded, we have found another prime
        primes = (*primes, i)
        logging.debug(f"Found a prime, current prime list is now \n{str(primes)}\n")
        return self.calculate_primes(n - 1, i + 1, primes)


def build_namespace_argument_dict(namespace):
    """
    Returns a dictionary version of a namespace for more natural parsing
    """
    # Namespace is mutable, copy it before making changes
    dict_args = vars(copy.copy(namespace))

    # Remove the function paramter if it exists, as its not an actual parameter
    dict_args.pop('func', None)
    return dict_args


def build_arg_parser():
    """
    Create an argparser configuration for command line arguments
    """
    parser = argparse.ArgumentParser(
        description="Module for getting the nth prime"
    )
    parser.add_argument('-n', '--number', type=int, help="The nth prime to retrieve")

    return build_namespace_argument_dict(parser.parse_known_args()[0])


if __name__ == "__main__":
    arguments = build_arg_parser()
    argument_str = '\n'.join([f'--- {key} = {arg}' for key, arg in arguments.items()])
    logger.info(f"Prime calculator running with the following arguments: \n{argument_str}")

    prime_calc = PrimeCalculator()
    nth_prime = prime_calc.calculate_primes(arguments['number'])
    with open('prime.txt', 'w') as prime_file:
        prime_file.write(str(nth_prime))

    logging.info(f"COMPLETED RUN, the {arguments['number']}th prime is {nth_prime}")
