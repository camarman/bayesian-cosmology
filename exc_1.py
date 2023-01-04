from numpy import mean, sqrt

Probe_data_Temp = [191.9,201.6,206.1,200.4,203.2,201.6,196.5,199.5,194.1,202.4] #in K
N = len(Probe_data_Temp)

#part b
T_ML = mean(Probe_data_Temp)
print("T_ML = ", round(T_ML, 1))
var = 25 #in K^2                   
sigma_T = sqrt(var/N)

#part c
#Confidence intervals for 68.3%, 95.4% and 99% corressponding to 1, 2, 2.57 sigma_T
sigma_1_interval_min, sigma_1_interval_max = T_ML - sigma_T, T_ML + sigma_T
sigma_2_interval_min, sigma_2_interval_max = T_ML - 2*sigma_T, T_ML + 2*sigma_T
sigma_3_interval_min, sigma_3_interval_max = T_ML - 2.57*sigma_T, T_ML + 2.57*sigma_T

print("CL: 68.3%", [round(sigma_1_interval_min, 1), round(sigma_1_interval_max, 1)])
print("CL: 95.4%", [round(sigma_2_interval_min, 1), round(sigma_2_interval_max, 1)])
print("CL: 99%", [round(sigma_3_interval_min, 1), round(sigma_3_interval_max, 1)])

