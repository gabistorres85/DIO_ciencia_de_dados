import pandas as pd

class Records:
    def __init__ (self, id_micro,id_family):
        self.id_micro = id_micro
        self.id_family = id_family
        records = {"id_micro":self.id_micro,"id_family":id_family}
        self.df_records = pd.DataFrame(columns=["id_micro", "id_family", "cns"])
    
    def add_patient(self,id_micro,id_family,cns):
        if len(cns) != 15:
            print("CNS inválido!")
        if cns in self.df_records['cns'].values:
            print(f"Paciente {cns} já está anexado ao prontuário.")
        else : 
            new_record = {"id_micro":id_micro,"id_family":id_family, "cns":cns}
            self.df_records= pd.concat([self.df_records,pd.DataFrame([new_record])],ignore_index=True)
            print (f"Paciente {cns} inserido ao prontuário {id_micro}.{id_family}.")
    def del_patient(self,id_micro,id_family,cns):
        if cns in self.df_records['cns'].values:
            self.df_records = self.df_records[self.df_records['cns'].values != cns]
            print(f"Paciente {cns} retirado do prontuário {id_micro}:{id_family}")
        else:
            print(f"Paciente {cns} não faz parte do prontuário.")
    def status (self,id_micro,id_family):
        print("Status dos registros:")
        print(self.df_records)
