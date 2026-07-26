from pathlib import Path
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LocalNotes")

# File to store notes
NOTES_FILE = Path("notes.txt")


@mcp.tool()
def read_notes() -> str:
    """
    Read and return all notes from notes.txt.
    """
    if not NOTES_FILE.exists():
        return "No notes found."

    return NOTES_FILE.read_text(encoding="utf-8")


@mcp.tool()
def add_note(note: str) -> str:
    """
    Append the given content to a local notes.txt file.
    Args:
        content: The text content to append
    """
    with NOTES_FILE.open("a", encoding="utf-8") as f:
        f.write(note + "\n")

    return "Note added successfully."

mcp.run()