# pydantic_ai.exceptions

ModelRetry
Bases: Exception
Exception raised when a tool function should be retried.
The agent will return the message to the model and ask it to try calling the function/tool again.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
The message to return to the model.
UserError
Bases: RuntimeError
Error caused by a usage mistake by the application developer — You!
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
Description of the mistake.
AgentRunError
Bases: RuntimeError
Base class for errors occurring during an agent run.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
The error message.
UsageLimitExceeded
Bases: AgentRunError
Error raised when a Model's usage exceeds the specified limits.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
UnexpectedModelBehavior
Bases: AgentRunError
Error caused by unexpected Model behavior, e.g. an unexpected response code.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
Description of the unexpected behavior.
body instance-attribute
body: str | None = dumps(loads(body), indent=2)
The body of the response, if available.

### ModelRetry

Bases: Exception
Exception raised when a tool function should be retried.
The agent will return the message to the model and ask it to try calling the function/tool again.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
The message to return to the model.

#### message instance-attribute

message: str = message

The message to return to the model.

### UserError

Bases: RuntimeError
Error caused by a usage mistake by the application developer — You!
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
Description of the mistake.

#### message instance-attribute

message: str = message

Description of the mistake.

### AgentRunError

Bases: RuntimeError
Base class for errors occurring during an agent run.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
The error message.

#### message instance-attribute

message: str = message

The error message.

### UsageLimitExceeded

Bases: AgentRunError
Error raised when a Model's usage exceeds the specified limits.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py

### UnexpectedModelBehavior

Bases: AgentRunError
Error caused by unexpected Model behavior, e.g. an unexpected response code.
Source code in pydantic_ai_slim/pydantic_ai/exceptions.py
message instance-attribute
message: str = message
Description of the unexpected behavior.
body instance-attribute
body: str | None = dumps(loads(body), indent=2)
The body of the response, if available.

#### message instance-attribute

message: str = message

Description of the unexpected behavior.

#### body instance-attribute

body: str | None = dumps(loads(body), indent=2)

The body of the response, if available.

