from numpy import mean, sqrt

deviation_data = [119, 119, 122, 121, 116] #in cm
N = len(deviation_data)

#part b
T_ML = mean(deviation_data)
var = 9 #in K^2                   
sigma_T = sqrt(var/N)
print("T_ML = ", round(T_ML, 1), "+\-", round(sigma_T, 2))

#part c
#Confidence intervals for ½68.3
sigma_1_interval_min, sigma_1_interval_max = T_ML - sigma_T, T_ML + sigma_T

print("CL: 68.3%", [round(sigma_1_interval_min, 1), round(sigma_1_interval_max, 1)])
