# 👻 CodeCasper

A smart code review assistant based on TBA Team Hermes' best practices and coding standards.

## 🎯 Overview

CodeCasper is an AI-powered tool that delivers consistent, high-quality code reviews. It analyzes code changes based on a defined ruleset and provides precise, constructive feedback in the style of TBA Team Hermes. The system continuously learns from each review, suggesting new rules and rule modifications to keep the ruleset current and effective.

## ✨ Key Features

- 🔍 Automated Code Reviews
- 📋 Standardized Best Practices
- 🛠️ Customizable Rule Base
- 🤝 AI Assistant Integration
- 📈 Continuous Code Quality Improvement
- 🎨 Style Enforcement
- 🧪 Testing Guidelines
- 🏗️ Architecture Patterns
- 🔒 Type Safety Focus
- 🧠 Self-Learning Capabilities
  - Identifies patterns for new rules
  - Suggests rule modifications
  - Detects outdated rules
  - Recognizes rule relationships

## 🚀 Getting Started

### AI Assistant Integration

1. **Create Custom GPT or Claude Project**
2. Insert instructions from `Code_Casper_Instructions.md` as base prompt
3. Add `Rules.json` as context/payload

### Running Code Reviews

1. Generate patch/diff of code changes:
2. Submit patch to AI assistant
3. Receive detailed feedback based on defined rules
4. Review suggested rule updates (if any)

## 🔄 Updating Rules

### Adding New Rules

1. Create rule in JSON format (manually or based on CodeCasper's suggestions)
2. Place in `rules/` directory
3. Regenerate Rules.json:

```bash
python concatenate_rules.py
```

### Modifying Existing Rules

1. Edit rule in `rules/` directory
2. Regenerate Rules.json
3. Commit changes

### AI-Driven Rule Evolution

CodeCasper continuously analyzes review patterns and can:
- Suggest new rules based on recurring patterns
- Recommend updates to existing rules
- Identify outdated or conflicting rules
- Detect implicit relationships between rules
- Propose rule priority adjustments

## 🏗️ Project Structure


```
codecasper/
├── rules/               # Individual rule definitions
│   ├── ARCH-*.json      # Architecture rules
│   ├── REACT-*.json     # React-specific rules
│   └── ...
├── Rules.json           # Generated comprehensive rule base
├── concatenate_rules.py # Script to merge rules
└── Code_Casper_Instructions.md
```

## 🎯 Rule Categories

- **ARCH**: Architecture & Component Organization
- **DEP**: Dependencies & Library Management
- **NEXT**: Next.js Framework Best Practices
- **REACT**: React Patterns & Best Practices
- **STYLE**: Styling & Naming Conventions
- **TS**: TypeScript Guidelines
- **TEST**: Testing & Debug Code Management

## 🤝 Contributing

Feel free to contribute by:
- Adding new rules
- Improving existing rules
- Suggesting new rule categories
- Reporting inconsistencies
- Sharing feedback on rule effectiveness
- Validating AI-suggested rule changes

## 📝 License

MIT License - feel free to use and adapt for your team's needs!