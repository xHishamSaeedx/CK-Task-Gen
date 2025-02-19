# pydantic_ai.tools

AgentDeps module-attribute
AgentDeps = TypeVar('AgentDeps', default=None)
Type variable for agent dependencies.
RunContext dataclass
Bases: Generic[AgentDeps]
Information about the current call.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
deps instance-attribute
deps: AgentDeps
Dependencies for the agent.
model instance-attribute
model: Model
The model used in this run.
usage instance-attribute
usage: Usage
LLM usage associated with the run.
prompt instance-attribute
prompt: str
The original user prompt passed to the run.
messages class-attribute instance-attribute
messages: list[ModelMessage] = field(default_factory=list)
Messages exchanged in the conversation so far.
tool_name class-attribute instance-attribute
tool_name: str | None = None
Name of the tool being called.
retry class-attribute instance-attribute
retry: int = 0
Number of retries so far.
run_step class-attribute instance-attribute
run_step: int = 0
The current step in the run.
ToolParams module-attribute
ToolParams = ParamSpec('ToolParams', default=...)
Retrieval function param spec.
SystemPromptFunc module-attribute
SystemPromptFunc = Union[
    Callable[[RunContext[AgentDeps]], str],
    Callable[[RunContext[AgentDeps]], Awaitable[str]],
    Callable[[], str],
    Callable[[], Awaitable[str]],
]
A function that may or maybe not take RunContext as an argument, and may or may not be async.
Usage SystemPromptFunc[AgentDeps].
ToolFuncContext module-attribute
ToolFuncContext = Callable[
    Concatenate[RunContext[AgentDeps], ToolParams], Any
]
A tool function that takes RunContext as the first argument.
Usage ToolContextFunc[AgentDeps, ToolParams].
ToolFuncPlain module-attribute
ToolFuncPlain = Callable[ToolParams, Any]
A tool function that does not take RunContext as the first argument.
Usage ToolPlainFunc[ToolParams].
ToolFuncEither module-attribute
ToolFuncEither = Union[
    ToolFuncContext[AgentDeps, ToolParams],
    ToolFuncPlain[ToolParams],
]
Either kind of tool function.
This is just a union of ToolFuncContext and ToolFuncPlain.
Usage ToolFuncEither[AgentDeps, ToolParams].
ToolPrepareFunc module-attribute
ToolPrepareFunc: TypeAlias = (
    "Callable[[RunContext[AgentDeps], ToolDefinition], Awaitable[ToolDefinition | None]]"
)
Definition of a function that can prepare a tool definition at call time.
See tool docs for more information.
Example — here only_if_42 is valid as a ToolPrepareFunc:
from typing import Union

from pydantic_ai import RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def only_if_42(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    if ctx.deps == 42:
        return tool_def

def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f'{ctx.deps} {answer}'

hitchhiker = Tool(hitchhiker, prepare=only_if_42)
Usage ToolPrepareFunc[AgentDeps].
DocstringFormat module-attribute
DocstringFormat = Literal[
    "google", "numpy", "sphinx", "auto"
]
Supported docstring formats.
'google' — Google-style docstrings.
'numpy' — Numpy-style docstrings.
'sphinx' — Sphinx-style docstrings.
'auto' — Automatically infer the format based on the structure of the docstring.
Tool dataclass
Bases: Generic[AgentDeps]
A tool function for an agent.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
__init__
__init__(
    function: ToolFuncEither[AgentDeps],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[AgentDeps] | None = None,
    docstring_format: DocstringFormat = "auto",
    require_parameter_descriptions: bool = False
)
Create a new tool instance.
Example usage:
from pydantic_ai import Agent, RunContext, Tool

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

agent = Agent('test', tools=[Tool(my_tool)])
or with a custom prepare method:
from typing import Union

from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
        return tool_def

agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
Parameters:
Name Type Description Default
function ToolFuncEither[AgentDeps] The Python function to call as the tool. required
takes_ctx bool | None Whether the function takes a RunContext first argument, this is inferred if unset. None
max_retries int | None Maximum number of retries allowed for this tool, set to the agent default if None. None
name str | None Name of the tool, inferred from the function if None. None
description str | None Description of the tool, inferred from the function if None. None
prepare ToolPrepareFunc[AgentDeps] | None custom method to prepare the tool definition for each step, return None to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See ToolPrepareFunc. None
docstring_format DocstringFormat The format of the docstring, see DocstringFormat. Defaults to 'auto', such that the format is inferred from the structure of the docstring. 'auto'
require_parameter_descriptions bool If True, raise an error if a parameter description is missing. Defaults to False. False
Source code in pydantic_ai_slim/pydantic_ai/tools.py
prepare_tool_def async
prepare_tool_def(
    ctx: RunContext[AgentDeps],
) -> ToolDefinition | None
Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls self.prepare if it's set.
Returns:
Type Description
ToolDefinition | None return a ToolDefinition or None if the tools should not be registered for this run.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
run async
run(
    message: ToolCallPart,
    run_context: RunContext[AgentDeps],
) -> ModelRequestPart
Run the tool function asynchronously.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
ObjectJsonSchema module-attribute
ObjectJsonSchema: TypeAlias = dict[str, Any]
Type representing JSON schema of an object, e.g. where "type": "object".
This type is used to define tools parameters (aka arguments) in ToolDefinition.
With PEP-728 this should be a TypedDict with type: Literal['object'], and extra_parts=Any
ToolDefinition dataclass
Definition of a tool passed to a model.
This is used for both function tools result tools.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
name instance-attribute
name: str
The name of the tool.
description instance-attribute
description: str
The description of the tool.
parameters_json_schema instance-attribute
parameters_json_schema: ObjectJsonSchema
The JSON schema for the tool's parameters.
outer_typed_dict_key class-attribute instance-attribute
outer_typed_dict_key: str | None = None
The key in the outer [TypedDict] that wraps a result tool.
This will only be set for result tools which don't have an object JSON schema.

### AgentDeps module-attribute

AgentDeps = TypeVar('AgentDeps', default=None)

Type variable for agent dependencies.

### RunContext dataclass

Bases: Generic[AgentDeps]
Information about the current call.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
deps instance-attribute
deps: AgentDeps
Dependencies for the agent.
model instance-attribute
model: Model
The model used in this run.
usage instance-attribute
usage: Usage
LLM usage associated with the run.
prompt instance-attribute
prompt: str
The original user prompt passed to the run.
messages class-attribute instance-attribute
messages: list[ModelMessage] = field(default_factory=list)
Messages exchanged in the conversation so far.
tool_name class-attribute instance-attribute
tool_name: str | None = None
Name of the tool being called.
retry class-attribute instance-attribute
retry: int = 0
Number of retries so far.
run_step class-attribute instance-attribute
run_step: int = 0
The current step in the run.

#### deps instance-attribute

deps: AgentDeps

Dependencies for the agent.

#### model instance-attribute

model: Model

The model used in this run.

#### usage instance-attribute

usage: Usage

LLM usage associated with the run.

#### prompt instance-attribute

prompt: str

The original user prompt passed to the run.

#### messages class-attribute instance-attribute

messages: list[ModelMessage] = field(default_factory=list)

Messages exchanged in the conversation so far.

#### tool_name class-attribute instance-attribute

tool_name: str | None = None

Name of the tool being called.

#### retry class-attribute instance-attribute

retry: int = 0

Number of retries so far.

#### run_step class-attribute instance-attribute

run_step: int = 0

The current step in the run.

### ToolParams module-attribute

ToolParams = ParamSpec('ToolParams', default=...)

Retrieval function param spec.

### SystemPromptFunc module-attribute

SystemPromptFunc = Union[
    Callable[[RunContext[AgentDeps]], str],
    Callable[[RunContext[AgentDeps]], Awaitable[str]],
    Callable[[], str],
    Callable[[], Awaitable[str]],
]

A function that may or maybe not take RunContext as an argument, and may or may not be async.
Usage SystemPromptFunc[AgentDeps].

### ToolFuncContext module-attribute

ToolFuncContext = Callable[
    Concatenate[RunContext[AgentDeps], ToolParams], Any
]

A tool function that takes RunContext as the first argument.
Usage ToolContextFunc[AgentDeps, ToolParams].

### ToolFuncPlain module-attribute

ToolFuncPlain = Callable[ToolParams, Any]

A tool function that does not take RunContext as the first argument.
Usage ToolPlainFunc[ToolParams].

### ToolFuncEither module-attribute

ToolFuncEither = Union[
    ToolFuncContext[AgentDeps, ToolParams],
    ToolFuncPlain[ToolParams],
]

Either kind of tool function.
This is just a union of ToolFuncContext and ToolFuncPlain.
Usage ToolFuncEither[AgentDeps, ToolParams].

### ToolPrepareFunc module-attribute

ToolPrepareFunc: TypeAlias = (
    "Callable[[RunContext[AgentDeps], ToolDefinition], Awaitable[ToolDefinition | None]]"
)

Definition of a function that can prepare a tool definition at call time.
See tool docs for more information.
Example — here only_if_42 is valid as a ToolPrepareFunc:
from typing import Union

from pydantic_ai import RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def only_if_42(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    if ctx.deps == 42:
        return tool_def

def hitchhiker(ctx: RunContext[int], answer: str) -> str:
    return f'{ctx.deps} {answer}'

hitchhiker = Tool(hitchhiker, prepare=only_if_42)
Usage ToolPrepareFunc[AgentDeps].

### DocstringFormat module-attribute

DocstringFormat = Literal[
    "google", "numpy", "sphinx", "auto"
]

Supported docstring formats.
'google' — Google-style docstrings.
'numpy' — Numpy-style docstrings.
'sphinx' — Sphinx-style docstrings.
'auto' — Automatically infer the format based on the structure of the docstring.

### Tool dataclass

Bases: Generic[AgentDeps]
A tool function for an agent.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
__init__
__init__(
    function: ToolFuncEither[AgentDeps],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[AgentDeps] | None = None,
    docstring_format: DocstringFormat = "auto",
    require_parameter_descriptions: bool = False
)
Create a new tool instance.
Example usage:
from pydantic_ai import Agent, RunContext, Tool

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

agent = Agent('test', tools=[Tool(my_tool)])
or with a custom prepare method:
from typing import Union

from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
        return tool_def

agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
Parameters:
Name Type Description Default
function ToolFuncEither[AgentDeps] The Python function to call as the tool. required
takes_ctx bool | None Whether the function takes a RunContext first argument, this is inferred if unset. None
max_retries int | None Maximum number of retries allowed for this tool, set to the agent default if None. None
name str | None Name of the tool, inferred from the function if None. None
description str | None Description of the tool, inferred from the function if None. None
prepare ToolPrepareFunc[AgentDeps] | None custom method to prepare the tool definition for each step, return None to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See ToolPrepareFunc. None
docstring_format DocstringFormat The format of the docstring, see DocstringFormat. Defaults to 'auto', such that the format is inferred from the structure of the docstring. 'auto'
require_parameter_descriptions bool If True, raise an error if a parameter description is missing. Defaults to False. False
Source code in pydantic_ai_slim/pydantic_ai/tools.py
prepare_tool_def async
prepare_tool_def(
    ctx: RunContext[AgentDeps],
) -> ToolDefinition | None
Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls self.prepare if it's set.
Returns:
Type Description
ToolDefinition | None return a ToolDefinition or None if the tools should not be registered for this run.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
run async
run(
    message: ToolCallPart,
    run_context: RunContext[AgentDeps],
) -> ModelRequestPart
Run the tool function asynchronously.
Source code in pydantic_ai_slim/pydantic_ai/tools.py

#### __init__

__init__(
    function: ToolFuncEither[AgentDeps],
    *,
    takes_ctx: bool | None = None,
    max_retries: int | None = None,
    name: str | None = None,
    description: str | None = None,
    prepare: ToolPrepareFunc[AgentDeps] | None = None,
    docstring_format: DocstringFormat = "auto",
    require_parameter_descriptions: bool = False
)

Create a new tool instance.
Example usage:
from pydantic_ai import Agent, RunContext, Tool

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

agent = Agent('test', tools=[Tool(my_tool)])
or with a custom prepare method:
from typing import Union

from pydantic_ai import Agent, RunContext, Tool
from pydantic_ai.tools import ToolDefinition

async def my_tool(ctx: RunContext[int], x: int, y: int) -> str:
    return f'{ctx.deps} {x} {y}'

async def prep_my_tool(
    ctx: RunContext[int], tool_def: ToolDefinition
) -> Union[ToolDefinition, None]:
    # only register the tool if `deps == 42`
    if ctx.deps == 42:
        return tool_def

agent = Agent('test', tools=[Tool(my_tool, prepare=prep_my_tool)])
Parameters:
Name Type Description Default
function ToolFuncEither[AgentDeps] The Python function to call as the tool. required
takes_ctx bool | None Whether the function takes a RunContext first argument, this is inferred if unset. None
max_retries int | None Maximum number of retries allowed for this tool, set to the agent default if None. None
name str | None Name of the tool, inferred from the function if None. None
description str | None Description of the tool, inferred from the function if None. None
prepare ToolPrepareFunc[AgentDeps] | None custom method to prepare the tool definition for each step, return None to omit this tool from a given step. This is useful if you want to customise a tool at call time, or omit it completely from a step. See ToolPrepareFunc. None
docstring_format DocstringFormat The format of the docstring, see DocstringFormat. Defaults to 'auto', such that the format is inferred from the structure of the docstring. 'auto'
require_parameter_descriptions bool If True, raise an error if a parameter description is missing. Defaults to False. False
Source code in pydantic_ai_slim/pydantic_ai/tools.py

#### prepare_tool_def async

prepare_tool_def(
    ctx: RunContext[AgentDeps],
) -> ToolDefinition | None

Get the tool definition.
By default, this method creates a tool definition, then either returns it, or calls self.prepare if it's set.
Returns:
Type Description
ToolDefinition | None return a ToolDefinition or None if the tools should not be registered for this run.
Source code in pydantic_ai_slim/pydantic_ai/tools.py

#### run async

run(
    message: ToolCallPart,
    run_context: RunContext[AgentDeps],
) -> ModelRequestPart

Run the tool function asynchronously.
Source code in pydantic_ai_slim/pydantic_ai/tools.py

### ObjectJsonSchema module-attribute

ObjectJsonSchema: TypeAlias = dict[str, Any]

Type representing JSON schema of an object, e.g. where "type": "object".
This type is used to define tools parameters (aka arguments) in ToolDefinition.
With PEP-728 this should be a TypedDict with type: Literal['object'], and extra_parts=Any

### ToolDefinition dataclass

Definition of a tool passed to a model.
This is used for both function tools result tools.
Source code in pydantic_ai_slim/pydantic_ai/tools.py
name instance-attribute
name: str
The name of the tool.
description instance-attribute
description: str
The description of the tool.
parameters_json_schema instance-attribute
parameters_json_schema: ObjectJsonSchema
The JSON schema for the tool's parameters.
outer_typed_dict_key class-attribute instance-attribute
outer_typed_dict_key: str | None = None
The key in the outer [TypedDict] that wraps a result tool.
This will only be set for result tools which don't have an object JSON schema.

#### name instance-attribute

name: str

The name of the tool.

#### description instance-attribute

description: str

The description of the tool.

#### parameters_json_schema instance-attribute

parameters_json_schema: ObjectJsonSchema

The JSON schema for the tool's parameters.

#### outer_typed_dict_key class-attribute instance-attribute

outer_typed_dict_key: str | None = None

The key in the outer [TypedDict] that wraps a result tool.
This will only be set for result tools which don't have an object JSON schema.

