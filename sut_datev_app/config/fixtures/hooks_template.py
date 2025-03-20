
# Fixtures Configuration for sut_datev_app
# This is automatically generated based on your customization export

fixtures = [
    "Taetigkeitsbezeichnung",
    "Bereich",
    "Grundlage der Verguetung",
    {
        "dt": "Custom Field",
        "filters": [
            [
                "dt",
                "in",
                [
                    "Employee",
                    "Project"
                ]
            ]
        ]
    },
    {
        "dt": "Property Setter",
        "filters": [
            [
                "doc_type",
                "in",
                [
                    "Employee",
                    "Project"
                ]
            ]
        ]
    },
    {
        "dt": "Client Script",
        "filters": []
    },
    {
        "dt": "Server Script",
        "filters": []
    }
]
