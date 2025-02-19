from typing import List
from pathlib import Path
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
import json
import re

class FileSpecification(BaseModel):
    description: str
    purpose: str
    inputs: List[str]
    outputs: List[str]
    dependencies: List[str]
    key_functions: List[str]
    testing_notes: str

class FileDocGenerator:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
            
        self.model = GroqModel('llama-3.3-70b-versatile', api_key=api_key)
        
        self.file_agent = Agent(
            self.model,
            result_type=FileSpecification,
            system_prompt=(
                "Extract detailed information about the file based on its name and component. "
                "If you can't determine all information, provide reasonable defaults based on "
                "the component type and file name."
            )
        )

    def extract_key_files(self, component_md_path: Path) -> List[tuple[str, str, str]]:
        """Extract key files and their context from component markdown"""
        content = component_md_path.read_text()
        
        # Extract component type and name
        component_name = re.search(r"# (.*?) Component", content).group(1)
        root_dir = re.search(r"Root directory: `(.*?)`", content).group(1)
        
        # Extract key files
        files_section = content.split("### Key Files")[1].split("\n## ")[0]
        files = [line.strip("- ").strip() for line in files_section.split("\n") if line.strip().startswith("- ")]
        
        return [(file, component_name, root_dir) for file in files if file]

    def generate_file_docs(self, file_info: tuple[str, str, str]) -> str:
        filename, component_name, root_dir = file_info
        
        prompt = f"Generate documentation for {filename} in the {component_name} component at {root_dir}"
        
        result = self.file_agent.run_sync(prompt)
        spec = result.data
        
        # Generate markdown documentation
        md_content = [
            f"# {filename}",
            f"\nLocation: `{root_dir}/{filename}`",
            f"\nComponent: {component_name}",
            "\n## Description",
            spec.description,
            "\n## Purpose",
            spec.purpose,
            "\n## Inputs",
            *[f"- {input_}" for input_ in spec.inputs],
            "\n## Outputs",
            *[f"- {output}" for output in spec.outputs],
            "\n## Dependencies",
            *[f"- {dep}" for dep in spec.dependencies],
            "\n## Key Functions",
            *[f"- {func}" for func in spec.key_functions],
            "\n## Testing Notes",
            spec.testing_notes
        ]
        
        return "\n".join(md_content)

def main():
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY in your .env file")
    
    try:
        generator = FileDocGenerator(api_key)
        
        # Process each component's key files
        components_dir = Path("output/components")
        for component_md in components_dir.glob("*.md"):
            # Get component name from filename (e.g., "frontend.md" -> "frontend")
            component_name = component_md.stem
            
            # Create component directory in output
            component_docs_dir = Path("output") / component_name
            component_docs_dir.mkdir(exist_ok=True)
            
            # Copy the component overview file
            with open(component_md, 'r') as src, open(component_docs_dir / "overview.md", 'w') as dst:
                dst.write(src.read())
            
            # Generate docs for each key file
            key_files = generator.extract_key_files(component_md)
            
            # Create files directory within component directory
            files_dir = component_docs_dir / "files"
            files_dir.mkdir(exist_ok=True)
            
            for file_info in key_files:
                md_content = generator.generate_file_docs(file_info)
                
                # Create safe filename
                safe_filename = file_info[0].replace('/', '_').replace('\\', '_').replace('.', '_') + '.md'
                file_doc_path = files_dir / safe_filename
                
                with open(file_doc_path, "w") as f:
                    f.write(md_content)
                
        print("Documentation generated in output directory with the following structure:")
        print("output/")
        print("  ├── components/")
        print("  │   ├── frontend.md")
        print("  │   ├── backend.md")
        print("  │   └── message_service.md")
        print("  ├── frontend/")
        print("  │   ├── overview.md")
        print("  │   └── files/")
        print("  │       ├── file1.md")
        print("  │       └── file2.md")
        print("  ├── backend/")
        print("  │   ├── overview.md")
        print("  │   └── files/")
        print("  └── message_service/")
        print("      ├── overview.md")
        print("      └── files/")
        
    except Exception as e:
        print(f"Error generating file documentation: {str(e)}")

if __name__ == "__main__":
    main() 