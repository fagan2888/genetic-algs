
import numpy as np
import pickle

""" Module to generate fake data to test the program. """

def make_pendulum(m, l, angle_0, t=10, sample_period=1e-2, fname="pendulum.pkl"):
    """ Simulate a pendulum with mass `m` and length `l` starting at
        angle `angle_0` relative to the vertical.

        Args:
            m: mass (in kg)
            l: length (in m)
            angle_0: initial angle (in radians)
            t: time to run the simulation (in seconds) (default=10)
            sample_period: time period of each sample (in seconds) (default=1e-2)
            fname: filename to save .pkl file to (default="pendulum.pkl")

        Outputs:
            pickled dictionary file with the following mappings:
            "x": x position of the pendulum (right is positive)
            "y": y position of the pendulum (up is positive)
            "sample_period": time per sample (in seconds)
    """
    # Solution to the system is theta = Acos(wt)
    g = 9.81

    times = np.arange(0, t, sample_period)

    angular_freq = np.sqrt(g / l)
    xs = []
    ys = []
    for time in times:
        angle = angle_0 * np.cos(angular_freq * time)

        x = l * np.sin(angle)
        y = l * np.cos(angle)

        xs.append(x)
        ys.append(y)

    xs = np.array(xs)
    ys = np.array(ys)

    # Save data
    data = {}
    data["arrays"] = {}
    data["arrays"]["t"] = times
    data["arrays"]["x"] = xs
    data["arrays"]["y"] = ys

    # Save sample period
    data["sample_period"] = sample_period

    pickle.dump(data, open(fname, "wb"))

def make_const(x, t=10, sample_period=1e-2, fname="const.pkl"):
    """ Simulate a constant.

        Args:
            x: constant
            t: time to run the simulation (in seconds) (default=10)
            fname: filename to save .pkl file to (default="const.pkl")

        Outputs:
            pickled dictionary file with the following mappings:
            "x": constant value
            "sample_period": time per sample (in seconds)
    """
    # Solution to the system is theta = Acos(wt)
    times = np.arange(0, t, sample_period)

    # TODO this is kinda dumb
    xs = np.array([x for _ in times])

    # Save data
    data = {}
    data["arrays"] = {}
    data["arrays"]["t"] = times
    data["arrays"]["x"] = xs

    # Save sample period
    data["sample_period"] = sample_period

    pickle.dump(data, open(fname, "wb"))

def make_linear(m, b, t=10, sample_period=1e-2, fname="linear.pkl"):
    """ Simulate a linear relationship with slope and y-intercept.

        Args:
            m: slope
            b: y-intercept
            t: time to run the simulation (in seconds) (default=10)
            fname: filename to save .pkl file to (default="const.pkl")

        Outputs:
            pickled dictionary file with the following mappings:
            "x": constant value
            "sample_period": time per sample (in seconds)
    """
    # Solution to the system is theta = Acos(wt)
    times = np.arange(0, t, sample_period)
    xs = np.array([m * time + b for time in times])

    # Save data
    data = {}
    data["arrays"] = {}
    data["arrays"]["t"] = times
    data["arrays"]["x"] = xs

    # Save sample period
    data["sample_period"] = sample_period

    pickle.dump(data, open(fname, "wb"))

def make_quadratic(a, b, c, t=10, sample_period=1e-2, fname="quadratic.pkl"):
    """ Simulate a quadratic relationship:

            at^2 + bt + c

        Args:
            a: degree-2 term
            b: degree-1 term
            c: degree-0 term
            t: time to run the simulation (in seconds) (default=10)
            fname: filename to save .pkl file to (default="const.pkl")

        Outputs:
            pickled dictionary file with the following mappings:
            "x": constant value
            "sample_period": time per sample (in seconds)
    """
    # Solution to the system is theta = Acos(wt)
    times = np.arange(0, t, sample_period)
    xs = np.array([a * time ** 2 + b * time + c for time in times])

    # Save data
    data = {}
    data["arrays"] = {}
    data["arrays"]["t"] = times
    data["arrays"]["x"] = xs

    # Save sample period
    data["sample_period"] = sample_period

    pickle.dump(data, open(fname, "wb"))

if __name__ == "__main__":
    make_pendulum(1, 10, 1, t=0.1)
    make_const(3, t=0.1)
    make_linear(5, 0, t=10, sample_period=1e-1)
    make_quadratic(4, 5, 2, t=10, sample_period=1e-1)
