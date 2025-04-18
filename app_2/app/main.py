from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint
from app.missing_number import MissingNumber

app = FastAPI()

# Modelo para validar el input
class ExtractRequest(BaseModel):
    number: conint(ge=1, le=100)  

@app.post("/extract")
def extract_number(req: ExtractRequest):
    try:
        mn = MissingNumber()
        mn.extract(req.number)
        missing = mn.find_missing()
        return {"faltante": missing}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
