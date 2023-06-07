from fastapi import FastAPI
from typing import List
from models import Engins, Categorie, Proprietaire, Facture

app = FastAPI()

engins = [] 

@app.get("/category/{category}")
def get_engins_by_category(category: str) -> List[Engins]:
    cat_engins = [engin for engin in engins if engin.category == category]
    return cat_engins

@app.get("/owner/{owner}")
def get_engins_by_owner(owner: str) -> List[Engins]:
    prop_engins = [engin for engin in engins if engin.owner == owner]
    return prop_engins

@app.get("/bills/{owner}")
def get_bills_by_owner(owner: str) -> List[str]:
    bills = [engin.immatriculation for engin in engins if engin.owner == owner]
    return bills