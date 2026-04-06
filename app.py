from fastapi import FastAPI,Request,Form
import joblib
from fastapi.responses import HTMLResponse
import pandas as pd
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
#load the model
model=joblib.load('clv.pkl')
#import FastApi
app=FastAPI()
templates=Jinja2Templates(directory='templates')
@app.get('/',response_class=HTMLResponse)
def home(request:Request):
      return templates.TemplateResponse('index.html',{'request':request})
@app.post('/')
def predict(
      request: Request,
      Age:int=Form(...),
      Gender:str=Form(...),
      City:str=Form(...),
      Product_Category:str=Form(...),
      Unit_Price:float=Form(...),
      Quantity:int=Form(...),
      Discount_Amount:float=Form(...),
      Payment_Method:str=Form(...),
      Device_Type:str=Form(...),
      Session_Duration_Minutes:int=Form(...),
      Pages_Viewed:int=Form(...),
      Is_Returning_Customer:bool=Form(...),
      Delivery_Time_Days:int=Form(...),
      Customer_Rating:int=Form(...),
):
      data = pd.DataFrame([{
        "Age": Age,
        "Gender": Gender,
        "City": City,
        "Product_Category": Product_Category,
        "Unit_Price": Unit_Price,
        "Quantity": Quantity,
        "Discount_Amount": Discount_Amount,
        "Payment_Method": Payment_Method,
        "Device_Type": Device_Type,
        "Session_Duration_Minutes": Session_Duration_Minutes,
        "Pages_Viewed": Pages_Viewed,
        "Is_Returning_Customer": Is_Returning_Customer,
        "Delivery_Time_Days": Delivery_Time_Days,
        "Customer_Rating": Customer_Rating
    }])
      prediction = model.predict(data)

    # RETURN SAME PAGE with result
      return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": prediction[0]
        }
    )
