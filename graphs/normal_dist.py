from scipy.stats import kstest, norm
my_data = norm.rvs(size=10)
print(my_data)
other = [72.934772, 73.228536, 74.50874, 73.655632, 74.716868, 74.804672, 58.75822, 74.793832, 74.642072, 73.112548]
print(other)
ks_statistic, p_value = kstest(other, 'norm')

if p_value > 0.05:
    print('normal distribution')
else:
    print('not a normal distribution')
print(ks_statistic, p_value)