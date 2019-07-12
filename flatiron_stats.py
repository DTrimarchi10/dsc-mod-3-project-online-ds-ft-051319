import numpy as np
import scipy.stats as stats

def welch_t(a, b):

    """ Calculate Welch's t statistic for two samples. """
    
    #Convert to numpy arrays in case lists are passed in
    a = np.array(a)
    b = np.array(b)

    numerator = a.mean() - b.mean()

    # “ddof = Delta Degrees of Freedom”: the divisor used in the calculation is N - ddof,
    #  where N represents the number of elements. By default ddof is zero.

    denominator = np.sqrt(a.var(ddof=1)/a.size + b.var(ddof=1)/b.size)

    return np.abs(numerator/denominator)

def welch_df(a, b):

    """ Calculate the effective degrees of freedom for two samples. This function returns the degrees of freedom """
    
    #Convert to numpy arrays in case lists are passed in
    a = np.array(a)
    b = np.array(b)

    s1 = a.var(ddof=1)
    s2 = b.var(ddof=1)
    n1 = a.size
    n2 = b.size

    numerator = (s1/n1 + s2/n2)**2
    denominator = (s1/ n1)**2/(n1 - 1) + (s2/ n2)**2/(n2 - 1)

    return numerator/denominator


def p_value_welch_ttest(a, b, two_sided=False):
    """Calculates the p-value for Welch's t-test given two samples.
    By default, the returned p-value is for a one-sided t-test.
    Set the two-sided parameter to True if you wish to perform a two-sided t-test instead.
    """
    
    t = welch_t(a, b)
    df = welch_df(a, b)

    p = 1-stats.t.cdf(np.abs(t), df)

    if two_sided:
        return 2*p
    else:
        return p
    
    
#function to calculate Cohen's d which provides effect size
def cohens_d(df1, df2):
    """Calculates the effect size for Cohen's 'd' test given two samples.
    """
    mean_diff = np.mean(df1) - np.mean(df2)
    n1, n2 = len(df1)-1, len(df2)-1
    var1, var2 = np.var(df1,ddof=1), np.var(df2,ddof=1)
    
    pooled_var = (n1*var1 + n2*var2)/(n1 + n2)
    
    d = mean_diff/(pooled_var**0.5)
    
    return abs(d)


def get_sample(df, sample_size):
    """Returns a random choice sample of sample_size from the data.
    Replacement is True
    """
    return np.random.choice(df, size=sample_size, replace=True)


# function to get sampling distribution
def get_sampling_means(df, num_samples=500, sample_size=50):
    """Returns sampling means for samples taken from the given data.
    The number of samples taken is num_samples.
    The size of each sample is sample_size.
    """
    sample_means = [] 
    for i in range(num_samples):
        sample = get_sample(df, sample_size)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)        
    return sample_means