from src.competition.competitors.Balazs.main import take_action as action_balazs
from src.competition.competitors.David.main import take_action as action_david
from src.competition.competitors.Jona.main import take_action as action_jona

COMPETITORS = {
    "Balazs": action_balazs,
    "Jona": action_jona,
    "David": action_david,
}
