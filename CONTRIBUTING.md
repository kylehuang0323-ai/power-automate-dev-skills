# Contributing to Power Automate Dev Skills

Thank you for your interest in contributing! This project provides expert-level Power Automate development guidance as a reusable GitHub Copilot skill.

## How to contribute

### Reporting issues

- Open a [GitHub Issue](../../issues) for errors, outdated information, or missing topics
- Include the specific `docs/` file and section where the issue exists

### Adding or updating content

1. **Fork** the repository
2. **Create a branch** from `main` (e.g., `fix/expression-docs` or `feat/dataverse-patterns`)
3. **Make your changes** following the guidelines below
4. **Submit a Pull Request** with a clear description

### Content guidelines

- **Accuracy first** — all expressions, action names, and patterns must be verified against the current Power Automate platform
- **Practical examples** — include concrete code/expression examples, not just descriptions
- **DLP awareness** — note any DLP implications when introducing new connectors
- **Pure English** — all content should be in English for international accessibility
- **Consistent formatting** — follow the existing Markdown structure (tables, code blocks, headers)

### File structure

| Location | Purpose |
|----------|---------|
| `docs/*.md` | Detailed reference modules (one per topic) |
| `.github/copilot-instructions.md` | Core AI instructions (<4KB, high-priority rules only) |
| `.github/skills/power-automate/SKILL.md` | Skill metadata and index |
| `.github/prompts/*.prompt.md` | Task-specific prompt templates |
| `.github/instructions/*.instructions.md` | Path-specific AI instructions |
| `scripts/` | Internal tooling (not part of the skill content) |

### Style rules

- Use fenced code blocks with syntax hints for expressions
- Use tables for reference data (functions, limits, connector lists)
- Use `>` blockquotes for warnings (`⚠️`) and tips (`💡`)
- Keep each `docs/` file focused on a single topic
- Add cross-references to related docs when relevant

## Code of Conduct

Be respectful, constructive, and focused on improving the quality of Power Automate guidance for the community.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
