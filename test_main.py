from main import calcBMI, BMI
import pytest



'''     Height  Weight  BMI
One     74      200     26.297
Two     60      100     20.0
Three   84      150     15.306
Four    36      500     277.778
'''
one = (74, 200, 26.297)
two = (60, 100, 20.0)
three = (84, 150, 15.306)
four = (36, 500, 277.778)
test = [one, two, three, four]
@pytest.mark.parametrize("inches, weight, output", test)
def test_calcBMI(inches, weight, output):
    assert calcBMI(inches, weight) == pytest.approx(output, .001) 



'''             OFF1     ON1    Interior    OFF2    ON2
Underweight     18.5    17.5    0
Normal Weight   17.5    18.5    22          24      25
Overweight      24      25      27          29      30
Obese           29      30      40
'''

test = [(18.5, "Normal Weight"), (17.5, "Underweight"), (0, "Underweight"),
(17.5, "Underweight"), (18.5, "Normal Weight"), (22, "Normal Weight"), (24, "Normal Weight"), (25, "Overweight"),
(24, "Normal Weight"), (25, "Overweight"), (27, "Overweight"), (29, "Overweight"), (30, "Obese"),
(29, "Overweight"), (30, "Obese"), (40, "Obese")]
@pytest.mark.parametrize("input, output", test)
def test_BMI(input, output):
    assert BMI(input) == output 
