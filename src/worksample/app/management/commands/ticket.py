from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from dataclasses import dataclass, field
from typing import List, Dict
import datetime


@dataclass
class TicketInfo:
    total: int = 0
    adults: int = 0
    childs: int = 0
    seniors: int = 0
    plan: str = "NORMAL"
    weekday_discount: int = 0
    time_discount: int = 0
    total_discount: bool = False
    discounts: Dict[str, int] = field(default_factory=dict)
    ticket_prices: List[int] = field(default_factory=list)
    total_price: int = 0
    prices: Dict[str, int] = field(default_factory=dict)


class Command(BaseCommand):
    help = "動物園のチケット販売価格計算"

    def add_arguments(self, parser):
        parser.add_argument("-a", "--adult", default=0, type=int)
        parser.add_argument("-c", "--child", default=0, type=int)
        parser.add_argument("-s", "--senior", default=0, type=int)
        parser.add_argument("-sp", "--special", action="store_true")

    def handle(self, *args, **options):
        dt = datetime.datetime.now()
        data = TicketInfo()
        data.adults = options.get("adult", 0)
        data.childs = options.get("child", 0)
        data.seniors = options.get("senior", 0)
        if options.get("special", False):
            data.plan = "SPECIAL"
        # dt = datetime.datetime(2024, 11, 4, 16, 50, 0)

        # 合計人数
        data.total = data.adults + data.childs + data.seniors

        # チケット料金
        data.ticket_prices = self.check_plan(data.plan)

        # 曜日別料金
        data.weekday_discount = self.check_weekday(dt)

        # 時間帯別料金
        data.time_discount = self.check_time(dt)

        # 単純合計料金
        data.total_price = (
            (data.ticket_prices["ADULT"] * data.adults)
            + (data.ticket_prices["CHILD"] * data.childs)
            + (data.ticket_prices["SENIOR"] * data.seniors)
        )

        # 大人料金
        data.prices["ADULT"] = (
            data.ticket_prices["ADULT"] + data.weekday_discount + data.time_discount
        ) * data.adults
        # 子供料金
        data.prices["CHILD"] = (
            data.ticket_prices["CHILD"] + data.weekday_discount + data.time_discount
        ) * data.childs
        # シニア料金
        data.prices["SENIOR"] = (
            data.ticket_prices["SENIOR"] + data.weekday_discount + data.time_discount
        ) * data.seniors

        # 団体割引
        if data.total >= settings.ZOO_TICKET["GROUP"]["THRESHOLD"]:
            data.total_discount = True
            data.discounts["ADULT"] = (
                data.prices["ADULT"] * settings.ZOO_TICKET["GROUP"]["ADULT"]
            )
            data.discounts["CHILD"] = (
                data.prices["CHILD"] * settings.ZOO_TICKET["GROUP"]["CHILD"]
            )
            data.discounts["SENIOR"] = (
                data.prices["SENIOR"] * settings.ZOO_TICKET["GROUP"]["SENIOR"]
            )

            data.prices["ADULT"] = int(data.prices["ADULT"] - data.discounts["ADULT"])
            data.prices["CHILD"] = int(data.prices["CHILD"] - data.discounts["CHILD"])
            data.prices["SENIOR"] = int(
                data.prices["SENIOR"] - data.discounts["SENIOR"]
            )

        # 変動後合計金額
        data.total_price_discount = sum(data.prices.values())

        # 結果表示
        self.output(data)

    # チケットプラン
    def check_plan(self, plan):
        match plan:
            case "NORMAL":
                return settings.ZOO_TICKET["NORMAL"]
            case "SPECIAL":
                return settings.ZOO_TICKET["SPECIAL"]
            case _:
                return settings.ZOO_TICKET["NORMAL"]

    # 曜日別料金変動計算
    def check_weekday(self, dt):
        weekday = dt.weekday()
        return settings.ZOO_TICKET["WEEKDAY"][weekday]

    # 時間帯別料金変動計算
    def check_time(self, dt):
        match dt.hour:
            case hour if hour in [5, 6, 7, 8, 9, 10]:
                return settings.ZOO_TICKET["TIME_TABLE"]["MORNING"]
            case hour if hour in [11, 12, 13, 14, 15, 16]:
                return settings.ZOO_TICKET["TIME_TABLE"]["NOON"]
            case hour if hour in [17, 18, 19, 20]:
                return settings.ZOO_TICKET["TIME_TABLE"]["EVENING"]
            case hour if hour in [21, 22, 23, 0, 1, 2, 3, 4]:
                return settings.ZOO_TICKET["TIME_TABLE"]["NIGHT"]
            case _:
                return 0

    # 結果表示
    def output(self, data):

        self.stdout.write("--------------------")
        self.stdout.write("合計金額: {}円".format(data.total_price_discount))
        self.stdout.write("合計金額(変更前): {}円".format(data.total_price))
        self.stdout.write("--------------------")

        if data.weekday_discount != 0:
            self.stdout.write("曜日金額変更: {}円".format(data.weekday_discount))
        if data.time_discount != 0:
            self.stdout.write("時間帯金額変更: {}円".format(data.time_discount))
        if data.total_discount:
            self.stdout.write("団体割引: 有 ")

        if data.adults:
            if data.total_discount:
                self.stdout.write(
                    "大人チケット: {}円 x {}人 = {}円 ({}%割引)".format(
                        (
                            data.ticket_prices["ADULT"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.adults,
                        data.prices["ADULT"],
                        int(settings.ZOO_TICKET["GROUP"]["ADULT"] * 100),
                    )
                )
            else:
                self.stdout.write(
                    "大人チケット: {}円 x {}人 = {}円".format(
                        (
                            data.ticket_prices["ADULT"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.adults,
                        data.prices["ADULT"],
                    )
                )
        if data.childs:
            if data.total_discount:
                self.stdout.write(
                    "子供チケット: {}円 x {}人 = {}円 ({}%割引)".format(
                        (
                            data.ticket_prices["CHILD"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.childs,
                        data.prices["CHILD"],
                        int(settings.ZOO_TICKET["GROUP"]["CHILD"] * 100),
                    )
                )
            else:
                self.stdout.write(
                    "子供チケット: {}円 x {}人 = {}円".format(
                        (
                            data.ticket_prices["CHILD"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.childs,
                        data.prices["CHILD"],
                    )
                )
        if data.seniors:
            if data.total_discount:
                self.stdout.write(
                    "シニアチケット: {}円 x {}人 = {}円 ({}%割引)".format(
                        (
                            data.ticket_prices["SENIOR"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.seniors,
                        data.prices["SENIOR"],
                        int(settings.ZOO_TICKET["GROUP"]["SENIOR"] * 100),
                    )
                )
            else:
                self.stdout.write(
                    "シニアチケット: {}円 x {}人 = {}円".format(
                        (
                            data.ticket_prices["SENIOR"]
                            + data.weekday_discount
                            + data.time_discount
                        ),
                        data.seniors,
                        data.prices["SENIOR"],
                    )
                )
