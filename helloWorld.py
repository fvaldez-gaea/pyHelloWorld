import json

def handler(ctx, data: bytes = None):
    try:
        body = json.loads(data)
        name = body.get("name", "World")
    except (Exception, ValueError) as ex:
        name = "World"
    
    response = {
        "message": f"Hello, {name}"
    }

    return json.dumps(response)