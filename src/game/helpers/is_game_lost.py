def is_game_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False
