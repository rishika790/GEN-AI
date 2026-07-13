#from fastapi import FastAPi
#app = FastAPI()
#@app.get("/") ### "/" home index get function 
#def home():
    #return {"message": "Hello, World!"}



# #path parameter
# from fastapi import FastAPI
# app = FastAPI() 
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"user_id": user_id}


# #query parameter
# @app.get("/search")
# def search(name: str, age: int):
#     return {"name": name, "age": age}


#post method 
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()
# class student(BaseModel):
#     name: str
#     age: int

# @app.post("/student_data")
# def create_student(student: student):
#     return student 

# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.responses import HTMLResponse 

# app = FastAPI()
# @app.get("/", response_class=HTMLResponse)
# def home():
#     return """
#     <html>
#         <head>
#             <title>My App</title>
#         </head>
#         <body>
#             <h1>Welcome to My App</h1>
#             <p>This is a simple FastAPI app.</p>
#         </body>
#     </html>
#     """

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/hello")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )