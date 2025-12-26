from dataclasses import dataclass
from typing import List, Optional

@dataclass(frozen=True)
class AttemptContext:

    # question metadeta 
    question_id : str
    subject : str
    topic : str
    difficulty : str
    
    #attempt metadeta 
    time_taken : float
    final_anser_time : float
    confidence : float

    marked_option : str
    correct_option : str

    #reassoning 
    option_elimination : List[str]
    option_change : int
    reasoning_started : Optional[bool]

    #derived helper
    @property
    def is_correct(self) -> bool:
        return self.marked_option == self.correct_option
    