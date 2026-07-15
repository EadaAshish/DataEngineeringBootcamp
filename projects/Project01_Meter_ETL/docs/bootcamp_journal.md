# Data Engineering Bootcamp Roadmap

## ✅ Phase 1: Python Foundations (Completed)

### Day 1
- Project setup
- Virtual environments
- Git & GitHub workflow
- Logging
- Reading CSV using Pandas

### Day 2
- Project structure
- Functions
- Modules
- Exception handling
- Type hints

### Day 3
- Dataclasses
- ValidationResult model
- OOP fundamentals
  - Class
  - Object
  - Attributes
  - Methods

### Day 4
- Separation of responsibilities
- Validators
- Boolean masks
- DataFrame filtering
- Performance considerations

### Day 5
- Validation framework design
- Creating valid and invalid DataFrames
- Preserving original DataFrame
- Error reporting strategy

### Day 6
- ValidationError dataclass
- Iterating DataFrames
- iterrows()
- loc[]
- Building error objects

### Day 7
- Individual validator implementation
- Returning list[ValidationError]
- Multiple errors per row
- Using sets
- Unique row extraction
- Validator architecture

### Day 8
- Validator orchestration
- Function references
- Storing functions in lists
- append() vs extend()
- Building ValidationResult
- DataFrame filtering using index.isin()
- Fail-fast vs recoverable errors
- ETL architecture discussions

---

# 🚧 Phase 2: Validation Framework (In Progress)

## Day 9
- Multiple validators
- Voltage validation
- Timestamp validation
- Warning framework
- Logging improvements

## Day 10
- Duplicate detection
- Business rule validation
- Validator registration improvements
- Unit testing validators

---

# ⏳ Phase 3: Transformation Layer

- Data cleaning
- Data normalization
- Datetime conversion
- Data enrichment
- Derived columns
- Pipeline chaining

---

# ⏳ Phase 4: Loading Layer

- Writing CSV
- Writing Excel
- PostgreSQL loading
- Batch inserts
- Transaction handling
- Upserts

---

# ⏳ Phase 5: Configuration & Utilities

- settings.py
- Environment variables
- Config files
- Constants
- Path management

---

# ⏳ Phase 6: Testing

- pytest
- Unit tests
- Mocking
- Test data
- Coverage

---

# ⏳ Phase 7: Production Engineering

- CLI arguments
- Scheduling
- Logging best practices
- Retry mechanisms
- Performance optimization
- Parallel processing

---

# ⏳ Phase 8: Docker & Deployment

- Docker
- Docker Compose
- Environment configuration
- Production deployment

---

# ⏳ Phase 9: Cloud & Data Engineering

- Object Storage
- Airflow
- Spark Basics
- Kafka Basics
- Data Warehousing
- ETL vs ELT
- Medallion Architecture

---

# Final Project

Build a production-style Meter ETL Pipeline featuring:

- Modular architecture
- Configurable validation framework
- Transformation layer
- PostgreSQL loading
- Comprehensive logging
- Unit tests
- Docker support
- Documentation
- GitHub CI-ready project