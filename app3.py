from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib
from fastapi import Form

app=FastAPI()
model=joblib.load("model2.pkl")


HTML="""<!DOCTYPE html>
<html>
<head>
    <title>HOUSE-PRICE-PREDICTOR</title>
</head>
<body>
    <p>BOSTON HOUSE-PRICE-ESTIMATOR</p>
    <form method="post" action="/predict">
        <label>crime-rate</label><br>
        <input name="crim" placeholder="E.g 0.000632" type="number" step="any"><br><br>
        <label>Proportion of residential land zooned for over 25,000 sq ft</label><br>
        <input name="zn" placeholder="E.g 18.0" type="number" step="any"><br><br>
        <label>Proportion of non-retail bussines acres per town</label><br>
        <input name="indus" placeholder="Eg 2.18" type="number" step="any"><br><br>
        <label>Charles River Dummy variable</label><br>
        <input name="chas" placeholder="Eg 3" type="number" step="any"><br><br>
        <label>Average number of rooms per dwelling</label><br>
        <input name="rm" placeholder="Eg 7.147" type="number" step="any"><br><br>
        <label>Nitirc oxides concentration</label><br>
        <input name="nox" placeholder="E.g 0.458" type="number" step="any"><br><br>
        <label> Age(Proportion of owner occupied units prior to 1940)</label><br>
        <input name="age" placeholder="Eg 65.2" type="number" step="any"><br><br>
        <label>Weighet distances to five Boston Employee Centers</label><br>
        <input name="dis" placeholder="Eg 4.9671" type="number" step="any"><br><br>
        <label>index of accessibility to radial highways</label><br>
        <input name="rad" placeholder="Eg 1" type="number" step="any"><br><br>
        <label>Tax per $10000</label><br>
        <input name="tax" placeholder="Eg  296" type="number" step="any"><br><br>
        <label>Pupil-teacher ratio by town</label><br>
        <input name="ptratio" placeholder="Eg 15.3" type="number" step="any"><br><br>
        <label>proportion of blacks by town</label><br>
        <input type="number" name="b" placeholder="Eg 396.90" step="any"><br><br>
        <label>lower status of the population</label><br>
        <input type="number" name="lstat" placeholder="eg 5.33" step="any"><br><br>

        <button type="submit">Predict Price</button><br>
    </form>
    {results}
</body>
</html>"""

@app.get("/",response_class=HTMLResponse)
def home():
    return HTML.format(result="")

@app.post("/predict", response_class=HTMLResponse)
def predict(crim:float=Form(...), zn:float=Form(...), indus:float=Form(...),
            chas:float=Form(...), nox:float=Form(...), rm:float=Form(...),
            age:float=Form(...), dis:float=Form(...), rad:float=Form(...),
            tax:float=Form(...), ptratio:float=Form(...), b:float=Form(...),
            lstat:float=Form(...)):
    X = np.array([[crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]])
    price = model.predict(X)[0]
    return HTML.format(results=f"<h3>The estimated price is {price*1000}$ </h3>")
