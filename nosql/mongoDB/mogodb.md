# MongoDB

Favours Consistency over availability.   
(ie it has a primary node ,if the primary node dies we could still read from the database but we cannot write until the issue is resolved).

### Features:

- No real schema is enforced on the data.
    (It does this by appending a unique ID to every blog of data that is added to the DB)
    - Although, you can insert a schema if you want to.

- Terminology
    - Databases
    - Collections
    - Documents

- Shell is a full JavaScript interpreter

- It alone can act as replcement for Hadoop
    - It has aggregation capabilities
    - It can exectue Map-reduce codes directly
    - And it has its own File system called GridFS

- But it still integrates with Hadoop, Spark and most languages.

