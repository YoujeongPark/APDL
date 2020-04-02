import pandas as pd
import os

##APDL에서 받은 DATA를 사용해서
##Membrane stress와 bending stress만 추출하는것

new_file_name = "2016_Result.csv"
path_dir = 'E:\yjPark\\00_ML_data\\02_APDL_Data\\path_data\\2016_path_data\\'

def apdl_membrane_bending_stress_get_to_excel():

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

        new_excel.to_csv(new_file_name, mode='w')

if __name__ == "__main__":
    apdl_membrane_bending_stress_get_to_excel()
