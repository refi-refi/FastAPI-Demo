from datetime import datetime


def function_0(data_id: int, x: int, y: int, z: int = 3):
    return {
        "timestamps": [datetime.now() for _ in range(data_id)],
        "values": x + y + z
    }


def function_1(x: int, y: int, z: int = 1, data_id: int | None = None):
    if data_id:
        return (x + y + z) * data_id
    return x + y + z


def function_2(x, y, z, t):
    return 0


def function_3():
    pass
