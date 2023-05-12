# -*- coding: utf-8 -*-


"""This program visualizes the posterior distribution of a beta-binomial model.
"""


import pymc as pm
import arviz as az


def coin_flip(trials=10, successes=5):
    """This """
    with pm.Model() as model:
        p = pm.Beta(
            "p",
            alpha=1,
            beta=1)

        obs = pm.Binomial(
            "obs",
            p=p,
            n=trials,
            observed=successes)

        idata = pm.sample()

    az.plot_posterior(
        data=idata,
        show=True)


def main():
    """Main function."""
    coin_flip()


if __name__ == "__main__":
    main()
