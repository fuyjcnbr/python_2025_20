from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import numpy as np


class Item(BaseModel):
    text: str

_labels = ["good", "bad", "ugly"]

app = FastAPI()


@app.get("/")
def root():
    return {"message": "text classifier"}

classifier = pipeline("zero-shot-classification", model="roberta-large-mnli")

@app.post("/get_text_tonality/")
def predict(item: Item):
    c = classifier(item.text, _labels)
    i = np.argmax(c["scores"])
    label = c["labels"][i]
    return f"most probable tonality is {label}"
