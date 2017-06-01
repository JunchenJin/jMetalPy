from jmetal.algorithm.singleobjective.evolutionaryalgorithm import NonElitistEvolutionStrategy
from jmetal.core.solution import BinarySolution, FloatSolution
from jmetal.operator.mutation import Polynomial, BitFlip
from jmetal.problem.singleobjectiveproblem import OneMax, Sphere


def main():
    binary_example()
    print()
    float_example()
    print()
    run_as_a_thread()


def binary_example() -> None:
    bits = 512
    problem = OneMax(bits)
    algorithm = NonElitistEvolutionStrategy[BinarySolution, BinarySolution]\
        (problem, mu=1, lambdA=10, max_evaluations= 50000, mutation=BitFlip(1.0/bits))

    algorithm.run()
    result = algorithm.get_result()
    print("Algorithm: " + algorithm.get_name())
    print("Problem: " + problem.get_name())
    print("Solution: " + str(result.variables[0]))
    print("Fitness:  " + str(result.objectives[0]))


def float_example() -> None:
    variables = 10
    problem = Sphere(variables)
    algorithm = NonElitistEvolutionStrategy[FloatSolution, FloatSolution]\
        (problem, mu=10, lambdA=10, max_evaluations= 50000, mutation=Polynomial(1.0/variables))

    algorithm.run()
    result = algorithm.get_result()
    print("Algorithm: " + algorithm.get_name())
    print("Problem: " + problem.get_name())
    print("Solution: " + str(result.variables))
    print("Fitness:  " + str(result.objectives[0]))


def run_as_a_thread() -> None:
    variables = 10
    problem = Sphere(variables)
    algorithm = NonElitistEvolutionStrategy[FloatSolution, FloatSolution]\
        (problem, mu=10, lambdA=10, max_evaluations= 50000, mutation=Polynomial(1.0/variables))

    algorithm.start()
    print("Algorithm (running as a thread): " + algorithm.get_name())
    print("Problem: " + problem.get_name())
    algorithm.join()

    result = algorithm.get_result()

    print("Solution: " + str(result.variables))
    print("Fitness:  " + str(result.objectives[0]))

if __name__ == '__main__':
    main()