# Langchain Essay Writter

This project uses langchain with Groq LLM and Langserve to implement a simple API from which a Streamlit client requests to get an essay written on a specific topic provided by the user. 

Live API [here](https://langserve-essay-writter-api.onrender.com/docs)

View Live Site [here](https://langserve-essay-writter.streamlit.app/)

# Essay Writter Running
![streamlit](./screenshots/streamlit.JPG)

# API 
![api docs](./screenshots/api.JPG)

# Setup
- Create virtual environment:  `python -m venv venv`
- Activate virtual environment: `call venv/Scripts/activate.bat` in cmd
- Install dependencies: `pip install -r requirements.txt`
- Create environment variables `LANGCHAIN_API_KEY` and `GROQ_API_KEY`. You can get your langchain api key from [here](https://smith.langchain.com/), and your groq api key from [here](https://console.groq.com/keys).
- Run app.py in a terminal using command `python app.py`
- In another terminal run client.py using comman `streamlit run client.py`


# Libraries
- Streamlit
- Langchain
- Langserve
- Langchain Groq
- Python-Dotenv


## Contact
 - LinkedIn: [Natan Asrat](https://linkedin.com/in/natan-asrat)
 - Gmail: nathanyilmaasrat@gmail.com
 - Telegram: [Natan Asrat](https://t.me/fail_your_way_to_success)
 - Youtube: [Natville](https://www.youtube.com/@natvilletutor)

