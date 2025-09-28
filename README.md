# Virtual Environment Setup
1) We will use *uv* package instead of *pip*
```
pip install uv
```
2) Initialize the workspace
```
uv init
```
3) Create the virtual environment
```
uv venv
```
4) Activate the virtual environment
```
.venv\Scripts\activate
```

# Install the dependencies
```
uv add -r requirements.txt
```
### or
```
uv pip install -r requirements.txt
```

# Credentials File
### Make sure to include the <u>*.env*</u> file in your workspace such as <u>*.env.example*</u>

