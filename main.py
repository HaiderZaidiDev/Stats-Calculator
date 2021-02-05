import numpy
class Stats:
    def __init__(self):
        pass
    def variance(self):
        """Calculates variance given observations."""
        observations_raw = input("Observations: ").split()
        observations = [int(elem) for elem in observations_raw]
        observations_squared = sum([num**2 for num in observations])
        aggregate_squared = sum(observations)**2
        n = len(observations)
        mean = sum(observations)/n
        variance = (observations_squared - (aggregate_squared/n))/(n-1)
        print(f"Variance is: {variance}")
        return variance, mean

    def std(self):
        """Calculates standard deviation given observations."""
        variance, mean = self.variance()
        standard_deviation = variance**0.5
        print(f"Standard Deviation is: {standard_deviation}")
        return standard_deviation, mean

    def mad(self):
        """ Calculates Mean Absolute Deviation"""
        observations_raw = input("Observations: ").split()
        observations = [int(elem) for elem in observations_raw]
        n = len(observations)
        mean = sum(observations)/n
        deviations = [xi - mean for xi in observations]
        abs_deviations = [abs(xi) for xi in deviations]
        mad = sum(abs_deviations)/n
        print(f"Mean Absolute Deviation is: {mad}")
        return mad

    def coefficient_variation(self):
        """ Calculates the Coefficient of Variation"""
        std, mean = self.std()
        coefficient_variation = std/mean
        print(f"Coefficient of Variation is: {coefficient_variation}")
        return coefficient_variation

calculator = Stats()


