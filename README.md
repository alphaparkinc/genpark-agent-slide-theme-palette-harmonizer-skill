# Slide Theme & Palette Harmonizer Skill for Autonomous Agents

[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-blue.svg)](https://modelcontextprotocol.io)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-zero-success.svg)](requirements.txt)

Generates accessible, harmonious presentation design themes. Calculates exact WCAG contrast ratios, typography pairings, surface tokens, and border accents.

## Features
- **WCAG Accessibility Compliance**: Accurately computes relative luminance contrast ratios for text vs background.
- **Harmonized Design Tokens**: Outputs complete token set (primary, background, surface, text, border).
- **Zero Third-Party Math Libraries**: Pure Python mathematical formulas.

## MCP Server Integration
```bash
python mcp_server.py
```

### Available MCP Tools
- `generate_theme_tokens`: Generate harmonized presentation theme from primary brand color.
