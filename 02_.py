import pandas as pd
import os

##APDL에서 받은 DATA를 사용해서
##Membrane stress와 bending stress만 추출하는 것을 바탕으로 총 PATH 7개의 응력을 추출해 내는것


#구해야할 변수
#path가 7개면 구해야 할 값은 7*2 = 14개
variable = 28
### 위의 값 바꾸어야함

#순서 [1, 10,11,12,13,14,2,3,4,5,6,7,8,9]

list_14 = [1, 10,11,12,13,14,2,3,4,5,6,7,8,9]

path_dir = 'E:\\yjPark\\00_ML_data\\02_APDL_Data\path_data\\2015_path_data'
firstfile_name = "2015_Result.csv"
secondfile_name = "2015_Result_version2.csv"



def sum_data_path7_pandas():
    #path_dir = "result.csv"

 #   path_dir = "E:\\yjPark\\2rd_data_output\\2st_python_code"
    read_excel = pd.read_csv(firstfile_name)
    file_list = read_excel['file_name'].values.tolist()

    print("read_excel.shape[0]",read_excel.shape[0])

    columns_data_list = []
    columns_data_list.append('file_name')

    for i in range(0, int(variable/2)):
        mem_name = "path" + str(i + 1) + "_membrane_SINT"
        ben_name = "path" + str(i + 1) + "_bending_SINT"

        columns_data_list.append(mem_name)
        columns_data_list.append(ben_name)

    new_excel = pd.DataFrame(columns=columns_data_list)

    for v, j in zip(range(0,int(read_excel.shape[0]/int(variable/2))),range(0, read_excel.shape[0],int(variable/2))):

        file_name = file_list[j]
        data = []

        data.append(file_name)

        for i ,k in zip(range(j+0,j+int(variable/2)) , range(0,int(variable/2))):
            #if "PATH" and str(k+1) in read_excel.iloc[i,1]:
            #print(i," " , k)

            #Path 검사해주는 것
            #if "PATH" in read_excel.iloc[i, 1] and str(k + 1) in read_excel.iloc[i, 1]:
            path_i_membrane_SINT = read_excel.iloc[i,2]
            #else:
            #    pass
            #    print("error")

            bending_stres_intensity = read_excel.iloc[i,6]

            data.append(path_i_membrane_SINT)
            data.append(bending_stres_intensity)

        #print(data)

        #print([data[i] for i in range(1,15)])
        #print("len data", len(data))
        #new_excel.loc[variable] = data
        #new_excel.loc[variable] = sum([file_name,[data[i] for i in range(1,14)]])
        #print("type",type([file_name, data[1], data[2], data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14]]))
        #new_excel.loc[v] = [file_name, data[1], data[2], data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14]]
        new_excel.loc[v] = data

        new_file_name = secondfile_name
        new_excel.to_csv(new_file_name, mode='w')
        # variable  = variable + 1
        # print(variable)



def apdl_membrane_bending_stress_get_to_excel():
    ####Pathdir 중요

    #path_dir = 'E:\\yjPark\\2rd_data_output\\path_data\\'
    file_list = os.listdir(path_dir)
    print(file_list)

    file_list_sort = file_list.sort()
    print(file_list_sort)

    if(file_list == file_list_sort):
        print("okayyyyyyy ")


    new_excel = pd.DataFrame(
        columns=['file_name','membrane_SINT','bending_SINT_I', 'bending_SINT_C', 'bending_SINT_O','bending_stres_intensity',
                 'membrane_SEQV',  'bending_SEQV_I','bending_SEQV_C','bending_SEQV_O'
                ])



    for i in range(0, len(file_list)):
        file_name = file_list[i]
        read_excel = pd.read_csv(path_dir + file_name, error_bad_lines=False)
        # print(read_excel)

        m_list = read_excel.iloc[7, 0]
        #print(read_excel.iloc[7, 0])
        m_list_split = m_list.split()
        membrane_SINT = m_list_split[3]
        membrane_SEQV = m_list_split[4]

        b_list_I_intensity = read_excel.iloc[14, 0]
        b_list_C_intensity = read_excel.iloc[15, 0]
        b_list_O_intensity = read_excel.iloc[16, 0]

        b_list_I_split = b_list_I_intensity.split()
        b_list_C_split = b_list_C_intensity.split()
        b_list_O_split = b_list_O_intensity.split()

        bending_SINT_I = b_list_I_split[4]
        bending_SINT_C = b_list_C_split[4]
        bending_SINT_O = b_list_O_split[4]

        bending_SEQV_I = b_list_I_split[5]
        bending_SEQV_C = b_list_C_split[5]
        bending_SEQV_O = b_list_O_split[5]


        if bending_SINT_I >= bending_SINT_C and bending_SINT_I >= bending_SINT_O:
            bending_stres_intensity = bending_SINT_I
        elif bending_SINT_C >= bending_SINT_I and bending_SINT_C >= bending_SINT_I:
            bending_stres_intensity = bending_SINT_C
        else:
            bending_stres_intensity = bending_SINT_O



        # print(bending_SINT_I)
        # print(bending_SINT_C)
        # print(bending_SINT_O)

        new_excel.loc[i] = [file_name, membrane_SINT, bending_SINT_I,bending_SINT_C,bending_SINT_O,bending_stres_intensity,
                            membrane_SEQV, bending_SEQV_I,bending_SEQV_C,bending_SEQV_O]
        new_file_name = firstfile_name
        new_excel.to_csv(new_file_name, mode='w')


if __name__ == "__main__":
    #apdl_membrane_bending_stress_get_to_excel()
    sum_data_path7_pandas()
