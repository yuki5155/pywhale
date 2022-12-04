from costs_base import AwsCost

def test_aws_sample():
   
    aws_cost = AwsCost()
    try:
        current_cost = float(aws_cost.get_current_cost())
        assert type(current_cost) == float
    except:
        raise TypeError("script does not work")

