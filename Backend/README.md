-- RUN Command 
```
uv run uvicorn fastapi_uv_project.main:app --reload
```
uv run uvicorn main:app --reload --app-dir source
```
-- sending data through url

```
http://127.0.0.1:8000/predicts?q=apple,banana,mango
```