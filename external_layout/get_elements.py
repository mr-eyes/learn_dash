def get_elements():
    nodes = [
    {
        'data': {'id': short, 'label': label} # ,
        # 'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label, long, lat in (
        ('la', 'Los Angeles', 34.03, -118.25),
        ('nyc', 'New York', 40.71, -74),
        ('to', 'Toronto', 43.65, -79.38),
        ('mtl', 'Montreal', 45.50, -73.57),
        ('van', 'Vancouver', 49.28, -123.12),
        ('chi', 'Chicago', 41.88, -87.63),
        ('bos', 'Boston', 42.36, -71.06),
        ('hou', 'Houston', 29.76, -95.37))
    ]

    edges = [
        {'data': {'source': source, 'target': target}}
        for source, target in (
            ('van', 'la'),
            ('la', 'chi'),
            ('hou', 'chi'),
            ('to', 'mtl'),
            ('mtl', 'bos'),
            ('nyc', 'boston'),
            ('to', 'hou'),
            ('to', 'nyc'),
            ('la', 'nyc'),
            ('nyc', 'bos')
        )
    ]

    elements = nodes + edges

    return elements