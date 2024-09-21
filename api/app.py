from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn, os
from dotenv import load_dotenv
load_dotenv()


os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"]="langserve_routes"

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API server"
)


model = ChatGroq()
prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")

add_routes(
    app,
    prompt|model,
    path = "/essay"
)

if __name__=="__main__":
    uvicorn.run(app)
