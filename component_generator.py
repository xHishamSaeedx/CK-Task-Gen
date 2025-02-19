from typing import List, Tuple
from pathlib import Path
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
import json

class FileStructure(BaseModel):
    path: str
    description: str
    key_files: List[Tuple[int, str]]
    dependencies: List[str]
    setup_instructions: str

class ComponentDocGenerator:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
            
        self.model = GroqModel('llama-3.3-70b-versatile', api_key=api_key)
        
        self.doc_agent = Agent(
            self.model,
            result_type=FileStructure,
            system_prompt="""
            You are an expert software architect. Given a component specification from a system architecture:
            1. Design a clear file/folder structure for the component
            2. Identify key files needed for implementation and their sequence order
            3. List external dependencies and requirements
            4. Provide setup instructions
            
            For key files:
            - Assign sequence numbers (starting from 1) to indicate implementation order
            - Lower numbers should be implemented first
            - Consider dependencies between files
            
            Consider:
            - Best practices for the given technology stack
            - Clear separation of concerns
            - Maintainability and scalability
            - Testing and deployment requirements
            """
        )

    def generate_component_docs(self, component_data: dict) -> str:
        # Generate the file structure specification
        prompt = f"""
        Generate a file structure for a {component_data['type']} component with these details:
        Name: {component_data['name']}
        Description: {component_data['description']}
        Technologies: {', '.join(component_data['libraries'])}
        Inputs: {', '.join(component_data['inputs'])}
        Outputs: {', '.join(component_data['outputs'])}
        Additional Info: {component_data['additional_info']}
        """
        
        result = self.doc_agent.run_sync(prompt)
        structure = result.data
        
        # Generate markdown documentation
        md_content = [
            f"# {component_data['name']} Component",
            "\n## Overview",
            component_data['description'],
            "\n## File Structure",
            f"Root directory: `{structure.path}`",
            "\n### Key Files",
            "Implementation sequence:",
        ]
        
        # Sort key files by sequence number and format output
        for seq_num, file in sorted(structure.key_files):
            md_content.append(f"{seq_num}. {file}")
            
        md_content.extend([
            "\n## Dependencies",
            *[f"- {dep}" for dep in structure.dependencies],
            "\n## Setup Instructions",
            structure.setup_instructions
        ])
        
        return "\n".join(md_content)

def main():
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY in your .env file")
    
    try:
        # Load the architecture specification
        with open("output/architecture.json", "r") as f:
            arch_spec = json.load(f)
        
        generator = ComponentDocGenerator(api_key)
        
        # Create components directory if it doesn't exist
        output_dir = Path("output/components")
        output_dir.mkdir(exist_ok=True, parents=True)
        
        # Generate documentation for each component
        for component in arch_spec["components"]:
            md_content = generator.generate_component_docs(component)
            
            # Save to file
            component_file = output_dir / f"{component['name'].lower().replace(' ', '_')}.md"
            with open(component_file, "w") as f:
                f.write(md_content)
                
        print(f"Component documentation generated in {output_dir} directory")
        
    except Exception as e:
        print(f"Error generating component documentation: {str(e)}")

if __name__ == "__main__":
    main() 