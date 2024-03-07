from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.routers import user_routes

app = FastAPI()

# Configuración del middleware CORS para permitir cualquier acceso
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen (puedes especificar dominios permitidos en lugar de "*")
    allow_credentials=True,
    allow_methods=["*"],  # Permite cualquier método HTTP
    allow_headers=["*"],  # Permite cualquier encabezado HTTP
)

app.include_router(user_routes.router)

@app.get("/")
async def root():
    return {"Hello": "World"}