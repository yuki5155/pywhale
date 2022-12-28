import boto3
import calendar
from datetime import date, timedelta, datetime


class AwsCostBase:
    client = boto3.client('ce')
    # 半年前
    start_date = None
    # 今日
    end_date = None

    def __init__(self):
        self.check_dates()
        costs = self.client.get_cost_and_usage(
            TimePeriod={
                'Start': self.start_date,
                'End': self.end_date
            },
            Granularity='MONTHLY',
            Metrics=['BlendedCost']
        )['ResultsByTime']
        self.costs = sorted(
            costs, 
            key=lambda item: datetime.strptime(
                item['TimePeriod']['End'], 
                '%Y-%m-%d'), 
            reverse=True
        )
    
    def check_dates(self):
        if self.start_date is None:
            raise ValueError("start_date is required")
        if self.end_date is None:
            raise ValueError("end_date is required")

    def get_current_cost(self):
         return self.costs[0]["Total"]['BlendedCost']["Amount"]


def get_last_day_cuurent_month():
    # 今月最後の日を取得
    last_day = calendar.monthrange(date.today().year, date.today().month)[1]

    # formatを整える
    last_day_formatted = date.today().strftime("%Y-%m-") + str(last_day)

    return last_day_formatted

def get_firstday_three_month_ago():
    # 3ヶ月前の日にち
    start_date = date.today() - timedelta(days=90)
    start_date = start_date.replace(day=1)
    # Format the start date in the format YYYY-MM-DD
    start_date_formatted = start_date.strftime("%Y-%m-%d")

    return start_date_formatted

class AwsCost(AwsCostBase):
    start_date = get_firstday_three_month_ago()
    end_date = get_last_day_cuurent_month()
    