# -*- coding: utf-8 -*-
"""
Run this script using the BERT virtual environment:
D:\\anaconda\\envs\\BERT\\python.exe import_triples_bert.py
"""

import pandas as pd
from neo4j import GraphDatabase
import sys
import os

# Configuration
EXCEL_FILE_TRIPLES = 'F:/ddg/KG/抽取.xlsx'
EXCEL_FILE_ATTRIBUTES = 'F:/ddg/KG/属性.xlsx'
NEO4J_URI = 'bolt://localhost:7687'
NEO4J_USER = 'neo4j'
NEO4J_PASSWORD = 'xty328310'

def clear_database(driver):
    """Clears all nodes and relationships from the database."""
    print("Clearing database...", flush=True)
    try:
        with driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
        print("Database cleared successfully.", flush=True)
    except Exception as e:
        print(f"Error clearing database: {e}", flush=True)
        sys.exit(1)

def import_triples(driver):
    """Imports triples from Excel file."""
    print(f"Reading Triples Excel file: {EXCEL_FILE_TRIPLES}...", flush=True)
    try:
        # Use header=0 to treat the first row as header
        df = pd.read_excel(EXCEL_FILE_TRIPLES, header=0)
        print(f"Loaded {len(df)} rows from triples file.", flush=True)
        
        expected_cols = ['A', 'relation', 'B']
        if not all(col in df.columns for col in expected_cols):
            print(f"Warning: Expected columns {expected_cols}, but found {df.columns.tolist()}", flush=True)
            if len(df.columns) == 3:
                df.columns = expected_cols
                print(f"Renamed columns to {expected_cols}", flush=True)
            else:
                print("Error: DataFrame must have 3 columns for triples.", flush=True)
                return

    except Exception as e:
        print(f"Error reading Triples Excel file: {e}", flush=True)
        return

    print("Starting triples import...", flush=True)
    count = 0
    
    with driver.session() as session:
        for index, row in df.iterrows():
            try:
                subject = str(row['A']).strip()
                predicate = str(row['relation']).strip()
                object_ = str(row['B']).strip()
                
                if not subject or not predicate or not object_ or subject == 'nan' or object_ == 'nan':
                    continue
                    
                # Sanitize predicate for Cypher relationship type
                safe_predicate = predicate.replace("`", "").replace("'", "")
                
                query = f"""
                MERGE (s:Entity {{name: $subject}})
                MERGE (o:Entity {{name: $object}})
                MERGE (s)-[:`{safe_predicate}`]->(o)
                """
                
                session.run(query, subject=subject, object=object_)
                count += 1
                if count % 100 == 0:
                    print(f"Imported {count} triples...", flush=True)
            except Exception as e:
                print(f"Error importing row {index}: {e}", flush=True)

    print(f"Triples import finished. Total triples imported: {count}", flush=True)

def import_attributes(driver):
    """Imports attributes from Excel file and updates existing nodes."""
    print(f"Reading Attributes Excel file: {EXCEL_FILE_ATTRIBUTES}...", flush=True)
    try:
        # header=0 because 属性.xlsx has a proper header row ['name', 'labels']
        df = pd.read_excel(EXCEL_FILE_ATTRIBUTES, header=0)
        
        # Check columns
        expected_cols = ['name', 'labels']
        if not all(col in df.columns for col in expected_cols):
             # Try to rename if count matches
             if len(df.columns) >= 2:
                  print(f"Warning: Expected columns {expected_cols}, but found {df.columns.tolist()}. Renaming...", flush=True)
                  df = df.iloc[:, :2]
                  df.columns = expected_cols
             else:
                  print(f"Error: Attributes file must have at least 2 columns. Found {len(df.columns)}", flush=True)
                  return
            
        print(f"Loaded {len(df)} rows from attributes file.", flush=True)
        
    except Exception as e:
        print(f"Error reading Attributes Excel file: {e}", flush=True)
        return

    print("Starting attributes import...", flush=True)
    count = 0
    
    with driver.session() as session:
        for index, row in df.iterrows():
            try:
                name = str(row['name']).strip()
                attr_type = str(row['labels']).strip()
                
                if not name or not attr_type or name == 'nan' or attr_type == 'nan':
                    continue
                
                # Sanitize label
                safe_label = attr_type.replace("`", "").replace("'", "")
                
                # Update node: Set property 'type' AND add Label
                query = f"""
                MATCH (n:Entity {{name: $name}})
                SET n.type = $attr_type
                SET n:`{safe_label}`
                """
                
                result = session.run(query, name=name, attr_type=attr_type)
                
                count += 1
                if count % 100 == 0:
                    print(f"Processed {count} attribute rows...", flush=True)
                    
            except Exception as e:
                print(f"Error updating attributes for row {index}: {e}", flush=True)

    print(f"Attributes import finished. Processed {count} rows.", flush=True)

def main():
    print(f"Connecting to Neo4j at {NEO4J_URI}...", flush=True)
    driver = None
    try:
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        driver.verify_connectivity()
        print("Connected successfully.", flush=True)
    except Exception as e:
        print(f"Failed to connect to Neo4j: {e}", flush=True)
        print("Please ensure Neo4j is running and credentials are correct.", flush=True)
        return

    # 1. Clear Database
    clear_database(driver)
    
    # 2. Import Triples
    import_triples(driver)
    
    # 3. Import Attributes
    import_attributes(driver)

    driver.close()
    print("All tasks completed.", flush=True)

if __name__ == "__main__":
    main()
