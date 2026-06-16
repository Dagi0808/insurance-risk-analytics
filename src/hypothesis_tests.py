import scipy.stats as stats


def chi_square_test(group1, group2):
    table = [
        group1,
        group2
    ]

    chi2, p, dof, expected = stats.chi2_contingency(table)

    return p



def t_test(group1, group2):

    statistic, p = stats.ttest_ind(
        group1,
        group2,
        equal_var=False
    )

    return p



def decision(p_value, alpha=0.05):

    if p_value < alpha:
        return "Reject H0"

    return "Fail to reject H0"