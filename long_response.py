import random

R_EAT = "I don't anything yet, I was created resently!"


def unknown():
    responce = ['Please re-phrase that.',
                "...",
                "I don't undertand you..."][random.randrange(3)]
    return responce
