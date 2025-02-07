# Streaming Project 101

## Scope

- [x]  Install requirements.txt when the image is built
- [ ]  Create a diagram with project main idea
- [ ]  Create an API REST for data delivery
- [ ]  Tools:
    - [ ]  Spark - Engine
    - [ ]  DuckDB - Alternative Engine
    - [ ]  Postgre - Application db
        - [ ]  Create a data factory function/application to populate the db
        - [ ]  Create a function/application to random delete/alter existing data
    - [ ]  Kafka - Integration with postgre for Data Change Capture - CDC
        - [ ]  Step 2: Use Airbyte to handle the CDC part
    - [ ]  MINio - Storage
    - [ ]  Can I make postgre interact with my storage like a lakehouse?

Notes

- Try to use Scala in a second phase of the project