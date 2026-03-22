import os

class DefaultConfig:
    API_KEY = os.environ.get("MicrosoftAPIKey", "")
    ENDPOINT_URI = os.environ.get("MicrosoftAIServiceEndpoint", "")