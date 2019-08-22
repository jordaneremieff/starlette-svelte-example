from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware
from databases import Database

database = Database("sqlite:///example.db")


app = Starlette()
app.debug = True


@app.route("/high-scores/", methods=["GET", "POST"])
async def high_scores(request):

    if request.method == "POST":
        form = await request.form()
        query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
        await database.execute(query=query, values=form)
        return JSONResponse(dict(form))
    else:
        query = "SELECT * FROM HighScores"
        rows = await database.fetch_all(query=query)
        data = [dict(row) for row in rows]
        return JSONResponse(data)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.add_middleware(CORSMiddleware, allow_origins=["*"])
