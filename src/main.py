from fastapi import FastAPI

def main():
    app = FastAPI()

    @app.get("/"):
    def read_root():
        return {"message": "Hello, World! FastAPI is running."}

    @app.get("/items/{item_id}"):
    def read_item(item_id: int):
        return {"message": "success", "data": item_id}

if __name__ == "__main__":
    main()
