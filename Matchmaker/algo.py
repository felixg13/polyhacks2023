import csv

class Question():
    def __init__(self, type_de_question, reponse_pretendant, reponse_coup_de_coeur, importance):
        self.type_de_question = type_de_question
        self.reponse_pretendant = reponse_pretendant
        self.reponse_coup_de_coeur = reponse_coup_de_coeur
        self.importance = importance

    def __str__(self):
        return f"question de type: {self.type_de_question}, reponse du pretendant: {self.reponse_pretendant}, reponse du crush: {self.reponse_coup_de_coeur}, poids de la question: {self.importance}"


def evaluer_score_accord_desaccord(question: Question):
    attente = int(question.reponse_coup_de_coeur)
    reponse = int(question.reponse_pretendant)
    score = 5 - abs(attente - reponse)
    return float(score / 5)

def evaluer_score_choix_multiple(question: Question):
    score = 0
    for elem in question.reponse_pretendant:
        if elem in question.reponse_coup_de_coeur:
            score += 1
    return score / len(question.reponse_coup_de_coeur)

def evaluer_score_oui_non(question: Question):
    if question.reponse_coup_de_coeur == question.reponse_pretendant:
        return 1
    return 0

def main():
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        liste_de_reponse = [Question(int(row[0]), int(row[1]), int(row[2]), int(row[3])) for row in reader]
    score = 0
    denominateur_du_score = 0
    for i in range(len(liste_de_reponse)):
        question = liste_de_reponse[i]

        if int(question.type_de_question) == 0:
            score += evaluer_score_accord_desaccord(question) * question.importance
            denominateur_du_score += question.importance
            
        if int(question.type_de_question) == 1:
            score += evaluer_score_choix_multiple(question) * question.importance
            denominateur_du_score += question.importance
            
        if int(question.type_de_question) == 2:
            score += evaluer_score_oui_non(question) * question.importance            
            denominateur_du_score += question.importance

        print(i, "  ", question, "\n")

    score_final = int(score / denominateur_du_score *100)

    print("La compatibilité est de ", score_final,"%")
    pass



if __name__ == "__main__":
   main()