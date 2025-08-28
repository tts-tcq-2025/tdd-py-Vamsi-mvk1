import re

class StringCalculator:
    """Simplified StringCalculator with fewer helper methods."""
    
    def __init__(self):
        self.default_delimiters = [',', '\n']

    def add(self, numbers: str) -> int:
        """Add numbers from a string input."""
        if not numbers:
            return 0

        # Handle custom delimiter
        delimiters = self.default_delimiters[:]
        if numbers.startswith("//"):
            delimiter_part, numbers = numbers.split("\n", 1)
            delimiter_part = delimiter_part[2:]
            if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
                # Support delimiters inside brackets
                delimiter_part = delimiter_part[1:-1]
            delimiters.append(re.escape(delimiter_part))

        # Build regex pattern for all delimiters
        pattern = "|".join(map(re.escape, delimiters))
        
        # Split and convert
        nums = [int(n) for n in re.split(pattern, numbers) if n.strip()]
        
        # Validate negatives
        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        # Ignore numbers > 1000
        nums = [n for n in nums if n <= 1000]

        return sum(nums)
