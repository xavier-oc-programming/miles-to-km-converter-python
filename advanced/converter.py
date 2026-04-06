from config import FACTOR_MI_KM, MODE_IMP2MET


class Converter:
    """Pure conversion logic — no UI, no print(), no input()."""

    def miles_to_km(self, miles: float) -> float:
        return miles * FACTOR_MI_KM

    def km_to_miles(self, km: float) -> float:
        return km / FACTOR_MI_KM

    def convert(self, value: float, mode: str) -> float:
        """Convert value using the given mode constant."""
        if mode == MODE_IMP2MET:
            return self.miles_to_km(value)
        return self.km_to_miles(value)
