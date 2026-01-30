def format_greeting(name, style="friendly"):
    """Format a greeting message based on style."""
    styles = {
        "friendly": f"Hey {name}! Great to see you! 😊",
        "formal": f"Good day, {name}. Welcome.",
        "excited": f"OMG {name}!!! YOU'RE HERE!!! 🎉🎊",
        "robot": f"GREETINGS, {name.upper()}. I AM A ROBOT. BEEP BOOP. 🤖"
    }
    return styles.get(style, f"Hello {name}")

def calculate_sync_stats(files_added=0, files_modified=0, files_deleted=0):
    """Calculate statistics about a sync operation."""
    total_changes = files_added + files_modified + files_deleted
    return {
        "total_changes": total_changes,
        "added": files_added,
        "modified": files_modified,
        "deleted": files_deleted,
        "summary": f"Sync completed: +{files_added} ~{files_modified} -{files_deleted}"
    }

def validate_file_name(filename):
    """Check if a filename is valid for HF Spaces."""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    return not any(char in filename for char in invalid_chars)
