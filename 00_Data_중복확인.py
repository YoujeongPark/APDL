import pandas as pd
import os



path_dir_1 = r'E:\yjPark\00_ML_data\01_Velocity_Data_m_s\Velocity_2018'
path_dir_2 = r'E:\yjPark\00_ML_data\02_APDL_Data\2018_pln_data'


file_list_1 = os.listdir(path_dir_1)
file_list_2 = os.listdir(path_dir_2)

print(file_list_1)
print(file_list_2)

new_list1 = []
new_list2 = []

for listname1 in file_list_1:
    listname1 = listname1.replace(".dat","")
    #print(listname1)
    new_list1.append(listname1)


for listname2 in file_list_2:
    listname2 = listname2.replace('_d_2_RS.dat.out','')
    #print(listname2)
    new_list2.append(listname2)




result = set(new_list2) - set(new_list1)
print(result)
print(len(result))

result = set(new_list1) - set(new_list2)
print(result)
print(len(result))

#
# import os
# for name in result:
#     os.remove("E:\yjPark\\00_ML_data\\01_Velocity_Data_m_s\Velocity_2015\\"+ name  + ".dat")


