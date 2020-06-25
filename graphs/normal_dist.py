from scipy.stats import kstest, norm
my_data = norm.rvs(size=10)
print(my_data)
other = [57.80901449,
93.18522917,
84.32681944,
112.7376877,
87.94473145]
print(other)
ks_statistic, p_value = kstest(other, 'norm')

if p_value > 0.05:
    print('normal distribution')
else:
    print('not a normal distribution')
print(ks_statistic, p_value)