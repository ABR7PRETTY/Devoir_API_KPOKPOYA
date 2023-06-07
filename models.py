from typing import List
from pydantic import BaseModel


class Categorie(BaseModel):
    nomCategorie:str

class Engins(BaseModel):
    categorie:Categorie
    immatriculation:str


class Proprietaire(BaseModel):
    nom:str
    type:str
    engins:Engins
    addresse:str

class Cotation(BaseModel):
    engins:Engins
    montant:int
    majoration:int
    
class Facture(BaseModel):
    proprietaire:Proprietaire
    cotaion:Cotation
    montant:int