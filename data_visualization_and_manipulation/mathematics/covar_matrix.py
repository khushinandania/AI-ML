import numpy as np
import pandas as pd

df = pd.read_csv("/home/khushi/Desktop/khushi_module/sample_data.csv")
print(df)

covariance_matrix = df.cov()
print(covariance_matrix)

x=df.iloc[:,0]
y=df.iloc[:,1]
z=df.iloc[:,2]

n=len(x)

var_x = np.var(x,ddof=1)
var_y = np.var(y,ddof=1)
var_z = np.var(z,ddof=1)

mean_x =np.mean(x)
mean_y = np.mean(y)
mean_z = np.mean(z)


x_cen = x-mean_x
y_cen = y-mean_y
z_cen = z-mean_z

cov_xy = np.sum(x_cen * y_cen)/n-1
cov_xz = np.sum(x_cen * z_cen)/n-1
cov_yz = np.sum(z_cen * y_cen)/n-1


cov_matrix = np.array([
    [var_x ,cov_xy ,cov_xz],
    [cov_xy, var_y,cov_yz],
    [cov_xz ,cov_yz,var_z]
])

print(cov_matrix)
