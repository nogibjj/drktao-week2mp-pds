from main import denirostats

def test_deniro():
    assert denirostats('deniro.csv')['Mean Score']==58.1954023
    assert denirostats('deniro.csv')['Median Score']==65
    assert denirostats('deniro.csv')['Standard Deviation of Scores']==28.06754274

