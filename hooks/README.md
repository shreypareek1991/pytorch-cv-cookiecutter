# CookieCutter Hooks

This directory contains pre and post-generation hooks for the cookiecutter template.

## Files

- `pre_gen_project.py` - Runs before project generation, displays welcome message and logo
- `post_gen_project.py` - Runs after project generation, handles setup tasks
- `logo.txt` - ASCII art logo displayed during template generation

## Customizing the Logo

To customize the company logo:

1. Edit `logo.txt` with your ASCII art logo
2. The logo will be automatically displayed when users run the template
3. You can use any ASCII art generator or create your own design
4. Recommended width: ~60 characters for best display

### ASCII Art Generators

- https://patorjk.com/software/taag/
- https://www.ascii-art-generator.org/
- https://asciiflow.com/

### Example Logo Format

```
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║              YOUR COMPANY NAME HERE                       ║
║              Your Tagline or Description                   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

## Customizing Messages

Edit the following functions in the hook files:

- `pre_gen_project.py` → `print_welcome()` - Welcome message
- `post_gen_project.py` → `print_success_message()` - Completion message

