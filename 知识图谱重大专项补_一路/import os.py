import os
import json
import argparse
from py2neo import Graph

def to_node(identity, labels, props):
    return {"identity": identity, "labels": labels, "properties": props, "elementId": str(identity)}

def to_rel(rel_id, start_id, end_id, rel_type, rel_props):
    return {"identity": rel_id, "start": start_id, "end": end_id, "type": rel_type, "properties": rel_props, "elementId": str(rel_id), "startNodeElementId": str(start_id), "endNodeElementId": str(end_id)}

def export(output_path):
    graph = Graph('bolt://localhost:7687', auth=("neo4j", "xty328310"))
    q = '''
    MATCH (start)-[rel]->(end)
    RETURN id(start) AS startId, labels(start) AS startLabels, properties(start) AS startProps,
           id(end) AS endId, labels(end) AS endLabels, properties(end) AS endProps,
           id(rel) AS relId, type(rel) AS relType, properties(rel) AS relProps
    '''
    data = graph.run(q).data()
    out = []
    for r in data:
        start = to_node(r["startId"], r["startLabels"], r["startProps"])
        end = to_node(r["endId"], r["endLabels"], r["endProps"])
        rel = to_rel(r["relId"], r["startId"], r["endId"], r["relType"], r["relProps"])
        seg = {"start": start, "relationship": rel, "end": end}
        out.append({"p": {"start": start, "end": end, "segments": [seg], "length": 1.0}})
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--output", default=r"D:\\Desktop\\盾构机\\重大专项\\知识图谱重大专项补\\盾构机换刀.json")
    args = parser.parse_args()
    export(args.output)