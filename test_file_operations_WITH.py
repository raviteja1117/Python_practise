
ece_info_path = r"C:\Users\SUMANTH\Desktop\college\ECE\Ece_data.txt"

EEE_info_path = r"C:\Users\SUMANTH\Desktop\college\EEE\EEE_data.txt"
CSE_info_path = r"C:\Users\SUMANTH\Desktop\college\CSE\Cse_data.txt"
MEC_info_path = r"C:\Users\SUMANTH\Desktop\college\MEC\Mec_data.txt"

with open(ece_info_path) as ece:
    content = ece.readlines()
    print(content)

with open(EEE_info_path,mode="w+") as eee:
    for line in content:
        eee.writelines(line)

with open(CSE_info_path,mode="w+") as cse:
    count=0
    # write 6 lines
    for line in content:
        count=count+1
        if count<6:
            cse.writelines(line)
        else:
            break

with open(MEC_info_path,mode="w+") as mec:
    for line in content:
        mec.writelines(line)
