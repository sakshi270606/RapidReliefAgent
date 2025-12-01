def create_message(sender, receiver, payload):
    return {"from": sender, "to": receiver, "payload": payload}
