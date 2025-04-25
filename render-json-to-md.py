import json
import os

input_folder = "./articles"
output_folder = "./rendered_markdown"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".json"):
        with open(os.path.join(input_folder, filename), "r") as f:
            data = json.load(f)
        
        output_md = f"# {data['requirement']}\n"
        
        for section in data.get("sections", []):
            output_md += f"## {section['title']}\n\n"
            if isinstance(section.get("content"), dict):
                for sub_title, sub_content in section["content"].items():
                    output_md += f"**{sub_title}**\n\n{sub_content}\n\n"
            elif isinstance(section.get("content"), list):
                for item in section["content"]:
                    output_md += f"- {item}\n"
                output_md += "\n"
            elif section.get("table"):
                output_md += "| Sub-Requirement | Responsible | Accountable | Consulted | Informed |\n"
                output_md += "|:----------------|:------------|:-----------|:----------|:--------|\n"
                for row in section["table"]:
                    output_md += f"| {row['Sub-Requirement']} | {row['Responsible']} | {row['Accountable']} | {row['Consulted']} | {row['Informed']} |\n"
                output_md += "\n"
            else:
                output_md += f"{section.get('content', '')}\n\n"
        
        output_file = os.path.join(output_folder, filename.replace(".json", ".md"))
        with open(output_file, "w") as f:
            f.write(output_md)

print("✅ Articles rendered successfully into Markdown!")
