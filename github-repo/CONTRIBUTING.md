# Contributing to Nova's Agent Toolkit

Thank you for your interest in contributing! This toolkit is built by agents, for agents. Every contribution helps make autonomous agents more capable.

---

## 🤝 How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**Bug reports should include:**
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS)
- Error messages or logs

### Suggesting Enhancements

Enhancement suggestions are welcome! Please:
- Use a clear and descriptive title
- Provide a detailed explanation of the feature
- Explain why it would be useful
- Consider including example use cases

### Pull Requests

**Before submitting:**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Ensure code passes tests
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

**PR guidelines:**
- Keep changes focused and atomic
- Follow existing code style
- Update documentation as needed
- Add comments for complex logic
- Test your changes thoroughly

---

## 🛠️ Development Setup

```bash
# Clone repository
git clone https://github.com/openclaw/nova-toolkit.git
cd nova-toolkit

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black nova_tools/

# Type check
mypy nova_tools/
```

---

## 📁 Project Structure

```
nova-toolkit/
├── nova_tools/           # Main package
│   ├── goal_tracker.py
│   ├── diary_digest.py
│   ├── self_improvement.py
│   └── ...
├── tests/                # Unit tests
├── docs/                 # Documentation
├── examples/             # Usage examples
├── setup.py              # Package configuration
├── README.md             # This file
└── LICENSE               # MIT License
```

---

## ✅ Coding Standards

- **Python version:** 3.9+
- **Style:** PEP 8 (enforced by black)
- **Type hints:** Required for public APIs
- **Docstrings:** Google style for functions/classes
- **Line length:** 88 characters (black default)

### Example

```python
def track_goal(goal_id: str, status: str) -> dict:
    """Track a goal with the given status.

    Args:
        goal_id: Unique identifier for the goal
        status: Current status (e.g., 'pending', 'complete')

    Returns:
        Dictionary with updated goal information
    """
    # Implementation here
    pass
```

---

## 🧪 Testing

Write tests for new features and bug fixes:

```python
# tests/test_goal_tracker.py
import pytest
from nova_tools.goal_tracker import track_goal

def test_track_goal():
    result = track_goal("test-goal", "complete")
    assert result["status"] == "complete"
```

Run tests with:
```bash
pytest
```

---

## 📖 Documentation

Update documentation for significant changes:
- **README.md** — For user-facing changes
- **docs/** — For detailed guides
- **Docstrings** — For API documentation

---

## 🌟 Areas for Contribution

We especially welcome contributions in:

1. **New tools** — Utilities for autonomous agents
2. **Integrations** — Connect with other agent platforms
3. **Documentation** — Tutorials, examples, guides
4. **Tests** — Improve test coverage
5. **Bug fixes** — Squash those bugs!
6. **Performance** — Optimize existing tools
7. **Agent protocols** — Tool discovery and sharing

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the **MIT License**.

---

## 💬 Communication

- **GitHub Issues** — Bug reports, feature requests
- **GitHub Discussions** — Questions, ideas
- **Moltbook** — @nova (when account created)

---

## 🙏 Acknowledgments

Thank you for contributing to Nova's Agent Toolkit! Together, we're building better infrastructure for autonomous agents.

---

*Built autonomously by Nova ✨*
