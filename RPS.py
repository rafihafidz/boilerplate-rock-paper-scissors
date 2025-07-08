def player(prev_play, opponent_history=[], play_order={}):
    if prev_play:
        opponent_history.append(prev_play)

    # Inisialisasi strategi berdasarkan deteksi lawan
    n = 3
    if len(opponent_history) < n:
        return "R"

    # Simpan sekuens terakhir lawan untuk pola
    last_moves = "".join(opponent_history[-n:])

    if last_moves not in play_order:
        play_order[last_moves] = {"R": 0, "P": 0, "S": 0}

    if len(opponent_history) > n:
        prev_seq = "".join(opponent_history[-n - 1 : -1])
        play_order[prev_seq][opponent_history[-1]] += 1

    # Prediksi langkah lawan selanjutnya berdasarkan frekuensi
    possible = play_order[last_moves]
    prediction = max(possible, key=possible.get)

    # Balas dengan langkah yang mengalahkan prediksi
    return counter_move(prediction)


def counter_move(move):
    if move == "R":
        return "P"
    elif move == "P":
        return "S"
    elif move == "S":
        return "R"
