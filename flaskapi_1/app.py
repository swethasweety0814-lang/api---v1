from fastapi import FastAPI
app= FastAPI()
@app.get("/display/{userid}")
def view():
    return "hello swetha Congragulation"

