"""Store constants shared within miscellaneous files of the app"""

CONSTANTS = {
    "tableTitles": [
        "Title",
        "Weight [kg]",
        "Category",
        "Description",
        "Delivery date",
        "Posted",
    ],
    "materialsToSelect": [
        "Alloy Steel",
        "Aluminum",
        "Copper",
        "Iron",
        "Steel",
        "Timber",
        "Other",
    ],
    "selectionParameters": {
        "sortingOrderKeys": [
            "title asc",
            "title desc",
            "weight asc",
            "weight desc",
            "delivery_date asc",
            "delivery_date desc",
        ],
        "sortingOrderTitles": [
            "Title A to Z",
            "Title Z to A",
            "Lowest storage weight",
            "Highest storage weight",
            "Oldest trade date",
            "Newest trade date",
        ],
        "filterBalanceKeys": [
            "entireBalance",
            "purchasedMaterials",
            "soldMaterials",
        ],
        "filterBalanceTitles": [
            "Entire balance",
            "Purchased materials only",
            "Sold materials only",
        ],
        "filterHistoryKeys": [
            "fromVeryBeginning",
            "0",
            "7",
            "30",
            "365",
            "futureTrades",
        ],
        "filterHistoryTitles": [
            "From very beginning",
            "Today's trades",
            "From last 7 days",
            "From last 30 days",
            "From last 365 days",
            "Future trades",
        ],
    },
}
