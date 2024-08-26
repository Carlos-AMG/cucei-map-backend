In SQLAlchemy, you have several ways to perform queries using models, each suited to different scenarios. Here’s a comprehensive overview of the querying methods available:

### 1. **Using the ORM Query API**

This is the most common way to query models:

- **Basic Queries**
  ```python
  users = session.query(User).all()  # Retrieve all users
  ```

- **Filtering**
  ```python
  users_named_john = session.query(User).filter(User.name == 'John').all()
  ```

- **Combining Filters**
  ```python
  users_named_john_older_than_30 = session.query(User).filter(User.name == 'John').filter(User.age > 30).all()
  ```

- **Ordering**
  ```python
  sorted_users = session.query(User).order_by(User.age.desc()).all()
  ```

- **Limiting and Paging**
  ```python
  limited_users = session.query(User).limit(5).all()
  paged_users = session.query(User).offset(10).limit(5).all()
  ```

- **Distinct Results**
  ```python
  distinct_users = session.query(User.name).distinct().all()
  ```

### 2. **Using the New SQLAlchemy 2.0 Syntax**

With SQLAlchemy 2.0, you can perform queries directly on the model class if `query_property` is defined:

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    @query_property
    def query(cls):
        return session.query(cls)

# Usage
users = User.query.all()
```

### 3. **Using SQL Expressions**

For more complex queries or when you need raw SQL, you can use SQL expression language:

- **Direct SQL Expressions**
  ```python
  from sqlalchemy import select
  stmt = select(User).where(User.name == 'John')
  result = session.execute(stmt).scalars().all()
  ```

### 4. **Using the `session.execute()` Method**

For raw SQL queries or when you need to run custom SQL:

- **Raw SQL Query**
  ```python
  result = session.execute("SELECT * FROM users WHERE name = :name", {'name': 'John'}).fetchall()
  ```

### 5. **Using SQLAlchemy Core with ORM**

You can use SQLAlchemy Core’s SQL expression language and then map results to ORM models:

- **Core SQL Expression Language**
  ```python
  from sqlalchemy import select
  stmt = select(User).where(User.name == 'John')
  result = session.execute(stmt)
  users = [User(**row) for row in result]
  ```

### 6. **Using `query_property` with AsyncIO**

If you're using SQLAlchemy with AsyncIO:

- **AsyncIO Queries**
  ```python
  from sqlalchemy.ext.asyncio import AsyncSession
  from sqlalchemy.future import select

  async with AsyncSession(engine) as session:
      result = await session.execute(select(User).filter(User.name == 'John'))
      users = result.scalars().all()
  ```

### Summary

- **ORM Query API**: Fluent and flexible, ideal for most use cases.
- **SQLAlchemy 2.0 Syntax**: Modern approach with direct model queries.
- **SQL Expressions**: For more complex or raw queries.
- **`session.execute()`**: For raw SQL queries and custom commands.
- **SQLAlchemy Core**: For integrating SQL expressions with ORM.
- **AsyncIO**: For asynchronous queries.

Each method has its strengths and is suitable for different types of querying needs in SQLAlchemy.