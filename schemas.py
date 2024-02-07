pet = {
    "type": "object",
    "required": ["id","name", "type","status"],
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string",
            "enum": ["cat", "dog", "fish"]
        },
        "status": {
            "type": "string",
            "enum": ["available", "sold", "pending"]
        },
    }
}

Order = {
    "type": "object",
    "required": ["id","pet_id"],
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "pet_id": {
            "type": "integer"
        }
    }
}