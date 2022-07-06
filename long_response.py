import random

R_EATTING = ""

responses = {
    "chills": ["chills", "feel cold"],
    "vomiting": ["vomiting"],
    "fatigue": ["fatigue", "feeling overtired", "lingering tiredness", "feeling tired", "feeling weak",
                "feeling tired all the time", "feeling weak all the time", "lack of energy"],
    "continuous sneezing": ["continuous sneezing", "regular sneezing"],
    "high fever": ["high fever", "high temperature", "elevated body temperature", " hyperthermia",
                   "higher than normal body temperature", "pyrexia"],
    "cough": ["cough"],
    "sweating": ["sweating", "perspiration", "hyperhidrosis"],
    "weight loss": ["weight loss", "loosing weight", "lost weight", "lighter in terms of weight"],
    "headache": ["headache", "pain in the head", "migraine"],
    "breathlessness": ["breathlessness", "shortness of breath", "difficult breathing", "rapid breathing", "puffed",
                       "very fast, shallow breath", "feel breathless", "winded", "dyspnoea"],
    "nausea": ["nausea", "urge to vomit", "feel like i want to vomit", "feel like vomiting"],
    "swelled lymph nodes": ["swelled lymph nodes", "swollen lymph nodes"],
    "malaise": ["malaise", "feeling discomfort", "i don't feel fine", "feeling funny", "feeling unease",
                "feel like am falling sick", "feeling unwell", "i fill funny"],
    "muscle pain": ["muscle pain", "myalgia"],
    "diarrhoea": ["diarrhoea", "watery stools"],
    "abdominal pain": ["abdominal pain", "cramping", "feeling discomfort in the stomach", "tummy pain", "stomach pain"],
    "constipation": ["constipation"],
    "phlegm": ["phlegm", "thick mucus"],
    "loss of appetite": ["loss of appetite", " lack of appetite", "feel like not eating"],
    "chest pain": ["chest pain", "discomfort in the chest", "short stabbing in the chest",
                   "feeling unease in the chest", "feeling discomfort in the chest", "feeling pain in the chest"],
    "toxic look (typhos)": ["toxic look (typhos)", "toxic look", "typhos", "feeling lazy", "feeling smoky"],
    "throat irritation": ["throat irritation", "sore throat", "scratchiness ofd the throat", "irritation of the throat",
                          "pharyngitis", "throat is irritating"],
    "fast heart rate": ["fast heart rate", "rapid heartbeat", "tachycardia", "irregular heartbeat"],
    "runny nose": ["runny nose", "stuffy nose", "running nose"],
    "belly pain": ["belly pain"],
    "rusty sputum": ["rusty sputum", "reddish-brown sputum", "lobar pneumonia", "blood-stained sputum"],
    "redness of eyes": ["redness of eyes", "bloodshot eyes", "red eyes"],
    "yellowing of eyes": ["yellowing of eyes", "jaundice", "yellowing of the eyes", "eyes turn yellow", "eyes turned yellow"],
    "sinus pressure": ["sinus pressure", "sinus pain", "facial tenderness"],
}


def unknown():
    # response = [
    #     "Could you please re-phrase that?",
    #     "...",
    #     "Sounds about right",
    #     "What does that mean?"
    # ][random.randrange(4)]
    return 0


def grammar_resolver2symbolic(extpected, provided):
    pass
