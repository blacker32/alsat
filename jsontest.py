
import json
with open("filename.json", "r") as f:
    content = json.loads(f.read())
    content = {"name": "Joe", "age": 20}
with open("filename.json", "w") as f:
    f.write(json.dumps(content, indent=2))