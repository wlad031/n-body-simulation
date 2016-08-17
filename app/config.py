AppConfig = {

    'window_width': 1024,
    'window_height': 640,
}

GravitationalSystemConfig = {

    'color': '#222222',
    'G': 6.0e-1,
    'dt': 0.1,

    'particles':
        [
            {
                'id': 0,
                'position': [120, 320],
                'speed': [0, 0],
                'mass': 10000,
                'radius': 4,
                'color': '#0000FF',
            },

            {
                'id': 1,
                'position': [320, 320],
                'speed': [0, 0],
                'mass': 10000,
                'radius': 4,
                'color': '#00FFFF',
            },
        ],
    # [
    #
    #     {
    #         'id': 0,
    #         'position': [120, 320],
    #         'speed': [0, -12],
    #         'mass': 1000,
    #         'radius': 2,
    #         'color': '#0000FF',
    #     },
    #
    #     {
    #         'id': 1,
    #         'position': [320, 320],
    #         'speed': [0, 0],
    #         'mass': 100000,
    #         'radius': 4,
    #         'color': '#00FFFF',
    #     },
    #
    #     {
    #         'id': 2,
    #         'position': [520, 320],
    #         'speed': [0, 10],
    #         'mass': 1000,
    #         'radius': 2,
    #         'color': '#00FF00',
    #     },
    # ]
}
