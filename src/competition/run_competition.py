import argparse
from typing import Callable

from src.competition import COMPETITORS
from src.engine import GomokuEngine

WINNER_POINT = 3
LOSER_POINT = -1


def single_match(
    engine: GomokuEngine, start_action_fun: Callable, sec_action_fun: Callable
):
    engine.reset()

    while True:
        start_a = start_action_fun(
            engine.state, engine.history, engine.active_player
        )
        engine.step(start_a, check_action=True)
        if engine.state.is_over:
            break

        sec_a = sec_action_fun(
            engine.state, engine.history, engine.active_player
        )
        engine.step(sec_a, check_action=True)
        if engine.state.is_over:
            break

    return engine.state.winner


def main(args):
    engine = GomokuEngine(args.board_size, win_len=args.win_len)
    players = list(COMPETITORS.keys())

    player_points = {name: 0 for name in players}

    for first_player in players:
        for second_player in players:
            if first_player == second_player:
                continue

            game_stats = {pl: 0 for pl in [-1, 0, 1]}
            for _ in range(args.num_matches_per_pair):
                winner = single_match(
                    engine,
                    COMPETITORS[first_player],
                    COMPETITORS[second_player],
                )
                game_stats[winner] += 1
                if winner == 1:  # start player won
                    player_points[first_player] += WINNER_POINT
                    player_points[second_player] -= LOSER_POINT

            print(
                f"{first_player} vs {second_player}."
                f" {first_player} won {game_stats[1]}"
                f" times, {second_player} won {game_stats[-1]}"
                f" times, draw {game_stats[0]} times."
            )

    names_points = sorted(list(player_points.items()), key=lambda x: -x[1])

    print("\n*** Final results ***")
    for i, (name, point) in enumerate(names_points):
        print(f"{i+1}. {name}: {point}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--board_size",
        "-s",
        type=int,
        default=20,
        help="size of the board (square board only)",
    )
    parser.add_argument(
        "--win_len",
        "-l",
        type=int,
        default=5,
        help="player wins with L contiguous signs",
    )
    parser.add_argument(
        "--num_matches_per_pair",
        type=int,
        default=100,
        help="given first player and second player, how many matches to play.",
    )
    args = parser.parse_args()

    main(args)
