import requests
ngrok_url = "https://77ca-34-105-60-98.ngrok-free.app"
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import chainlit as cl
import asyncio

@cl.on_message
async def main(message):
    print("################################################################################################")
    print(message.content)
    print("################################################################################################")
    response = requests.post(f"{ngrok_url}/generate", json={"text": message.content}) 
    print("-------------------------------------------------------------------------------------------------------------")
    print(response)
    
    
    response_text = response.json()["response"]

    await cl.Message(content=response.json()["response"]).send()