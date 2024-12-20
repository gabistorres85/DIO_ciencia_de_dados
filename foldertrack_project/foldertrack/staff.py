import pandas as pd 

class Staf:
    def __init__(self,id_staff,category):
        self.id_staff = id_staff
        self.category = category
        self.df_staff = pd.DataFrame(columns=["id_staff","catgory"])

    def add_staff(self,id_staff,category):
        if id_staff in self.df_staff["id_staff"].values:
            print(f"Funcionário {id_staff} já está incluido na TLP.")
        else:
            new_record = {'id_staff':id_staff,'category':category}
            self.df_staff = pd.concat([self.df_staff,pd.DataFrame([new_record])],ignore_index=True)
            print (f"Funcionário : {id_staff}  Categoria: {category} - anexado.")

    def del_staff(self, id_staff):
        if id_staff in self.df_staff['id_staff'].values:
            self.df_staff = self.df_staff[self.df_staff["id_staff"] != id_staff]
            print(f"Paciente {id_staff} retirado da TLP.")

