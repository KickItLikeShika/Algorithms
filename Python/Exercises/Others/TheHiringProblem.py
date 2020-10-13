def hire_assistant(candidates):
    best_candidate = -1
    for i in range(len(candidates)):
        if candidates[i] > best_candidate:
            best_candidate = candidates[i]

    return best_candidate


if __name__ == "__main__":
    candidates = [5, 9, 2, 1, 0, 7, 15, 14, 19, 28, 30, 22, 17]
    best_candidate = hire_assistant(candidates)
    print(best_candidate)