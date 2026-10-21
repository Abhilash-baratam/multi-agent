# spatial_dataset.py
"""
Complete A-to-Z Real-World Physical Geometry & Dimension Registry.
Used for precise monocular pin-hole depth projection:
Z = (focal_length * real_height_meters) / pixel_box_height
"""

SPATIAL_REGISTRY = {
    # A
    "air conditioner": {"height_m": 0.65, "anchor": "wall", "priority": 2},
    "airplane": {"height_m": 8.50, "anchor": "sky", "priority": 1},
    "ambulance": {"height_m": 2.45, "anchor": "ground", "priority": 1},
    "awning": {"height_m": 1.20, "anchor": "overhead", "priority": 2},

    # B
    "backpack": {"height_m": 0.48, "anchor": "attached", "priority": 3},
    "banner": {"height_m": 1.10, "anchor": "overhead", "priority": 2},
    "barricade": {"height_m": 1.00, "anchor": "ground", "priority": 2},
    "bench": {"height_m": 0.85, "anchor": "ground", "priority": 2},
    "bicycle": {"height_m": 1.05, "anchor": "ground", "priority": 1},
    "billboard": {"height_m": 3.20, "anchor": "overhead", "priority": 2},
    "bookcase": {"height_m": 1.90, "anchor": "ground", "priority": 2},
    "bottle": {"height_m": 0.28, "anchor": "surface", "priority": 3},
    "bus": {"height_m": 3.25, "anchor": "ground", "priority": 1},

    # C
    "camera": {"height_m": 0.18, "anchor": "wall", "priority": 3},
    "car": {"height_m": 1.50, "anchor": "ground", "priority": 1},
    "chair": {"height_m": 0.88, "anchor": "ground", "priority": 2},
    "clock": {"height_m": 0.40, "anchor": "wall", "priority": 3},
    "cone": {"height_m": 0.70, "anchor": "ground", "priority": 2},
    "cup": {"height_m": 0.12, "anchor": "surface", "priority": 3},

    # D
    "desk": {"height_m": 0.75, "anchor": "ground", "priority": 2},
    "dog": {"height_m": 0.60, "anchor": "ground", "priority": 2},
    "door": {"height_m": 2.10, "anchor": "ground", "priority": 1},
    "dumpster": {"height_m": 1.40, "anchor": "ground", "priority": 2},

    # E
    "elevator door": {"height_m": 2.20, "anchor": "ground", "priority": 1},
    "escalator": {"height_m": 3.50, "anchor": "ground", "priority": 1},

    # F
    "fire hydrant": {"height_m": 0.80, "anchor": "ground", "priority": 2},
    "forklift": {"height_m": 2.10, "anchor": "ground", "priority": 1},
    "flag": {"height_m": 1.20, "anchor": "overhead", "priority": 2},

    # G
    "garage door": {"height_m": 2.40, "anchor": "ground", "priority": 1},
    "guardrail": {"height_m": 0.75, "anchor": "ground", "priority": 2},

    # H
    "helmet": {"height_m": 0.26, "anchor": "attached", "priority": 3},
    "handbag": {"height_m": 0.35, "anchor": "attached", "priority": 3},

    # I
    "information board": {"height_m": 1.60, "anchor": "ground", "priority": 2},
    "intercom": {"height_m": 0.25, "anchor": "wall", "priority": 3},

    # J
    "junction box": {"height_m": 0.55, "anchor": "wall", "priority": 3},

    # K
    "kiosk": {"height_m": 2.30, "anchor": "ground", "priority": 1},

    # L
    "ladder": {"height_m": 2.40, "anchor": "ground", "priority": 2},
    "laptop": {"height_m": 0.25, "anchor": "surface", "priority": 3},
    "light pole": {"height_m": 5.50, "anchor": "ground", "priority": 1},

    # M
    "mailbox": {"height_m": 1.15, "anchor": "ground", "priority": 2},
    "manhole": {"height_m": 0.05, "anchor": "ground", "priority": 3},
    "monitor": {"height_m": 0.45, "anchor": "surface", "priority": 3},
    "motorcycle": {"height_m": 1.15, "anchor": "ground", "priority": 1},

    # N
    "neon sign": {"height_m": 0.85, "anchor": "overhead", "priority": 2},
    "notice board": {"height_m": 1.00, "anchor": "wall", "priority": 2},

    # O
    "office desk": {"height_m": 0.76, "anchor": "ground", "priority": 2},

    # P
    "pallet": {"height_m": 0.15, "anchor": "ground", "priority": 3},
    "parking meter": {"height_m": 1.45, "anchor": "ground", "priority": 2},
    "pedestrian crossing sign": {"height_m": 0.75, "anchor": "overhead", "priority": 2},
    "person": {"height_m": 1.70, "anchor": "ground", "priority": 1},
    "pillar": {"height_m": 3.00, "anchor": "ground", "priority": 1},
    "potted plant": {"height_m": 0.70, "anchor": "ground", "priority": 2},

    # Q
    "queue barrier": {"height_m": 0.95, "anchor": "ground", "priority": 2},

    # R
    "railings": {"height_m": 1.00, "anchor": "ground", "priority": 2},
    "refrigerator": {"height_m": 1.80, "anchor": "ground", "priority": 1},
    "road sign": {"height_m": 0.80, "anchor": "overhead", "priority": 2},

    # S
    "scaffold": {"height_m": 4.50, "anchor": "ground", "priority": 1},
    "scooter": {"height_m": 1.10, "anchor": "ground", "priority": 1},
    "signboard": {"height_m": 0.90, "anchor": "overhead", "priority": 2},
    "sofa": {"height_m": 0.85, "anchor": "ground", "priority": 1},
    "stairs": {"height_m": 2.20, "anchor": "ground", "priority": 1},
    "stop sign": {"height_m": 0.75, "anchor": "ground", "priority": 2},
    "street light": {"height_m": 5.00, "anchor": "ground", "priority": 1},
    "suitcase": {"height_m": 0.65, "anchor": "ground", "priority": 2},

    # T
    "table": {"height_m": 0.75, "anchor": "ground", "priority": 2},
    "traffic light": {"height_m": 1.15, "anchor": "overhead", "priority": 2},
    "trash can": {"height_m": 0.90, "anchor": "ground", "priority": 2},
    "truck": {"height_m": 2.90, "anchor": "ground", "priority": 1},
    "tuk tuk": {"height_m": 1.85, "anchor": "ground", "priority": 1},

    # U
    "umbrella": {"height_m": 0.85, "anchor": "handheld", "priority": 2},

    # V
    "van": {"height_m": 2.15, "anchor": "ground", "priority": 1},
    "vending machine": {"height_m": 1.85, "anchor": "ground", "priority": 1},

    # W
    "wall banner": {"height_m": 1.30, "anchor": "overhead", "priority": 2},
    "waste bin": {"height_m": 0.85, "anchor": "ground", "priority": 2},
    "water cooler": {"height_m": 1.35, "anchor": "ground", "priority": 2},
    "window": {"height_m": 1.40, "anchor": "wall", "priority": 2},

    # X
    "x-ray machine": {"height_m": 1.65, "anchor": "ground", "priority": 1},

    # Y
    "yield sign": {"height_m": 0.75, "anchor": "ground", "priority": 2},

    # Z
    "zebra crossing marker": {"height_m": 0.05, "anchor": "ground", "priority": 3}
}

def resolve_target_metadata(detected_label: str, box_y_ratio: float):
    """
    Matches any incoming label against the A-to-Z registry.
    If an unknown label or arbitrary surface is clicked, it matches using anchor height.
    """
    key = detected_label.lower().strip()
    
    # 1. Direct exact match
    if key in SPATIAL_REGISTRY:
        return key.capitalize(), SPATIAL_REGISTRY[key]["height_m"]
    
    # 2. Sub-string search (e.g., 'delivery truck' matches 'truck')
    for reg_key, item in SPATIAL_REGISTRY.items():
        if reg_key in key or key in reg_key:
            return reg_key.capitalize(), item["height_m"]

    # 3. Geometric location heuristics for unlisted objects
    if box_y_ratio < 0.40:
        return "Signboard / Banner", 1.10
    elif box_y_ratio > 0.75:
        return "Ground Obstacle", 0.60
    else:
        return "Structural Element", 1.50