def calculate_summary(materials):
    """Calculate summary used in balance visualisation"""
    summary = {}

    selected_purchases_list = list(
        map(lambda material: material.weight if material.weight > 0 else 0, materials)
    )
    summary["selectedPurchasedMaterials"] = round(sum(selected_purchases_list), 3)

    selected_sells_list = list(
        map(lambda material: material.weight if material.weight < 0 else 0, materials)
    )
    summary["selectedSoldMaterials"] = round(sum(selected_sells_list), 3)

    total_balance = (
        summary["selectedPurchasedMaterials"] + summary["selectedSoldMaterials"]
    )
    summary["total_balance"] = round(total_balance, 3)

    return summary
