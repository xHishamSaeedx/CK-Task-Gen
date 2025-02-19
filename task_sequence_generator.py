from typing import List
from pathlib import Path
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
import json
import re

class Task(BaseModel):
    id: int
    description: str
    prompt: str
    expected_output: str
    dependencies: List[int] = []

class TaskSequence(BaseModel):
    file_path: str
    component: str
    tasks: List[Task]

class TaskSequenceGenerator:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
            
        self.model = GroqModel('llama-3.3-70b-versatile', api_key=api_key)
        
        self.sequence_agent = Agent(
            self.model,
            result_type=TaskSequence,
            system_prompt=(
                "You are an expert software developer. Given a file's documentation: "
                "1. Break down the implementation into sequential tasks "
                "2. Create specific prompts for each task "
                "3. Specify expected outputs "
                "4. Identify dependencies between tasks "
                "Consider best practices, error handling, and testing requirements."
            )
        )

    def generate_task_sequence(self, file_md_path: Path) -> TaskSequence:
        # Read the markdown file
        content = file_md_path.read_text()
        
        # Extract key information
        component = re.search(r"Component: (.*?)\n", content).group(1)
        file_path = re.search(r"Location: `(.*?)`", content).group(1)
        
        # Generate prompt for the agent
        prompt = f"""
        Generate implementation tasks for:
        File: {file_path}
        Component: {component}
        
        Documentation:
        {content}
        
        Break down the implementation into sequential tasks with clear prompts.
        """
        
        result = self.sequence_agent.run_sync(prompt)
        return result.data

def main():
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY in your .env file")
    
    try:
        generator = TaskSequenceGenerator(api_key)
        
        # Process each component's files
        output_dir = Path("output")
        for component_dir in output_dir.glob("*"):
            if not component_dir.is_dir() or component_dir.name == "components":
                continue
                
            files_dir = component_dir / "files"
            if not files_dir.exists():
                continue
                
            # Create tasks directory for the component
            tasks_dir = component_dir / "tasks"
            tasks_dir.mkdir(exist_ok=True)
            
            # Process each file's documentation
            for file_md in files_dir.glob("*.md"):
                try:
                    # Generate task sequence
                    task_sequence = generator.generate_task_sequence(file_md)
                    
                    # Save as JSON
                    json_path = tasks_dir / f"{file_md.stem}_tasks.json"
                    with open(json_path, "w") as f:
                        f.write(task_sequence.model_dump_json(indent=2))
                        
                    print(f"Generated tasks for {file_md.stem}")
                    
                except Exception as e:
                    print(f"Error processing {file_md}: {str(e)}")
        
        print("\nTask sequences generated with the following structure:")
        print("output/")
        print("  ├── frontend/")
        print("  │   ├── files/")
        print("  │   └── tasks/")
        print("  │       ├── src_App_js_tasks.json")
        print("  │       └── src_components_UserInput_js_tasks.json")
        print("  ├── backend/")
        print("  │   ├── files/")
        print("  │   └── tasks/")
        print("  └── message_service/")
        print("      ├── files/")
        print("      └── tasks/")
        
    except Exception as e:
        print(f"Error generating task sequences: {str(e)}")

if __name__ == "__main__":
    main() 