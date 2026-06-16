import scipy.stats as stats
import pandas as pd


def chi_square_test(group1, group2):
    """
    Chi-square test for categorical variables
    """
    table = pd.crosstab(group1, group2)

    chi2, p, dof, expected = stats.chi2_contingency(table)

    return {
        "test": "Chi-square",
        "statistic": chi2,
        "p_value": p
    }


def t_test(group1, group2):
    """
    Independent t-test for numerical variables
    """

    t_stat, p_value = stats.ttest_ind(
        group1,
        group2,
        equal_var=False
    )

    return {
        "test": "Independent t-test",
        "statistic": t_stat,
        "p_value": p_value
    }


def hypothesis_decision(p_value, alpha=0.05):

    if p_value < alpha:
        return "Reject H0"
    else:
        return "Fail to Reject H0"