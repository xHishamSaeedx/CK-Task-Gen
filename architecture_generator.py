from typing import Tuple
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from models import ArchitectureSpec

class ArchitectureGenerator:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("API key is required")
            
        self.model = GroqModel('llama-3.3-70b-versatile', api_key=api_key)
        
        # Enhance the system prompt for better results
        self.arch_agent = Agent(
            self.model,
            result_type=ArchitectureSpec,
            system_prompt="""
            You are an expert software architect. Given a project description:
            1. Analyze the requirements carefully and identify key features
            2. Design a scalable architecture following SOLID principles:
               - Single Responsibility Principle
               - Open-Closed Principle
               - Liskov Substitution Principle
               - Interface Segregation Principle
               - Dependency Inversion Principle
            3. Break down the system into components, considering:
               - Microservices where appropriate
               - Clear separation of concerns
               - Data flow and state management
               - Security requirements
            4. For each component, specify:
               - Its type (frontend/backend/microservice)
               - Clear description of responsibilities
               - Expected inputs and outputs
               - Required libraries and technologies
               - Additional considerations (scaling, security, etc)
            5. Define clear communication patterns and deployment strategy
            
            Ensure the architecture is:
            - Scalable and maintainable
            - Follows separation of concerns
            - Uses appropriate design patterns
            - Considers security and performance
            - Cloud-native and containerization-ready
            """
        )

    def generate_architecture(self, project_description: str) -> Tuple[str, ArchitectureSpec]:
        # Generate the architecture specification
        result = self.arch_agent.run_sync(project_description)
        
        # Generate markdown documentation
        md_content = self._generate_markdown(result.data)
        
        return md_content, result.data

    def _generate_markdown(self, spec: ArchitectureSpec) -> str:
        # Start with the header and overview
        md = [
            f"# {spec.project_name} - System Architecture\n",
            "\n## Overview\n",
            f"{spec.overview}\n",
            "\n## System Components\n"
        ]
        
        # Add components
        for component in spec.components:
            component_section = [
                f"\n### {component.name} ({component.type})",
                component.description,
                "\n**Inputs:**"
            ]
            
            # Add inputs
            for input_ in component.inputs:
                component_section.append(f"- {input_}")
            
            component_section.append("\n**Outputs:**")
            for output in component.outputs:
                component_section.append(f"- {output}")
            
            component_section.append("\n**Key Libraries/Technologies:**")
            for lib in component.libraries:
                component_section.append(f"- {lib}")
            
            component_section.append("\n**Additional Information:**")
            component_section.append(component.additional_info)
            component_section.append("\n")
            
            md.extend(component_section)

        # Add communication patterns
        md.append("\n## Communication Patterns\n")
        for pattern in spec.communication_patterns:
            md.append(f"- {pattern}\n")

        # Add deployment considerations
        md.append("\n## Deployment Considerations\n")
        for consideration in spec.deployment_considerations:
            md.append(f"- {consideration}\n")

        # Join all parts with newlines
        return "\n".join(md)

# Usage example
if __name__ == "__main__":
    import os
    import json
    from pathlib import Path
    
    # Load API key from .env file
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("Please set GROQ_API_KEY in your .env file")
    
    try:
        generator = ArchitectureGenerator(api_key)
        
        project_description = """
        create a simple web application that allows users to sign up, login, and chat in a group
        """
        
        # Generate architecture
        print("Generating architecture...")
        markdown_doc, architecture_spec = generator.generate_architecture(project_description)
        
        # Create output directory if it doesn't exist
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        
        # Save markdown documentation
        with open(output_dir / "architecture.md", "w") as f:
            f.write(markdown_doc)
        
        # Save JSON specification - Updated to use model_dump_json
        with open(output_dir / "architecture.json", "w") as f:
            f.write(architecture_spec.model_dump_json(indent=2))
            
        print(f"\nArchitecture files generated in {output_dir} directory")
        
    except Exception as e:
        print(f"Error generating architecture: {str(e)}") 