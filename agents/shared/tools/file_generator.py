import os
from pathlib import Path


async def generate_files(files: dict[str, str], base_path: str = "/tmp/generated") -> list[str]:
    """Generate files at the specified paths with the given content.

    Args:
        files: Dictionary mapping relative file paths to their content.
        base_path: Base directory for generated files.

    Returns:
        List of absolute paths to the generated files.
    """
    generated: list[str] = []
    base = Path(base_path)

    for rel_path, content in files.items():
        abs_path = base / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)
        abs_path.write_text(content, encoding="utf-8")
        generated.append(str(abs_path))

    return generated
