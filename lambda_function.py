from mangum import Mangum
from mysite.asgi import application

# Mangum adapter wraps the ASGI application for AWS Lambda + API Gateway
handler = Mangum(application)
