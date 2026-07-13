### doctor >>>>>

from fastapi import FastAPI, Path, HTTPException, Request,Query
from fastapi.templating import Jinja2Templates

import json 
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def load_data():
    with open("patients.json") as file:
        data = json.load(file)
    return data


@app.get("/")
def index():
    return {"message": "welcome to fastapi"} 

@app.get("/about")
def about():
    return {"message": "we are learning about fastapi"}

@app.get("/view")
def view():
    return load_data() 

# @app.get("/my_dashboard/{patient_id}")
# def my_dashboard(patient_id: str):
#     patients_data = load_data()
#     return patients_data.get(patient_id, {"error": "Patient not found"})


@app.get("/patients_info/{patient_id}")
def patients_info(
    request: Request,
    patient_id: str = Path(
        ...,
        description="enter your patient id",
        example="P001"
    )
):
    patients_data = load_data()

    if patient_id not in patients_data:
        return templates.TemplateResponse(
            request=request,
            name="index.html"
        )

    return patients_data[patient_id]

# @app.get("/hello")
# async def home(request: Request):
#     return templates.TemplateResponse(
#         request=request,
#         name="index.html"
#     )


# def data_view(patients_id):
#     patients_data = load_data()
#     return patients_data[patients_id]
# print(data_view(patients_id = "P005"))

# path query parameter jo brave pe user name or pass dalte hi log in ho jata hai
@app.get("/sort")
def sort_data(sort_by: str = Query(..., description="age, weight, height, bmi"), order: str = Query('asc', description="age, weight, height, bmi")):
    data = load_data()
    sorted_list = ["age","height_cm","weight_kg","bmi"]
    if sort_by not in sorted_list:
        raise HTTPException(status_code=400, detail="Invalid sort parameter{sort_by}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order parameter{order}")
    sorted_order = 'desc' if order == 'desc' else 'asc'
    
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(sorted_order ))
    return sorted_data