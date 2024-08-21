import unittest
from src.weather_fetcher import get_weather

class TestWeatherFetcher(unittest.TestCase):
    def test_get_weather(self):
        
        #call the function
        tem, description = get_weather()
        
        #basic checks
        self.assertIsInstance(temp, (int, float),"Temperature")
        self.assertIsInstance(description, str, "weather description")
        
        #further checks can be added if needed
        
if __name__ == "__main__":
    unittest.main()