import pytest
import subprocess
import sys

def run_script(script, args=None):
    cmd = [sys.executable, str(script)]
    if args:
        cmd += list(args)
    completed = subprocess.run(cmd, capture_output=True, text=True)
    assert completed.returncode == 0, f"Script {script} exited with {completed.returncode}: {completed.stderr}"
    return completed.stdout.strip()


def assert_output_contains_pairs(output, pairs):
    lines = output.splitlines()
    for a, b in pairs:
        a_s = str(a)
        b_s = str(b)
        found = any((a_s in line and b_s in line) for line in lines)
        assert found, f"Expected a line containing both '{a_s}' and '{b_s}'"

def test_q1():
    # run 1.py and capture output
    output = run_script('1.py')
    for year in range(2005, 2025):
        assert str(year) in output

def test_q2():
    output = run_script('2.py')
    expected_types = ['Break and Enter Commercial', 'Break and Enter Residential/Other', 'Homicide', 'Mischief', 'Offence Against a Person', 'Other Theft', 'Theft from Vehicle', 'Theft of Bicycle', 'Theft of Vehicle', 'Vehicle Collision or Pedestrian Struck (with Fatality)', 'Vehicle Collision or Pedestrian Struck (with Injury)']
    for crime_type in expected_types:
        assert crime_type in output

def test_q3():
    output = run_script('3.py')
    expected = [
        (2003, 26),
        (2004, 25),
        (2005, 38),
        (2006, 26),
        (2007, 30),
        (2008, 20),
        (2009, 17),
        (2010, 13),
        (2011, 13),
        (2012, 19),
        (2013, 16),
        (2014, 14),
        (2015, 15),
        (2016, 15),
        (2017, 16),
        (2018, 14),
        (2019, 14),
        (2020, 8),
        (2021, 28),
        (2022, 19),
        (2023, 17),
        (2024, 8),
    ]
    assert_output_contains_pairs(output, expected)

def test_q4():
    output = run_script('4.py')
    assert '2015' in output
    assert 'Central Business District' in output
    assert '7' in output

def test_q5():
    output = run_script('5.py')
    assert 'Killarney' in output

def test_q6():
    output = run_script('6.py')
    assert 'Central Business District' in output
    
def test_q7():
    output = run_script('7.py')
    expected_line = '2017,435,13401,519,2162,2407,1440,1701,469,713,1876,1038,2851,30,644,2362,1006,490,398,208,2949,1029,803,3813,461'
    assert expected_line in output

def test_q8_no_arg():
    completed = subprocess.run([sys.executable, '8.py'], capture_output=True, text=True)
    assert completed.returncode != 0
    assert "Usage: python 8.py <NEIGHBOURHOOD>" in completed.stdout
    assert "Here are the available neighbourhoods:" in completed.stdout
    assert "Oakridge" in completed.stdout
    assert "Fairview" in completed.stdout

def test_q8_with_arg():
    output = run_script('8.py', args=['Killarney'])
    expected = [
        (2003, 1044),
        (2004, 1313),
        (2005, 1228),
        (2006, 1116),
        (2007, 958),
        (2008, 693),
        (2009, 765),
        (2010, 715),
        (2011, 638),
        (2012, 772),
        (2013, 610),
        (2014, 725),
        (2015, 694),
        (2016, 637),
        (2017, 713),
        (2018, 681),
        (2019, 733),
        (2020, 594),
        (2021, 522),
        (2022, 600),
        (2023, 578),
        (2024, 388),
    ]
    assert_output_contains_pairs(output, expected)