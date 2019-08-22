import asyncio
from databases import Database


async def main() -> None:
    database = Database("sqlite:///example.db")
    await database.connect()

    query = """CREATE TABLE HighScores (id INTEGER PRIMARY KEY, name VARCHAR(100), score INTEGER)"""
    await database.execute(query=query)

    query = "INSERT INTO HighScores(name, score) VALUES (:name, :score)"
    values = [
        {"name": "Daisy", "score": 92},
        {"name": "Neil", "score": 87},
        {"name": "Carol", "score": 43},
    ]
    await database.execute_many(query=query, values=values)

    await database.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
