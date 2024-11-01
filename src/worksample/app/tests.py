from django.test import TestCase
from django.core.management import call_command
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from freezegun import freeze_time


# Create your tests here.
class TicketTestCase(TestCase):
    # 月曜日時間割引なし
    @freeze_time("2024-11-04 16:50:00")
    def test_Monday_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 4000円", output.getvalue())

    # 月曜日時間割引あり
    @freeze_time("2024-11-04 17:50:00")
    def test_Monday_Evening_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 3400円", output.getvalue())

    # 月曜日団体割引あり
    @freeze_time("2024-11-04 16:50:00")
    def test_Monday_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 5300円", output.getvalue())

    # 月曜日団体割引あり
    @freeze_time("2024-11-04 17:50:00")
    def test_Monday_Evening_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 4560円", output.getvalue())

    # 月曜日時間割引なし
    @freeze_time("2024-11-04 16:50:00")
    def test_Monday_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 2400円", output.getvalue())

    # 月曜日時間割引あり
    @freeze_time("2024-11-04 17:50:00")
    def test_Monday_Evening_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 1800円", output.getvalue())

    # 月曜日団体割引あり
    @freeze_time("2024-11-04 16:50:00")
    def test_Monday_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 3120円", output.getvalue())

    # 月曜日団体割引あり
    @freeze_time("2024-11-04 17:50:00")
    def test_Monday_Evening_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 2380円", output.getvalue())

    # 火曜日時間割引なし
    @freeze_time("2024-11-05 16:50:00")
    def test_Tuesday_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 4600円", output.getvalue())

    # 火曜日時間割引あり
    @freeze_time("2024-11-05 17:50:00")
    def test_Tuesday_Evening_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 4000円", output.getvalue())

    # 火曜日団体割引あり
    @freeze_time("2024-11-05 16:50:00")
    def test_Tuesday_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 6040円", output.getvalue())

    # 火曜日団体割引あり
    @freeze_time("2024-11-05 17:50:00")
    def test_Tuesday_Evening_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 5300円", output.getvalue())

    # 火曜日時間割引なし
    @freeze_time("2024-11-05 16:50:00")
    def test_Tuesday_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 3000円", output.getvalue())

    # 火曜日時間割引あり
    @freeze_time("2024-11-05 17:50:00")
    def test_Tuesday_Evening_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 2400円", output.getvalue())

    # 火曜日団体割引あり
    @freeze_time("2024-11-05 16:50:00")
    def test_Tuesday_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 3860円", output.getvalue())

    # 火曜日団体割引あり
    @freeze_time("2024-11-05 17:50:00")
    def test_Tuesday_Evening_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 3120円", output.getvalue())

    # 日曜日時間割引なし
    @freeze_time("2024-11-10 16:50:00")
    def test_Sunday_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 5800円", output.getvalue())

    # 日曜日時間割引あり
    @freeze_time("2024-11-10 17:50:00")
    def test_Sunday_Evening_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", stdout=output)
        self.assertIn("合計金額: 5200円", output.getvalue())

    # 日曜日団体割引あり
    @freeze_time("2024-11-10 16:50:00")
    def test_Sunday_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 7520円", output.getvalue())

    # 日曜日団体割引あり
    @freeze_time("2024-11-10 17:50:00")
    def test_Sunday_Evening_Group_Ticket(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", stdout=output)
        self.assertIn("合計金額: 6780円", output.getvalue())

    # 日曜日時間割引なし
    @freeze_time("2024-11-10 16:50:00")
    def test_Sunday_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 4200円", output.getvalue())

    # 日曜日時間割引あり
    @freeze_time("2024-11-10 17:50:00")
    def test_Sunday_Evening_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "2", "-c", "2", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 3600円", output.getvalue())

    # 日曜日団体割引あり
    @freeze_time("2024-11-10 16:50:00")
    def test_Sunday_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 5340円", output.getvalue())

    # 日曜日団体割引あり
    @freeze_time("2024-11-10 17:50:00")
    def test_Sunday_Evening_Group_Ticket_SP(self):
        output = StringIO()
        call_command("ticket", "-a", "4", "-c", "4", "-s", "2", "-sp", stdout=output)
        self.assertIn("合計金額: 4600円", output.getvalue())
