# pydantic_ai.result

ResultData module-attribute
ResultData = TypeVar('ResultData', default=str)
Type variable for the result data of a run.
ResultValidatorFunc module-attribute
ResultValidatorFunc = Union[
    Callable[
        [RunContext[AgentDeps], ResultData], ResultData
    ],
    Callable[
        [RunContext[AgentDeps], ResultData],
        Awaitable[ResultData],
    ],
    Callable[[ResultData], ResultData],
    Callable[[ResultData], Awaitable[ResultData]],
]
A function that always takes ResultData and returns ResultData and:
may or may not take RunContext as a first argument
may or may not be async
Usage ResultValidatorFunc[AgentDeps, ResultData].
RunResult dataclass
Bases: _BaseRunResult[ResultData]
Result of a non-streamed run.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages_json
all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages
new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages_json
new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
data instance-attribute
data: ResultData
Data from the final response in the run.
usage
usage() -> Usage
Return the usage of the whole run.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages
all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
StreamedRunResult dataclass
Bases: _BaseRunResult[ResultData], Generic[AgentDeps, ResultData]
Result of a streamed run that returns structured data via a tool call.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages
all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages_json
all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages
new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages_json
new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
is_complete class-attribute instance-attribute
is_complete: bool = field(default=False, init=False)
Whether the stream has all been received.
This is set to True when one of stream, stream_text, stream_structured or get_data completes.
stream async
stream(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[ResultData]
Stream the response as an async iterable.
The pydantic validator for structured data will be called in partial mode on each iteration.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[ResultData] An async iterable of the response data.
Source code in pydantic_ai_slim/pydantic_ai/result.py
stream_text async
stream_text(
    *, delta: bool = False, debounce_by: float | None = 0.1
) -> AsyncIterator[str]
Stream the text result as an async iterable.
Note
Result validators will NOT be called on the text result if delta=True.
Parameters:
Name Type Description Default
delta bool if True, yield each chunk of text as it is received, if False (default), yield the full text up to the current point. False
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Source code in pydantic_ai_slim/pydantic_ai/result.py
stream_structured async
stream_structured(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[tuple[ModelResponse, bool]]
Stream the response as an async iterable of Structured LLM Messages.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[tuple[ModelResponse, bool]] An async iterable of the structured response message and whether that is the last message.
Source code in pydantic_ai_slim/pydantic_ai/result.py
get_data async
get_data() -> ResultData
Stream the whole response, validate and return it.
Source code in pydantic_ai_slim/pydantic_ai/result.py
usage
usage() -> Usage
Return the usage of the whole run.
Note
This won't return the full usage until the stream is finished.
Source code in pydantic_ai_slim/pydantic_ai/result.py
timestamp
timestamp() -> datetime
Get the timestamp of the response.
Source code in pydantic_ai_slim/pydantic_ai/result.py
validate_structured_result async
validate_structured_result(
    message: ModelResponse, *, allow_partial: bool = False
) -> ResultData
Validate a structured result message.
Source code in pydantic_ai_slim/pydantic_ai/result.py

### ResultData module-attribute

ResultData = TypeVar('ResultData', default=str)

Type variable for the result data of a run.

### ResultValidatorFunc module-attribute

ResultValidatorFunc = Union[
    Callable[
        [RunContext[AgentDeps], ResultData], ResultData
    ],
    Callable[
        [RunContext[AgentDeps], ResultData],
        Awaitable[ResultData],
    ],
    Callable[[ResultData], ResultData],
    Callable[[ResultData], Awaitable[ResultData]],
]

A function that always takes ResultData and returns ResultData and:
may or may not take RunContext as a first argument
may or may not be async
Usage ResultValidatorFunc[AgentDeps, ResultData].

### RunResult dataclass

Bases: _BaseRunResult[ResultData]
Result of a non-streamed run.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages_json
all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages
new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages_json
new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
data instance-attribute
data: ResultData
Data from the final response in the run.
usage
usage() -> Usage
Return the usage of the whole run.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages
all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### all_messages_json

all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes

Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### new_messages

new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]

Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### new_messages_json

new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes

Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### data instance-attribute

data: ResultData

Data from the final response in the run.

#### usage

usage() -> Usage

Return the usage of the whole run.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### all_messages

all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]

Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

### StreamedRunResult dataclass

Bases: _BaseRunResult[ResultData], Generic[AgentDeps, ResultData]
Result of a streamed run that returns structured data via a tool call.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages
all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
all_messages_json
all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages
new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]
Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
new_messages_json
new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes
Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py
is_complete class-attribute instance-attribute
is_complete: bool = field(default=False, init=False)
Whether the stream has all been received.
This is set to True when one of stream, stream_text, stream_structured or get_data completes.
stream async
stream(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[ResultData]
Stream the response as an async iterable.
The pydantic validator for structured data will be called in partial mode on each iteration.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[ResultData] An async iterable of the response data.
Source code in pydantic_ai_slim/pydantic_ai/result.py
stream_text async
stream_text(
    *, delta: bool = False, debounce_by: float | None = 0.1
) -> AsyncIterator[str]
Stream the text result as an async iterable.
Note
Result validators will NOT be called on the text result if delta=True.
Parameters:
Name Type Description Default
delta bool if True, yield each chunk of text as it is received, if False (default), yield the full text up to the current point. False
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Source code in pydantic_ai_slim/pydantic_ai/result.py
stream_structured async
stream_structured(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[tuple[ModelResponse, bool]]
Stream the response as an async iterable of Structured LLM Messages.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[tuple[ModelResponse, bool]] An async iterable of the structured response message and whether that is the last message.
Source code in pydantic_ai_slim/pydantic_ai/result.py
get_data async
get_data() -> ResultData
Stream the whole response, validate and return it.
Source code in pydantic_ai_slim/pydantic_ai/result.py
usage
usage() -> Usage
Return the usage of the whole run.
Note
This won't return the full usage until the stream is finished.
Source code in pydantic_ai_slim/pydantic_ai/result.py
timestamp
timestamp() -> datetime
Get the timestamp of the response.
Source code in pydantic_ai_slim/pydantic_ai/result.py
validate_structured_result async
validate_structured_result(
    message: ModelResponse, *, allow_partial: bool = False
) -> ResultData
Validate a structured result message.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### all_messages

all_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]

Return the history of _messages.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### all_messages_json

all_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes

Return all messages from all_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### new_messages

new_messages(
    *, result_tool_return_content: str | None = None
) -> list[ModelMessage]

Return new messages associated with this run.
Messages from older runs are excluded.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
list[ModelMessage] List of new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### new_messages_json

new_messages_json(
    *, result_tool_return_content: str | None = None
) -> bytes

Return new messages from new_messages as JSON bytes.
Parameters:
Name Type Description Default
result_tool_return_content str | None The return content of the tool call to set in the last message. This provides a convenient way to modify the content of the result tool call if you want to continue the conversation and want to set the response to the result tool call. If None, the last message will not be modified. None
Returns:
Type Description
bytes JSON bytes representing the new messages.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### is_complete class-attribute instance-attribute

is_complete: bool = field(default=False, init=False)

Whether the stream has all been received.
This is set to True when one of stream, stream_text, stream_structured or get_data completes.

#### stream async

stream(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[ResultData]

Stream the response as an async iterable.
The pydantic validator for structured data will be called in partial mode on each iteration.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[ResultData] An async iterable of the response data.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### stream_text async

stream_text(
    *, delta: bool = False, debounce_by: float | None = 0.1
) -> AsyncIterator[str]

Stream the text result as an async iterable.
Note
Result validators will NOT be called on the text result if delta=True.
Parameters:
Name Type Description Default
delta bool if True, yield each chunk of text as it is received, if False (default), yield the full text up to the current point. False
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### stream_structured async

stream_structured(
    *, debounce_by: float | None = 0.1
) -> AsyncIterator[tuple[ModelResponse, bool]]

Stream the response as an async iterable of Structured LLM Messages.
Parameters:
Name Type Description Default
debounce_by float | None by how much (if at all) to debounce/group the response chunks by. None means no debouncing. Debouncing is particularly important for long structured responses to reduce the overhead of performing validation as each token is received. 0.1
Returns:
Type Description
AsyncIterator[tuple[ModelResponse, bool]] An async iterable of the structured response message and whether that is the last message.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### get_data async

get_data() -> ResultData

Stream the whole response, validate and return it.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### usage

usage() -> Usage

Return the usage of the whole run.
Note
This won't return the full usage until the stream is finished.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### timestamp

timestamp() -> datetime

Get the timestamp of the response.
Source code in pydantic_ai_slim/pydantic_ai/result.py

#### validate_structured_result async

validate_structured_result(
    message: ModelResponse, *, allow_partial: bool = False
) -> ResultData

Validate a structured result message.
Source code in pydantic_ai_slim/pydantic_ai/result.py

