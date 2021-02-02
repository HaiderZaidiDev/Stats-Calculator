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
        variance = (observations_squared - (aggregate_squared/n))/(n-1)
        print(f"Variance is: {variance}")
        return variance

    def std(self):
        """Calculates standard deviation given observations."""
        variance = self.variance()
        standard_deviation = variance**1/2
        print(f"Standard Deviation is: {standard_deviation}")
        return standard_deviation


calculator = Stats()
calculator.std()

