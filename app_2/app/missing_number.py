class MissingNumber:
    def __init__(self):
        # Conjunto de los primeros 100 números naturales
        self.numbers = list(range(1, 101))

    def extract(self, number: int):
        if not isinstance(number, int):
            raise ValueError("El número debe ser un entero.")
        if number < 1 or number > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if number not in self.numbers:
            raise ValueError("El número ya fue extraído o no existe en el conjunto.")

        self.numbers.remove(number)

    def find_missing(self) -> int:
        # Suma de 1 a 100
        total_expected = 100 * 101 // 2  
        total_actual = sum(self.numbers)
        return total_expected - total_actual
