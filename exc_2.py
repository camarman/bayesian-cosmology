from numpy import mean, sqrt

Probe_data_Temp = [197.2,202.4,201.8,198.8,207.6,191.4,201.4,198.2,195.7,201.2] #in K
N = len(Probe_data_Temp)

#part b
T_ML = mean(Probe_data_Temp)
print("T_ML = ", round(T_ML, 1))
var = 25 #in K^2                   
sigma_T = sqrt(var/N)

#part c
#Confidence intervals for ½68.3

sigma_1_interval_min, sigma_1_interval_max = T_ML - sigma_T, T_ML + sigma_T

print("CL: 68.3%", [round(sigma_1_interval_min, 1), round(sigma_1_interval_max, 1)])
