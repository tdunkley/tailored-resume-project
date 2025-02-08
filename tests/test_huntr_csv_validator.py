import unittest
from huntr_csv_validator import validate_email, validate_url, validate_date, is_duplicate

class TestHuntrCSVValidator(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid-email"))

    def test_validate_url(self):
        self.assertTrue(validate_url("https://example.com"))
        self.assertFalse(validate_url("invalid-url"))

    def test_validate_date(self):
        self.assertTrue(validate_date("2025-01-01"))
        self.assertFalse(validate_date("01-01-2025"))

    def test_is_duplicate(self):
        existing_entries = [
            {"job_title": "Data Scientist", "company_name": "Company A", "job_description": "Analyze data"}
        ]
        new_entry = {"job_title": "Data Scientist", "company_name": "Company A", "job_description": "Analyze data"}
        self.assertTrue(is_duplicate(new_entry, existing_entries))

        new_entry = {"job_title": "Data Engineer", "company_name": "Company B", "job_description": "Build pipelines"}
        self.assertFalse(is_duplicate(new_entry, existing_entries))

if __name__ == "__main__":
    unittest.main()
