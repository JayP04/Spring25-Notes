# import numpy as np


# mor_vals_ku_net = [49.774 , 51.928  , 51.901 , 51.898 ,60.872]
# aft_vals = [80.863,65.928, 56.454,60.408]
# eve_vals = [66.750, 56.266 , 63.646 , 71.813 , 62.526 , 61.305 , 64.323 , 60.843  ]



# mean_mor = np.mean(mor_vals_ku_net)
# mean_aft = np.mean(aft_vals)
# mean_eve = np.mean(eve_vals)


# std_mor_vals = np.std(mor_vals_ku_net)
# std_aft_vals = np.std(aft_vals)
# std_eve_vals = np.std(eve_vals)


# print("morning mean by Jayhawk network: ", mean_mor)
# print("morning std by Jayhawk network: ", std_mor_vals)
# print("afternoon mean: ", mean_aft)
# print("afternoon std: ", std_aft_vals)
# print("evening mean: ", mean_eve)
# print("evening std: ", std_eve_vals)

from scipy.stats import binom

# Parameters
N = 20
p_active = 0.25

# Probability that more than 10 users are active
p_more_than_10 = 1 - binom.cdf(10, N, p_active)

print(f"Probability more than 10 users are active: {p_more_than_10:.4f}")