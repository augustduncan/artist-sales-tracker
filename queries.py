import sqlite3
import pandas as pd

def products(conn):
    return pd.read_sql_query("SELECT name FROM inventory ORDER BY name", conn)["name"]

def show_inventory(conn):
    return pd.read_sql_query("SELECT * FROM inventory", conn)

# def orphan_count(conn):
#     return pd.read_sql_query(
#         "SELECT COUNT(*) AS n FROM bed_log WHERE bed_id NOT IN (SELECT bed_id FROM bed)",
#         conn,
#     )["n"][0]
#would it make sense for us to have something like this? Every table feels pretty independent from eachother. Even transactions referencing an item no longer sold shouldn't be an issue due to foreign key restraint.

# hmmm im not sure. my initial thought is no, but i can imagine wanting to kind of seperate items not sold anymore.
# i think we come back to it once we have some functionality and see if it makes sense