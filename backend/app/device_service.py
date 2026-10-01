def check_device_status(device: str):
    if device.lower() == "warehouse scanner":
        return {
            "device": device,
            "status": "offline",
            "message": f"{device} is currently offline.",
        }

    return {
        "device": device,
        "status": "operational",
        "message": f"{device} is currently reachable.",
    }