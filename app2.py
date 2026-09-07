from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib, numpy as np

app = FastAPI()
model = joblib.load("model2.pkl")

HTML = """
<form method='post' action='/predict'>
  crim: <input name='crim'><br>
  zn: <input name='zn'><br>
  indus: <input name='indus'><br>
  chas: <input name='chas'><br>
  nox: <input name='nox'><br>
  rm: <input name='rm'><br>
  age: <input name='age'><br>
  dis: <input name='dis'><br>
  rad: <input name='rad'><br>
  tax: <input name='tax'><br>
  ptratio: <input name='ptratio'><br>
  b: <input name='b'><br>
  lstat: <input name='lstat'><br>
  <button type='submit'>Predict Price</button>
</form>
{result}
"""

@app.get("/", response_class=HTMLResponse)
def home(): return HTML.format(result="")

@app.post("/predict", response_class=HTMLResponse)
def predict(crim:float=Form(...), zn:float=Form(...), indus:float=Form(...),
            chas:float=Form(...), nox:float=Form(...), rm:float=Form(...),
            age:float=Form(...), dis:float=Form(...), rad:float=Form(...),
            tax:float=Form(...), ptratio:float=Form(...), b:float=Form(...),
            lstat:float=Form(...)):
    X = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    price = model.predict(X)[0]
    return HTML.format(result=f"<h2>Predicted Price: ${price*1000:.2f}</h2>")