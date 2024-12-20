import pandas as pd

class Records:
    def __init__ (self, id_micro,id_family):
        self.id_micro = id_micro
        self.id_family = id_family
        records = {"id_micro":self.id_micro,"id_family":id_family}
        df_records = pd.DataFrame(records)
    
    def add_patient(self,id_micro,id_family,cns):
        if len(cns) != 15:
            print("CNS inválido!")
        if cns in self.records:
            print(f"Paciente {cns} já está anexado ao prontuário.")
        else : 
            self.records[,cns]={"id_micro":id_micro,"id_family":id_family}
            print (f"Paciente {cns} inserido ao prontuário {id_micro}.{id_family}.")
    def del_patient(self,id_micro,id_family,cns):
        if cns in self.records:
            del self.records[cns]
            print(f"Paciente {cns} retirado do prontuário {id_micro}:{id_family}")
        else:
            print(f"Paciente {cns} não faz parte do prontuário.")
    def status (self,id_micro,id_family):
        pass
