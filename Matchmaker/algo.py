from enum import Enum
import pandas as pd


# Create a list of Car objects from the dataframe
cars = [Car(make, model) for make, model in df.to_records(index=False)]

# Access the attributes of the first car object
print(cars[0].make)
print(cars[0].model)

class Question():
    def __init__(self, type_de_question, reponse_pretendant):
        self.type_de_question = type_de_question
        self.reponse_pretendant = reponse_pretendant
        self.reponse_coup_de_coeur = reponse_coup_de_coeur
        self.importance = importance

    def __str__(self):
#Do whatever you want here
        return f"question de type: {self.type_de_question}, reponse du pretendant: {self.reponse_pretendant}, reponse du crush: {self.reponse_coup_de_coeur}, poids de la question: {self.importance}"

def lirefichier(data):
    type_question: Type_de_question = 0 #definir a vec lecture du fichier
    rep1, rep2: int = 0,0 # definir avec lecture du fichier
    poids: int = 0
    return type_question, rep1, rep2, poids

def evaluer_score_accord_desaccord(question: Question) -> int:
    attente: int = question.reponse_coup_de_coeur
    reponse: int = question.reponse_pretendant
    score = 5 - abs(attente - reponse)
    return score / 5

def evaluer_score_choix_multiple(question: Question) -> int:
    score = 0
    for elem in question.reponse_pretendant:
        if elem in question.reponse_coup_de_coeur:
            score += 1
    return score / len(question.reponse_coup_de_coeur)

def evaluer_score_oui_non(question: Question) -> int:
    if question.reponse_coup_de_coeur == question.reponse_pretendant:
        return 1
    return 0

def main():
    df = pd.read_csv("data.csv")
#for loop qui creer un objet par question
    liste_de_reponse = [Question() for i in range(7)]
    cars = [Car(make, model) for make, model in df.to_records(index=False)]
    score = 0
    denominateur_du_score = 0
    for i in range(len(liste_de_reponse)):
        question = liste_de_reponse[i]

        if question.type_de_question == 0:
            score += evaluer_score_accord_desaccord(question) * question.importance
            denominateur_du_score += question.importance
            
        if question.type_de_question == 1:
            score += evaluer_score_choix_multiple(question) * question.importance
            denominateur_du_score += question.importance
            
        if question.type_de_question == 2:
            score += evaluer_score_oui_non(question) * question.importance            
            denominateur_du_score += question.importance
        print(i, "  ", question, "/n")
    print((score/denominateur_du_score)*5)
    pass



if __name__ == "__main__":
   main()