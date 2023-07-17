WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

BLOCK_MAP = [
    '555555555',
    '444444444',
    '333333333',
    '222222222',
    '        ',
    '        ',
]

COLOR_LEGEND: {
    '1': 'blue',
    '2': 'green',
    '3': 'yellow',
    '4': 'orange',
    '5': 'grey'
}

GAP_SIZE = 2

BLOCK_HEIGHT = WINDOW_HEIGHT/len(BLOCK_MAP) - GAP_SIZE
BLOCK_WIDTH = WINDOW_WIDTH/len(BLOCK_MAP[0]) - GAP_SIZE