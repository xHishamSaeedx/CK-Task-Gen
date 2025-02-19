# pydantic_ai.models.groq

## Setup

For details on how to set up authentication with this model, see model configuration for Groq.

GroqModelName module-attribute
GroqModelName = Literal[
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview",
    "llama-3.1-70b-specdec",
    "llama-3.1-8b-instant",
    "llama-3.2-1b-preview",
    "llama-3.2-3b-preview",
    "llama-3.2-11b-vision-preview",
    "llama-3.2-90b-vision-preview",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
    "gemma-7b-it",
]
Named Groq models.
See the Groq docs for a full list.
GroqModel dataclass
Bases: Model
A model that uses the Groq API.
Internally, this uses the Groq Python client to interact with the API.
Apart from __init__, all methods are private or match those of the base class.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py
__init__
__init__(
    model_name: GroqModelName,
    *,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncClient | None = None
)
Initialize a Groq model.
Parameters:
Name Type Description Default
model_name GroqModelName The name of the Groq model to use. List of model names available here. required
api_key str | None The API key to use for authentication, if not provided, the GROQ_API_KEY environment variable will be used if available. None
groq_client AsyncGroq | None An existing AsyncGroq client to use, if provided, api_key and http_client must be None. None
http_client AsyncClient | None An existing httpx.AsyncClient to use for making HTTP requests. None
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py
GroqAgentModel dataclass
Bases: AgentModel
Implementation of AgentModel for Groq models.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py
GroqStreamedResponse dataclass
Bases: StreamedResponse
Implementation of StreamedResponse for Groq models.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py

### GroqModelName module-attribute

GroqModelName = Literal[
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "llama3-groq-70b-8192-tool-use-preview",
    "llama3-groq-8b-8192-tool-use-preview",
    "llama-3.1-70b-specdec",
    "llama-3.1-8b-instant",
    "llama-3.2-1b-preview",
    "llama-3.2-3b-preview",
    "llama-3.2-11b-vision-preview",
    "llama-3.2-90b-vision-preview",
    "llama3-70b-8192",
    "llama3-8b-8192",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
    "gemma-7b-it",
]

Named Groq models.
See the Groq docs for a full list.

### GroqModel dataclass

Bases: Model
A model that uses the Groq API.
Internally, this uses the Groq Python client to interact with the API.
Apart from __init__, all methods are private or match those of the base class.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py
__init__
__init__(
    model_name: GroqModelName,
    *,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncClient | None = None
)
Initialize a Groq model.
Parameters:
Name Type Description Default
model_name GroqModelName The name of the Groq model to use. List of model names available here. required
api_key str | None The API key to use for authentication, if not provided, the GROQ_API_KEY environment variable will be used if available. None
groq_client AsyncGroq | None An existing AsyncGroq client to use, if provided, api_key and http_client must be None. None
http_client AsyncClient | None An existing httpx.AsyncClient to use for making HTTP requests. None
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py

#### __init__

__init__(
    model_name: GroqModelName,
    *,
    api_key: str | None = None,
    groq_client: AsyncGroq | None = None,
    http_client: AsyncClient | None = None
)

Initialize a Groq model.
Parameters:
Name Type Description Default
model_name GroqModelName The name of the Groq model to use. List of model names available here. required
api_key str | None The API key to use for authentication, if not provided, the GROQ_API_KEY environment variable will be used if available. None
groq_client AsyncGroq | None An existing AsyncGroq client to use, if provided, api_key and http_client must be None. None
http_client AsyncClient | None An existing httpx.AsyncClient to use for making HTTP requests. None
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py

### GroqAgentModel dataclass

Bases: AgentModel
Implementation of AgentModel for Groq models.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py

### GroqStreamedResponse dataclass

Bases: StreamedResponse
Implementation of StreamedResponse for Groq models.
Source code in pydantic_ai_slim/pydantic_ai/models/groq.py

