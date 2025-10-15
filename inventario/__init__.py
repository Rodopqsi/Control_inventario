try:
    import pymysql  # type: ignore
    pymysql.install_as_MySQLdb()
except Exception:
    # If PyMySQL isn't installed yet, ignore. SQLite fallback still works.
    pass
