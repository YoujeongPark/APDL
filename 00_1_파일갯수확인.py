import pandas as pd
import os



file_list = os.listdir('E:\\yjPark\\00_ML_data\\01_Velocity_Data_m_s\\')
print(file_list)

for name in file_list:
    file_list = os.listdir('E:\\yjPark\\00_ML_data\\01_Velocity_Data_m_s\\' + name)
    print(name ,"------" ,len(file_list))


#######################################
file_list = os.listdir('E:\\yjPark\\00_ML_data\\02_APDL_Data\path_data')
print(file_list)

for name in file_list:
    file_list = os.listdir('E:\\yjPark\\00_ML_data\\02_APDL_Data\path_data\\' + name)
    print(name ,"------" ,len(file_list))



#######################################
file_list = os.listdir('E:\\yjPark\\00_ML_data\\02_APDL_Data\\pln_data')
print(file_list)

for name in file_list:
    file_list = os.listdir('E:\\yjPark\\00_ML_data\\02_APDL_Data\\pln_data\\' + name)
    print(name ,"------" ,len(file_list))

