str_ = "PI,KI,AdkesmaAkpem,Kastrat,Pengmas,Senbud,Olahraga,Keilmuan,PSDM,PTI,Bismit,Media,Humas"
str_list = str_.split(",")
for i in str_list:
    print(f'<option value="{i.lower()}">{i}</option>')