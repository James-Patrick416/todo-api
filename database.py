from sqlalchemy import create_engine, text
engine = create_engine('postgresql://postgres:postgres@localhost/todo_api')
with engine.connect() as conn:
    result = conn.execute(text("SELECT 'Database connection successful!'"))
    print(result.scalar())