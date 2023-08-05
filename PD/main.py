from fastapi import FastAPI,Request,Form,Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from database import SessionLocal
import models

app=FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/templates/static",StaticFiles(directory="/study files/HTML/PD/templates/static"),name="static")

def get_db():
    db=None
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/home.html')
def home(request:Request,db:Session=Depends(get_db)):
    return templates.TemplateResponse("home.html",context={"request":request})    

@app.get('/clogin.html')
def login(request:Request,db:Session=Depends(get_db)):
    return templates.TemplateResponse("clogin.html",context={"request":request})

@app.get('/signup.html')
def sign(request:Request,db:Session=Depends(get_db)):
    return templates.TemplateResponse("signup.html",context={"request":request})

@app.post('/SignUp')
async def create(request:Request,db:Session=Depends(get_db),name:str=Form(...),phone:str=Form(...),email:str=Form(...),password:str=Form(...)):
    find = db.query(models.Customer).filter(models.Customer.phone==phone,models.Customer.status=="ACTIVE").first()
    if find is None:
        body = models.Customer(name=name,phone=phone,email=email,password=password,status="ACTIVE")
        db.add(body)
        db.commit()
        error = "Registered Successfully"
        json_compatible_item_data =jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error = "User Already exists"
        json_compatible_item_data =jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
        
@app.post('/lhome.html')
def auth(request:Request,db:Session=Depends(get_db),phone:str=Form(...),password:str=Form(...)):
    find = db.query(models.Customer).filter(models.Customer.phone==phone,models.Customer.password==password,models.Customer.status=="ACTIVE").first()
    if find is None:
        error="Incorrect Password"
        json_compatible_item_data =jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        return templates.TemplateResponse("/lhome.html",context={"request":request})
    
@app.post('/book')
def bookord(request:Request,db:Session=Depends(get_db),material:str=Form(...),mimg:str=Form(...),color:str=Form(...),size:str=Form(...),date:str=Form):
    find = db.query(models.Booking).filter(models.Booking.material==material,models.Booking.mimg==mimg,models.Booking.color==color,models.Booking.size==size,models.Booking.date==date)
    if find is None:
        body = models.Booking(material=material,mimg=mimg,color=color,size=size,date=date)
        db.add(body)
        db.commit()