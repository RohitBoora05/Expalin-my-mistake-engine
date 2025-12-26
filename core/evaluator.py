from dataclasses import dataclass
from core.context import AttemptContext 

@dataclass(frozen=True)
class EvaluationResult:

    is_correct : bool
    marked_option : str
    correct_option : str

def evaluate_attempt(context : AttemptContext) -> EvaluationResult:

    return EvaluationResult(
        is_correct=context.is_correct,
        marked_option=context.marked_option,
        correct_option=context.correct_option
    )