# Local Virtual Environment Setup
**1) We will use *uv* package instead of *pip***
```
pip install uv
```
**If you have *pyproject.toml* file, run the following command and skip the steps 2, 3 and 5.**
```
uv sync
```
**2) Initialize the workspace**
```
uv init
```
**3) Create the virtual environment**
```
uv venv
```
**4) Activate the virtual environment**
```
.venv\Scripts\activate
```
**5) Install the dependencies**
```
uv add -r requirements.txt
```
### or
```
uv pip install -r requirements.txt
```

# Credential File
### Make sure to include the <u>*.env*</u> file in your workspace such as <u>*.env.example*</u>


# Setup on AWS
**Note**: You don't need the Credential file here on AWS
### AWS Services
* **Amazon Bedrock**
<br>You have to request access to **Nova Lite Model** from bedrock *Model access* page
* **S3**
* **Lambda Function** (*lambda_function.py* file)
<br> You have to add the layer **_python.zip_** to the function.
* **API Gateway**
<br> Goto *Integration request settings -> Mapping templates*:
<br> **_Content type_**: application/json
<br> **_Template body_**: {"uri": "$input.params('uri')"}
<br> The API accepts the uri of the image that will be processed as a parameter, such as {"uri": "s3://nova-bedrock/corps2.webp"}.
<br> The accepted image formats are **png, jpeg, gif and webp**
<br> **_Our API_**: https://32f9abkqtk.execute-api.us-west-2.amazonaws.com/v1/report-gen

