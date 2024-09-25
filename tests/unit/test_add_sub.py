from unittest import TestCase
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from hijridate import Hijri


class HijriDateTests(TestCase):
    def test_hijri_date_add_year(self):
        # Test adding 1 year to '1446-01-29'
        original_date = Hijri(1446, 1, 29)
        delta = relativedelta(years=1)
        new_date = original_date + delta
        expected_date = Hijri(1447, 1, 29)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Adding 1 year failed.")

    def test_hijri_date_add_month(self):
        # Test adding 2 months to '1446-11-15'
        original_date = Hijri(1446, 11, 15)
        delta = relativedelta(months=2)
        new_date = original_date + delta
        expected_date = Hijri(1447, 1, 15)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Adding 2 months failed.")

    def test_hijri_date_add_day(self):
        # Test adding 10 days to '1446-12-25'
        original_date = Hijri(1446, 12, 25)
        delta = timedelta(days=10)
        new_date = original_date + delta
        expected_date = Hijri(1447, 1, 6)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Adding 10 days failed.")

    def test_hijri_date_sub_year(self):
        # Test subtracting 1 year from '1447-01-30'
        original_date = Hijri(1447, 1, 30)
        delta = relativedelta(years=1)
        new_date = original_date - delta
        expected_date = Hijri(1446, 1, 29)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 1 year failed.")

    def test_hijri_date_sub_month(self):
        # Test subtracting 3 months from '1447-03-10'
        original_date = Hijri(1447, 3, 10)
        delta = relativedelta(months=3)
        new_date = original_date - delta
        expected_date = Hijri(1446, 12, 10)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 3 months failed.")

    def test_hijri_date_sub_day(self):
        # Test subtracting 15 days from '1447-01-15'
        original_date = Hijri(1447, 1, 15)
        delta = timedelta(days=15)
        new_date = original_date - delta
        expected_date = Hijri(1446, 12, 29)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 15 days failed.")

    def test_hijri_date_add_complex(self):
        # Test adding a complex interval to '1446-11-28'
        original_date = Hijri(1446, 11, 28)
        delta = relativedelta(years=1, months=2, days=5)
        new_date = original_date + delta
        expected_date = Hijri(1448, 2, 4)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Adding complex interval failed.")

    def test_hijri_date_sub_complex(self):
        # Test subtracting a complex interval from '1447-05-20'
        original_date = Hijri(1447, 5, 20)
        delta = relativedelta(years=2, months=6, days=10)
        new_date = original_date - delta
        expected_date = Hijri(1444, 11, 10)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting complex interval failed.")

    def test_hijri_date_add_overflow(self):
        # Test adding 40 days to '1446-12-20'
        original_date = Hijri(1446, 12, 20)
        delta = timedelta(days=40)
        new_date = original_date + delta
        expected_date = Hijri(1447, 2, 1)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Adding 40 days failed.")

    def test_hijri_date_sub_underflow(self):
        # Test subtracting 50 days from '1447-01-15'
        original_date = Hijri(1447, 1, 15)
        delta = timedelta(days=50)
        new_date = original_date - delta
        expected_date = Hijri(1446, 11, 23)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 50 days failed.")

    def test_subtracting_month_resulting_in_previous_year(self):
        # 1447-01-05, subtracting 1 month should give us 1446-12-05
        original_date = Hijri(1447, 1, 5)
        delta = relativedelta(months=1)
        new_date = original_date - delta
        expected_date = Hijri(1446, 12, 5)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 1 months failed.")

    def test_subtracting_days_resulting_in_previous_month(self):
        # 1447-01-05, subtracting 10 days should give us 1446-12-24
        original_date = Hijri(1447, 1, 5)
        delta = relativedelta(days=10)
        new_date = original_date - delta
        expected_date = Hijri(1446, 12, 24)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 10 days failed.")

    def test_subtracting_multiple_months(self):
        # 1447-03-15, subtracting 4 months should give us 1446-11-15
        original_date = Hijri(1447, 3, 15)
        delta = relativedelta(months=4)
        new_date = original_date - delta
        expected_date = Hijri(1446, 11, 15)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 4 months failed.")

    def test_subtracting_large_number_of_days(self):
        # 1447-03-01, subtracting 90 days should give us 1446-12-01
        original_date = Hijri(1447, 3, 1)
        delta = relativedelta(days=90)
        new_date = original_date - delta
        expected_date = Hijri(1446, 11, 28)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 90 days failed.")

    def test_subtracting_one_month(self):
        # Assuming 1447 is a leap year, subtracting 1 month from 1447-12-30 should give us 1447-11-30
        original_date = Hijri(1445, 12, 30)
        delta = relativedelta(months=1)
        new_date = original_date - delta
        expected_date = Hijri(1447, 11, 29)
        self.assertEqual(new_date.isoformat(), expected_date.isoformat(), "Subtracting 1 month failed.")
