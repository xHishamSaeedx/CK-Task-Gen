# pydantic_ai.usage

Usage dataclass
LLM usage associated with a request or run.
Responsibility for calculating usage is on the model; PydanticAI simply sums the usage information across requests.
You'll need to look up the documentation of the model you're using to convert usage to monetary costs.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
requests class-attribute instance-attribute
requests: int = 0
Number of requests made to the LLM API.
request_tokens class-attribute instance-attribute
request_tokens: int | None = None
Tokens used in processing requests.
response_tokens class-attribute instance-attribute
response_tokens: int | None = None
Tokens used in generating responses.
total_tokens class-attribute instance-attribute
total_tokens: int | None = None
Total tokens used in the whole run, should generally be equal to request_tokens + response_tokens.
details class-attribute instance-attribute
details: dict[str, int] | None = None
Any extra details returned by the model.
incr
incr(incr_usage: Usage, *, requests: int = 0) -> None
Increment the usage in place.
Parameters:
Name Type Description Default
incr_usage Usage The usage to increment by. required
requests int The number of requests to increment by in addition to incr_usage.requests. 0
Source code in pydantic_ai_slim/pydantic_ai/usage.py
__add__
__add__(other: Usage) -> Usage
Add two Usages together.
This is provided so it's trivial to sum usage information from multiple requests and runs.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
UsageLimits dataclass
Limits on model usage.
The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model. Token counts are provided in responses from the model, and the token limits are checked after each response.
Each of the limits can be set to None to disable that limit.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
request_limit class-attribute instance-attribute
request_limit: int | None = 50
The maximum number of requests allowed to the model.
request_tokens_limit class-attribute instance-attribute
request_tokens_limit: int | None = None
The maximum number of tokens allowed in requests to the model.
response_tokens_limit class-attribute instance-attribute
response_tokens_limit: int | None = None
The maximum number of tokens allowed in responses from the model.
total_tokens_limit class-attribute instance-attribute
total_tokens_limit: int | None = None
The maximum number of tokens allowed in requests and responses combined.
has_token_limits
has_token_limits() -> bool
Returns True if this instance places any limits on token counts.
If this returns False, the check_tokens method will never raise an error.
This is useful because if we have token limits, we need to check them after receiving each streamed message. If there are no limits, we can skip that processing in the streaming response iterator.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
check_before_request
check_before_request(usage: Usage) -> None
Raises a UsageLimitExceeded exception if the next request would exceed the request_limit.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
check_tokens
check_tokens(usage: Usage) -> None
Raises a UsageLimitExceeded exception if the usage exceeds any of the token limits.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

### Usage dataclass

LLM usage associated with a request or run.
Responsibility for calculating usage is on the model; PydanticAI simply sums the usage information across requests.
You'll need to look up the documentation of the model you're using to convert usage to monetary costs.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
requests class-attribute instance-attribute
requests: int = 0
Number of requests made to the LLM API.
request_tokens class-attribute instance-attribute
request_tokens: int | None = None
Tokens used in processing requests.
response_tokens class-attribute instance-attribute
response_tokens: int | None = None
Tokens used in generating responses.
total_tokens class-attribute instance-attribute
total_tokens: int | None = None
Total tokens used in the whole run, should generally be equal to request_tokens + response_tokens.
details class-attribute instance-attribute
details: dict[str, int] | None = None
Any extra details returned by the model.
incr
incr(incr_usage: Usage, *, requests: int = 0) -> None
Increment the usage in place.
Parameters:
Name Type Description Default
incr_usage Usage The usage to increment by. required
requests int The number of requests to increment by in addition to incr_usage.requests. 0
Source code in pydantic_ai_slim/pydantic_ai/usage.py
__add__
__add__(other: Usage) -> Usage
Add two Usages together.
This is provided so it's trivial to sum usage information from multiple requests and runs.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

#### requests class-attribute instance-attribute

requests: int = 0

Number of requests made to the LLM API.

#### request_tokens class-attribute instance-attribute

request_tokens: int | None = None

Tokens used in processing requests.

#### response_tokens class-attribute instance-attribute

response_tokens: int | None = None

Tokens used in generating responses.

#### total_tokens class-attribute instance-attribute

total_tokens: int | None = None

Total tokens used in the whole run, should generally be equal to request_tokens + response_tokens.

#### details class-attribute instance-attribute

details: dict[str, int] | None = None

Any extra details returned by the model.

#### incr

incr(incr_usage: Usage, *, requests: int = 0) -> None

Increment the usage in place.
Parameters:
Name Type Description Default
incr_usage Usage The usage to increment by. required
requests int The number of requests to increment by in addition to incr_usage.requests. 0
Source code in pydantic_ai_slim/pydantic_ai/usage.py

#### __add__

__add__(other: Usage) -> Usage

Add two Usages together.
This is provided so it's trivial to sum usage information from multiple requests and runs.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

### UsageLimits dataclass

Limits on model usage.
The request count is tracked by pydantic_ai, and the request limit is checked before each request to the model. Token counts are provided in responses from the model, and the token limits are checked after each response.
Each of the limits can be set to None to disable that limit.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
request_limit class-attribute instance-attribute
request_limit: int | None = 50
The maximum number of requests allowed to the model.
request_tokens_limit class-attribute instance-attribute
request_tokens_limit: int | None = None
The maximum number of tokens allowed in requests to the model.
response_tokens_limit class-attribute instance-attribute
response_tokens_limit: int | None = None
The maximum number of tokens allowed in responses from the model.
total_tokens_limit class-attribute instance-attribute
total_tokens_limit: int | None = None
The maximum number of tokens allowed in requests and responses combined.
has_token_limits
has_token_limits() -> bool
Returns True if this instance places any limits on token counts.
If this returns False, the check_tokens method will never raise an error.
This is useful because if we have token limits, we need to check them after receiving each streamed message. If there are no limits, we can skip that processing in the streaming response iterator.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
check_before_request
check_before_request(usage: Usage) -> None
Raises a UsageLimitExceeded exception if the next request would exceed the request_limit.
Source code in pydantic_ai_slim/pydantic_ai/usage.py
check_tokens
check_tokens(usage: Usage) -> None
Raises a UsageLimitExceeded exception if the usage exceeds any of the token limits.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

#### request_limit class-attribute instance-attribute

request_limit: int | None = 50

The maximum number of requests allowed to the model.

#### request_tokens_limit class-attribute instance-attribute

request_tokens_limit: int | None = None

The maximum number of tokens allowed in requests to the model.

#### response_tokens_limit class-attribute instance-attribute

response_tokens_limit: int | None = None

The maximum number of tokens allowed in responses from the model.

#### total_tokens_limit class-attribute instance-attribute

total_tokens_limit: int | None = None

The maximum number of tokens allowed in requests and responses combined.

#### has_token_limits

has_token_limits() -> bool

Returns True if this instance places any limits on token counts.
If this returns False, the check_tokens method will never raise an error.
This is useful because if we have token limits, we need to check them after receiving each streamed message. If there are no limits, we can skip that processing in the streaming response iterator.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

#### check_before_request

check_before_request(usage: Usage) -> None

Raises a UsageLimitExceeded exception if the next request would exceed the request_limit.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

#### check_tokens

check_tokens(usage: Usage) -> None

Raises a UsageLimitExceeded exception if the usage exceeds any of the token limits.
Source code in pydantic_ai_slim/pydantic_ai/usage.py

