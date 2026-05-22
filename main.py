from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def Raiz(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"request": request})

@app.post("/verificar")
async def Usuario(request: Request,nombre: str =Form(...), password: int = Form(...)):
    if password == 1234 and nombre == "admin":
        return RedirectResponse(url="/usuario")
    
@app.post("/usuario")
async def Usuario(request: Request,nombre: str =Form(...), password: str = Form(...)):
    return templates.TemplateResponse(request=request, name="usuario.html")
