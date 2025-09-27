''' Declaring routes and whatnot to use with fastapi '''

from fastapi import FastAPI
# Will import everythng here

app = FastAPI()

# Example endpoint for now
@app.get('/')
def read_root():
    return {"Hello": "World"}

''' TODO (endpoints/connections)
- Auth (Student ID or Admin to see everything)
- LLM requests + responses
- 
'''


