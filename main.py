import os

ENTRY = "I texted my boss 'I quit' but autocorrect changed it to 'I quilt' — now I'm teaching a sewing class on Friday."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
