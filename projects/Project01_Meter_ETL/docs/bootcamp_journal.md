# Bootcamp Journal

---

# Day 1 - Project Setup & Logging

## Objectives

- Set up the Data Engineering Bootcamp repository.
- Configure the development environment on both office and personal laptops.
- Build the logging framework for `Project01_Meter_ETL`.

## Topics Learned

- Python virtual environments
- Logging module
- Logger hierarchy
- Logging levels
- Log handlers
- Project structure
- Git basics
- VS Code setup

## Practical Work

- Created `Project01_Meter_ETL`.
- Configured `.venv`.
- Built reusable `logging_config.py`.
- Created project-specific `logs` directory.
- Fixed logger configuration issues.
- Learned why `basicConfig()` only works once unless `force=True` is used.
- Understood why `__name__` becomes `__main__` when a file is executed directly.

## Challenges Solved

- Log file created in the wrong directory.
- `application.log` not recreated.
- PowerShell execution policy preventing virtual environment activation.
- Git identity configuration (`user.name` and `user.email`).

## Key Takeaways

- Configure logging only once.
- Keep logging centralized.
- Never hardcode machine-specific paths.

---

# Day 2 - Extraction Module

## Objectives

- Build the Extract stage of the ETL pipeline.

## Topics Learned

- Reading CSV files using pandas
- `Path` objects
- Type hints
- Exception handling
- Returning DataFrames

## Practical Work

- Implemented `extract_csv()`.
- Added logging to extraction.
- Successfully loaded sample meter data.

## Design Decisions

- Accept `Path` instead of raw strings.
- Raise exceptions to the caller instead of silently failing.

## Challenges Solved

- Handling missing files.
- Understanding `raise`.
- Understanding why `df` becomes undefined after an exception.

## Key Takeaways

- Functions should have one responsibility.
- Errors should propagate to the orchestration layer.

---

# Day 3 - Validation Model

## Objectives

- Design the validation result object.

## Topics Learned

- Classes
- Objects
- Constructors
- `@dataclass`
- Type hints
- Package structure
- `__init__.py`

## Practical Work

- Created `ValidationResult`.
- Refactored project structure.
- Moved models into a dedicated package.
- Learned package exports using `__init__.py`.

## Challenges Solved

- Import errors caused by incorrectly naming `__init__.py`.
- Understanding why packages expose classes through `__init__.py`.

## Key Takeaways

- Classes model concepts.
- Objects store independent state.
- Dataclasses eliminate repetitive boilerplate.

---

# Day 4 - OOP Foundations

## Objectives

- Understand how dataclasses work internally.

## Topics Learned

- `self`
- `__init__()`
- Constructor execution
- Attribute initialization
- Manual class implementation
- Instance attributes

## Practical Work

- Recreated a dataclass manually using `__init__()`.
- Compared manual classes with dataclasses.

## Key Takeaways

- `@dataclass` automatically generates constructors.
- `self.attribute = parameter` copies data into the object.
- Objects own their own state.

---

# Day 5 - Validator Design

## Objectives

- Design the validation framework.

## Topics Learned

- Validator architecture
- Separation of responsibilities
- Boolean masks in pandas
- Designing validation output
- Planning scalable validators

## Design Decisions

- Prefer vectorized DataFrame operations over row-by-row loops.
- Preserve the original DataFrame.
- Return both valid and invalid DataFrames.
- Report all validation errors instead of stopping at the first one.
- Keep business logic inside validators, not `main.py`.

## Planned Architecture

```text
Extract
    ↓
Validate
    ↓
Transform
    ↓
Load
```

### Future validator structure

```text
validators/
├── missing.py
├── datatype.py
├── duplicates.py
├── range_checks.py
├── timestamps.py
└── business_rules.py
```

## Current Project Status

```text
✔ Logging
✔ Extractor
✔ ValidationResult
✔ Project Structure
✔ Exception Handling
✔ OOP Basics
✔ Packages
✔ Type Hints
⬜ Validator Rules
⬜ Transformation
⬜ Database Loader
⬜ Configuration
⬜ Unit Tests
```