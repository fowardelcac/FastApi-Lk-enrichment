from fastapi import FastAPI
from googlesearch import search


def search_api(text: str) -> str:
    site_base: str = "site:linkedin.com "
    query: str = site_base + text
    results = list(search(query, num=5, stop=5, pause=2))
    return results[0] if results else "No se encontraron resultados"


app = FastAPI()


@app.get("/linkedin_enrichment")
async def get_linkedin_url(text: str):
    return {
        "Profile URL": search_api(text),
    }
