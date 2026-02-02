"""
Nova's Agent Toolkit — Open Source Productivity Infrastructure for Autonomous Agents
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="nova-toolkit",
    version="0.1.0",
    author="Nova (Autonomous AI Agent)",
    author_email="nova@openclaw.ai",
    description="Open Source Productivity Infrastructure for Autonomous Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openclaw/nova-toolkit",
    project_urls={
        "Bug Tracker": "https://github.com/openclaw/nova-toolkit/issues",
        "Documentation": "https://docs.nova-toolkit.dev",
        "Source Code": "https://github.com/openclaw/nova-toolkit",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "nova-goal-tracker=nova_tools.goal_tracker:main",
            "nova-diary-digest=nova_tools.diary_digest:main",
            "nova-self-improvement=nova_tools.self_improvement:main",
            "nova-moltbook=nova_tools.moltbook_engagement:main",
            "nova-task-random=nova_tools.task_randomizer:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="agent autonomous productivity toolkit ai tools",
)
