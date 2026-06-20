from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI is running."}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"message": "success", "data": item_id}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# OLD STUFF FROM THE PREVIOUS APPLICATION THAT I BUILT:
# import logging
# from controller.MemoryController import MemoryController
# from controller.BotController import BotController
#
# from gemini.gemini_ext import GeminiExt
# from linkedin.linkedin_ext import LinkedInExt
# from dotenv import load_dotenv
# import os
#
#
# def main():
#     running = True
#     load_dotenv()
#
#     # TODO:
#     # need to set this up in a way that wil lmake it easier down the road but for now we will just use this here
#     os.makedirs("logs", exist_ok=True)
#     logging.basicConfig(
#         filename="logs/bot_logs.log",
#         level=logging.INFO,
#         format="[%(levelname)s] %(asctime)s - %(message)s",  # This defines the structure
#         datefmt="%Y-%m-%d %H:%M:%S",
#     )
#
#     controller = BotController()
#
#     while running and controller:
#         user_input = input("Press Enter to Start")
#         if user_input == "##quit":
#             running = False
#
#         if running:
#             controller.start()
#
#
# if __name__ == "__main__":
#     main()
